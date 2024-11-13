# Define the output directory
$outputDir = "C:\Temp"

# Ensure the output directory exists
if (-Not (Test-Path -Path $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir
}

# Define the queries and output file paths
$queries = @(
    @{
        Query = "Select SystemType from Win32_ComputerSystem"
        OutputFile = Join-Path -Path $outputDir -ChildPath "SystemType_Output.txt"
    },
    @{
        Query = "Select Family from Win32_Processor"
        OutputFile = Join-Path -Path $outputDir -ChildPath "Family_Output.txt"
    },
    @{
        Query = "Select Version from Win32_OperatingSystem"
        OutputFile = Join-Path -Path $outputDir -ChildPath "Version_Output.txt"
    }
)

# Function to execute a WMI query and save the output
function Execute-WmiQuery {
    param (
        [string]$query,
        [string]$outputFile
    )

    # Execute the query
    $result = Get-WmiObject -Query $query

    # Save the output to the file
    $result | Out-File -FilePath $outputFile
}

# Run the queries and save the outputs
foreach ($query in $queries) {
    Execute-WmiQuery -query $query.Query -outputFile $query.OutputFile
}

Write-Host "Queries executed and output saved to $outputDir"
