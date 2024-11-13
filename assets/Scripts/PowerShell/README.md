# PowerShell Scripts

This folder contains a set of PowerShell scripts for various system management and security tasks. Below is a summary of each script.

## Scripts Included

### 1. `DomainJoin_improved.ps1`
- **Description**: Automates the process of joining a Windows computer to a domain.
- **Key Features**:
  - Uses secure credentials to authenticate and join the domain.
  - Configures the computer with the specified domain and user credentials.
  - Optionally restarts the computer after successfully joining the domain.

### 2. `WMIQueries.ps1`
- **Description**: Runs predefined WMI (Windows Management Instrumentation) queries to retrieve specific system information.
- **Key Features**:
  - Executes queries to gather details such as system type, processor family, and OS version.
  - Saves query results to text files for later analysis.
  - Useful for system audits and inventory tracking.

### 3. `SSLSupport_revised.ps1`
- **Description**: Checks SSL/TLS support on a specified server and verifies available protocol versions.
- **Key Features**:
  - Tests support for various SSL/TLS protocols (e.g., TLS 1.0, 1.1, 1.2, 1.3).
  - Connects to a specified hostname and port to verify supported encryption protocols.
  - Outputs a summary of supported protocols and includes optional logging to a file.

---

These scripts demonstrate my ability to automate system management tasks and perform network security checks using PowerShell. Each script is documented with comments to guide the user on setup and execution.
