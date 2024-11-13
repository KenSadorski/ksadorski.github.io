# Place all using directives for namespaces at the very top of the script
using namespace System.Net.Security
using namespace System.Security.Cryptography.X509Certificates

[CmdletBinding()]
param(
    [string]$HostName = "ENTER HOST NAME HERE",
    [UInt16]$Port = 17472,
    [switch]$force,
    [string[]]$Protocols = @("ssl2", "ssl3", "tls", "tls11", "tls12", "tls13")
)

# Define log file path
$logFile = "C:\Path\To\LogFile.txt"

# Updated Write-Log function to create directory if it doesn't exist
function Write-Log {
    param([string]$message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    
    # Ensure the directory exists
    $logDir = [System.IO.Path]::GetDirectoryName($logFile)
    if (!(Test-Path -Path $logDir)) {
        New-Item -ItemType Directory -Path $logDir -Force | Out-Null
    }
    
    # Add content to the log file
    Add-Content -Path $logFile -Value "$timestamp - $message"
}

Write-Log "Starting SSL/TLS check on $($HostName):$($Port)"

try {
    # Check if the host is reachable on the specified port
    if (-not (Test-NetConnection -ComputerName $HostName -Port $Port).TcpTestSucceeded) {
        throw "Could not connect to $($HostName) on port $($Port)"
    }
} catch {
    Write-Log "Connection error: $_"
    if (-not $force) { throw $_ }
}

# Initialize properties for output
$Props = [ordered]@{
    Host = $HostName
    Port = $Port
    SSLv2 = $false
    SSLv3 = $false
    TLSv1_0 = $false
    TLSv1_1 = $false
    TLSv1_2 = $false
    TLSv1_3 = $false
    CertInfo = $null
}

# Loop through each specified protocol to test its support
$Protocols | ForEach-Object {
    $protocol = $_
    Write-Log "Testing $protocol support"
    try {
        # Create a new TCP client connection
        $TcpClient = New-Object Net.Sockets.TcpClient
        $TcpClient.Connect($HostName, $Port)
        
        # Create an SSL stream for the TCP client
        $SslStream = New-Object Net.Security.SslStream ($TcpClient.GetStream()), $true, ([System.Net.Security.RemoteCertificateValidationCallback]{ $true })
        $SslStream.ReadTimeout = 15000
        $SslStream.WriteTimeout = 15000

        # Attempt to authenticate using the specified protocol
        $SslStream.AuthenticateAsClient($HostName, $null, $protocol, $false)
        $Props["TLSv$protocol"] = $true

        # Dispose of the resources
        $SslStream.Dispose()
        $TcpClient.Dispose()
    } catch {
        Write-Log "Protocol $protocol not supported"
        $Props["TLSv$protocol"] = $false
        
        # Dispose of resources in case of error
        if ($SslStream) { $SslStream.Dispose() }
        if ($TcpClient) { $TcpClient.Dispose() }
    }
}

# Convert properties to an object and output the results in a table format
$Result = New-Object psobject -Property $Props
$Result | Format-Table -AutoSize

Write-Log "SSL/TLS check complete for $($HostName):$($Port)"
