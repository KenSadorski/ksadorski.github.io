# Ken Sadorski's Cybersecurity Portfolio

Welcome to my professional GitHub Pages portfolio, showcasing my projects, skills, and experience in cybersecurity. This portfolio is designed to serve as a central hub for my written reports, code projects, and video demonstrations. Explore each section to learn more about my work and capabilities.

## Table of Contents
- [Projects](#projects)
  - [Python Scripts](#python-scripts)
  - [PowerShell Scripts](#powershell-scripts)
  - [Written Reports](#written-reports)
  - [Video Demonstrations](#video-demonstrations)
- [Certifications](#certifications)
- [Resume](#resume)
- [Connect with Me](#connect-with-me)

---

## Projects

# Python Scripts

### 1. `tokens.py`
- **Description**: Tracks the number of tokens won over multiple game rounds.
- **Key Features**:
  - Takes input for the tokens won per game.
  - Calculates and displays the total, average, minimum, and maximum tokens won.

### 2. `SortingInPython.py`
- **Description**: Demonstrates list manipulation and sorting techniques.
- **Key Features**:
  - Declares and fills a list.
  - Sorts the list in both ascending and descending order.
  - Uses reverse and sort functions to modify list order.

### 3. `Login_Script.py`
- **Description**: Implements a simple authentication system.
- **Key Features**:
  - Allows up to 5 login attempts before locking the user out.
  - Provides feedback after each failed attempt, showing remaining attempts.
  - Uses predefined username and password constants for validation.

### 4. `CaesarCipher_improved.py`
- **Description**: A Caesar Cipher implementation for encrypting and decrypting text.
- **Key Features**:
  - Supports both uppercase and lowercase letters.
  - Allows users to choose encryption or decryption mode.
  - Shifts characters based on a specified key while preserving non-alphabet characters.

### 5. `supermario.py`
- **Description**: A fun ASCII art-based script where users can select a character and find different colored Yoshis.
- **Key Features**:
  - Allows user to select between characters and stages.
  - Displays ASCII art based on the chosen stage and character.
  - Outputs different Yoshi ASCII art for each stage.

### 6. `redactedreport.py`
- **Description**: Redacts specific personally identifiable information (PII) from a Word document.
- **Key Features**:
  - Searches for a list of specified PII terms in a `.docx` file.
  - Replaces each term with “[REDACTED]”.
  - Saves the redacted document to a specified location.

### 7. `home_network_ip_scanner.py`
- **Description**: Scans a specified IP range (default: `192.168.50.1/24`) to detect active devices and resolve their hostnames.
- **Key Features**:
  - Uses `ping` to check if each IP address in the range is active.
  - Attempts to retrieve the hostname of active IPs.
  - Saves the scan results, including status and hostnames, to a text file.

Each script demonstrates my familiarity with Python's built-in libraries and basic scripting concepts, tailored to various practical use cases. Feel free to explore the scripts and refer to their inline comments for additional details on their functionality.
---

- **[Token Counter](./assets/Scripts/Python/tokens.py):** Tracks tokens won over multiple games.
- **[Sorting Example](./assets/Scripts/Python/SortingInPython.py):** Demonstrates list sorting techniques.
- **[Login Script](./assets/Scripts/Python/Login_Script.py):** Implements a simple login authentication system with limited attempts.
- **[Caesar Cipher](./assets/Scripts/Python/CaesarCipher_improved.py):** Encrypts and decrypts text using the Caesar Cipher algorithm.
- **[Super Mario Game](./assets/Scripts/Python/supermario.py):** ASCII art-based Mario game where players find different colored Yoshis.
- **[Redacted Report Generator](./assets/Scripts/Python/redactedreport.py):** Redacts sensitive information from a document based on specific keywords.
- **[Home Network IP Scanner](./assets/Scripts/Python/home_network_ip_scanner.py):** Scans a specified IP range to detect active devices and retrieve hostnames.

### PowerShell Scripts
Collection of PowerShell scripts focused on network automation, configuration, and analysis.

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

These scripts demonstrate my ability to automate system management tasks and perform network security checks using PowerShell. Each script is documented with comments to guide the user on setup and execution.
---
- **[Domain Join Script](./assets/Scripts/PowerShell/DomainJoin_improved.ps1):** Automates joining a Windows computer to a domain using secure credentials.
- **[WMI Queries](./assets/Scripts/PowerShell/WMIQueries.ps1):** Executes predefined WMI queries to retrieve specific system information.
- **[SSL Support Checker](./assets/Scripts/PowerShell/SSLSupport_revised.ps1):** Tests support for various SSL/TLS protocols on a specified server.

---

### Written Reports

This section contains various technical reports showcasing my skills in network design, security analysis, and policy creation. Each document covers a distinct area of cybersecurity and IT management.

### 1. Network Design Proposal
- **Description**: This proposal addresses a network upgrade from a 10-100Mbps network to a managed Gigabit Ethernet-compatible network.
- **Highlights**:
  - Migration to Cisco 3800 series switches with 10Gbps uplinks.
  - Implementation of wireless access points and a new ASA 5585 firewall.
  - Plan for a 5% growth in network capacity over the next five years.
  - Enhanced security features, including centralized log monitoring and VPN support.
  - Please see the VLAN_revised.xlsx document for additional information 
  
### 2. Business Proposal (Revised)
- **Description**: A strategic proposal aimed at improving employee satisfaction and operational efficiency within a business.
- **Highlights**:
  - Analysis of Paid Time Off (PTO) policy, suggesting an open PTO model.
  - Recommendations for flexible scheduling and remote work to expand the talent pool.
  - Enhanced onboarding practices inspired by Google’s integration methods to improve employee retention and engagement.
  
### 3. Acceptable Use Policy (AUP)
- **Description**: A policy designed to secure company data and guide employees in ethical and secure use of company resources.
- **Highlights**:
  - Defines acceptable and unacceptable uses of company systems.
  - Establishes email usage guidelines, including encryption requirements for sensitive information.
  - Sets monitoring standards to ensure compliance and data protection.
  
### 4. Network Diagram
- **Description**: A detailed network diagram illustrating the network architecture across various departments and rooms within an organization.
- **Highlights**:
  - Layout of network components including switches, routers, and access points.
  - Fiber and cable runs between locations, with distances for each segment.
  - VLAN allocation for VOIP and other network services.
  
### 5. Security Analysis
- **Description**: A comprehensive vulnerability assessment conducted for a business, covering network security, physical security, and user education.
- **Highlights**:
  - Identification of top security risks, including unsecured wireless devices and lack of password protection.
  - Evaluation of network and wireless security measures, including WPA-2 encryption and firewall configuration.
  - Recommendations for improving physical security, user education, and AAA (Authorization, Authentication, Accounting) protocols.

Each report demonstrates my analytical abilities and commitment to enhancing security and operational efficiency within IT environments.
PLEASE NOTE: these reports have had images removed and PII redacted for security purposes. 
---

- **[Network Design Proposal](./assets/Written_Reports/NetworkDesignProposal_redacted.pdf):** Proposal for upgrading a network to managed Gigabit Ethernet.
- **[Business Proposal](./assets/Written_Reports/BusinessProposal_revised.pdf):** Strategic proposal for improving employee satisfaction and operational efficiency.
- **[Acceptable Use Policy](./assets/Written_Reports/AcceptableUsePolicy_redacted.pdf):** Policy defining acceptable use of company resources to ensure security.
- **[Network Diagram](./assets/Written_Reports/NetworkDiagram_redacted.pdf):** Diagram illustrating network architecture across departments and rooms.
- **[Security Analysis](./assets/Written_Reports/SecurityAnalysis_redacted.pdf):** Vulnerability assessment report covering network security, physical security, and user education.

### Video Demonstrations
Video walkthroughs and tutorials demonstrating cybersecurity techniques and tools.
Please note, you will have to download these files to view them as they are too large to be hosted on github. 
I am in the process of creating a YouTube channel for content such as this. 

# Video Descriptions

### 1. `RAT_Demo.webm`
- **Description**: Demonstrates the detection and analysis of a Remote Access Trojan (RAT).
- **Highlights**:
  - Explains how a RAT operates and its potential impact on network security.
  - Shows step-by-step procedures for identifying RAT activity within a network.
  - Discusses key indicators of compromise (IOCs) and the importance of monitoring.

### 2. `RDPSecurity.webm`
- **Description**: A guide on securing Remote Desktop Protocol (RDP) connections.
- **Highlights**:
  - Provides an overview of RDP security risks and best practices.
  - Demonstrates methods to secure RDP, including configuring network-level authentication and implementing firewall rules.
  - Covers techniques for monitoring and restricting RDP access to improve security posture.

These videos demonstrate my hands-on experience with security practices and tools, emphasizing both detection and prevention techniques. Each video is intended to provide insight into real-world cybersecurity applications.
---

- **[RAT Demo](./assets/Video_Demos/RAT_Demo.webm):** Demonstrates detection and analysis of a Remote Access Trojan (RAT).
- **[RDP Security Guide](./assets/Video_Demos/RDPSecurity.webm):** Guide on securing Remote Desktop Protocol (RDP) connections.

## Certifications
View a list of my professional certifications in cybersecurity, including:
- **CompTIA CySA+**
- **Splunk Certified Core User**
- **CompTIA Security+**
- **CompTIA Network+**
- **Google Cybersecurity**
- **Microsoft AZ-900** (Azure Fundamentals)
  
For more details on certifications, view **Certifications:** [https://kensadorski.github.io/ksadorski.github.io/certifications]

---

## Resume
My resume, showcasing my experience and skills, is available upon request or viewable [here](./_data/resume.yml) (in YAML format).

## Connect with Me
- **LinkedIn:** [https://www.linkedin.com/in/ken-sadorski-cyber/]
- **Email:** [ksadorski@koiosknowledge.com](mailto:ksadorski@koiosknowledge.com)
- **Try Hack Me:** [https://tryhackme.com/r/p/owloperator]

---

This portfolio is continually updated with new projects, so feel free to check back regularly for updates.
