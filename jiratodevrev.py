import pandas as pd
import requests
import json
import time

# Configurations
CSV_FILE = "Book1.csv"
DEVREV_PAT = "YOUR_DEVREV_PAT"  # Replace with your DevRev Personal Access Token
DEVREV_PART_ID = "PROD-3"  # Replace with actual part ID from DevRev
DEVREV_USER_ID = "DEVU-1"  # Replace with your DevRev user ID


jira_to_devrev_stage = {
    "Open": "queued",
    "Pending": "awaiting_customer_response",
    "Waiting for support": "awaiting_product_assist",
    "Work in progress": "work_in_progress",
    "In Progress": "work_in_progress",
    "Waiting for approval": "awaiting_customer_response",
    "Done": "resolved",
    "Completed": "resolved",
    "Resolved": "resolved",
    "Cancelled": "canceled"
}

# Read and clean CSV
df = pd.read_csv(CSV_FILE)
df = df[df["Summary"].notna()]

# Create tickets
for index, row in df.iterrows():
    title = row["Summary"].strip()
    description = str(row["Description"]) if not pd.isna(row["Description"]) else "No description provided"
    status = row["Status"].strip()

    # Map Jira status to DevRev stage name
    devrev_stage_name = jira_to_devrev_stage.get(status, "queued")  # default fallback

    payload = {
        "type": "ticket",
        "applies_to_part": DEVREV_PART_ID,
        "owned_by": [DEVREV_USER_ID],
        "title": title,
        "body": description,
        "stage": {
            "name": devrev_stage_name
        }
    }

    response = requests.post(
        "https://api.devrev.ai/works.create",
        headers={
            "Authorization": f"Bearer {DEVREV_PAT}",
            "Content-Type": "application/json"
        },
        json=payload
    )

    if response.status_code == 201:
        print(f"✅ Created: {title} ({status} → {devrev_stage_name})")
    else:
        print(f"❌ Failed to create: {title} | Status: {status} → {devrev_stage_name}\n    {response.status_code} {response.text}")

    time.sleep(1)