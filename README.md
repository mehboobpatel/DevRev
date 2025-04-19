# CloudOps Support Portal

This repository contains the CloudOps Support Portal, which integrates the DevRev Plug chat widget and provides scripts to import Jira tickets into DevRev.

## 1. Integrated DevRev Plug Chat Widget

The landing page (`demo.html`) includes the DevRev Plug chat widget, enabling seamless customer interaction. The widget is initialized using the `APP_ID` securely injected via the server (`server.js`). For more details, refer to the [DevRev Plug documentation](https://devrev.ai/docs/plug).

## 2. Hosting on Azure

This application is hosted on Azure Web App. The Personal Access Token (PAT) for DevRev API is securely stored and accessed internally using Azure's environment variable management. This ensures sensitive data is not exposed in the codebase.

## 3. Importing Jira Tickets into DevRev

The `Jiraexported.csv` file, exported from Jira Service Management, can be processed and imported into DevRev using two scripts: one in Python and another in TypeScript.

### Python Script (`jiratodevrev.py`)

#### Overview
This script uses the following packages:
- **pandas**: For reading and processing the CSV file.
- **requests**: For making HTTP requests to the DevRev API.
- **time**: To add delays between API calls to avoid rate limiting.

#### Key Functions
1. **CSV Processing**: Reads and filters rows with valid summaries.
2. **Status Mapping**: Maps Jira statuses to DevRev stages using a dictionary.
3. **Ticket Creation**: Sends POST requests to the DevRev API to create tickets.

#### Usage
- Update the `CSV_FILE` path and DevRev configurations (`DEVREV_PAT`, `DEVREV_PART_ID`, `DEVREV_USER_ID`).
- Run the script to process the CSV and create tickets in DevRev.

### TypeScript Script (`jiratodevrev.ts`)

#### Overview
This script uses the following packages:
- **fs**: For file system operations.
- **csv-parser**: For parsing the CSV file.
- **axios**: For making HTTP requests to the DevRev API.
- **strip-bom-stream**: To handle UTF-8 BOM in the CSV file.

#### Key Functions
1. **CSV Processing**: Reads and parses the CSV file, skipping empty rows.
2. **Status Mapping**: Maps Jira statuses to DevRev stages using a dictionary.
3. **Ticket Creation**: Sends POST requests to the DevRev API to create tickets.

#### Usage
- Update the `CSV_FILE` path and DevRev configurations (`DEVREV_PAT`, `DEVREV_PART_ID`, `DEVREV_USER_ID`).
- Run the script to process the CSV and create tickets in DevRev.

## 4. References
- [DevRev Plug Documentation](https://devrev.ai/docs/plug)
- [DevRev API Reference: Create Works](https://developer.devrev.ai/beta/api-reference/works/create)
- [DevRev Authentication](https://developer.devrev.ai/about/authentication)
