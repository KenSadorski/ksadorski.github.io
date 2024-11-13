# Parameters for flexibility
param (
    [string]$ComputerName = "CLIENT2_Win11",
    [string]$DomainName = "lab",
    [string]$LocalUsername = "administrator",
    [string]$DomainUsername = "lab\administrator"
)

# Prompt for the password securely
Write-Host "Enter the password for both local and domain administrator accounts:" -ForegroundColor Yellow
$pw = Read-Host -AsSecureString

# Create secure credential objects
$localCredential = New-Object System.Management.Automation.PSCredential ($LocalUsername, $pw)
$domainCredential = New-Object System.Management.Automation.PSCredential ($DomainUsername, $pw)

# Try to join the domain and handle errors
try {
    Add-Computer -ComputerName $ComputerName -LocalCredential $localCredential -DomainName $DomainName -Credential $domainCredential -Restart -ErrorAction Stop
    Write-Host "Successfully joined $ComputerName to the domain $DomainName." -ForegroundColor Green
} catch {
    Write-Host "Failed to join the domain. Error: $_" -ForegroundColor Red
}

# Logging (Optional): You can add logging to a file for better tracking
# Example:
# $logPath = "C:\Path\To\Your\LogFile.txt"
# Add-Content -Path $logPath -Value "$(Get-Date): Attempted to join $ComputerName to $DomainName"
