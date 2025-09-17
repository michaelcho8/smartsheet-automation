import requests
import smartsheet
import os
import csv
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import smartsheet_client, SHEET_ID, ACCESS_TOKEN, EMAIL_RECIPIENTS # Importing API Endpoint (URL), smartsheet client, and email recipients
from backup import backup_sheet_to_csv
from row_evaluators import evaluate_row_and_build_updates

# # Fetch all rows from the sheet and Initialize client. Uses the API token in the environment variable "SMARTSHEET_ACCESS_TOKEN"
sheet = smartsheet_client.Sheets.get_sheet(SHEET_ID)
print(f"Total Rows in Sheet: {sheet.total_row_count}")

# Backup the sheet before making updates
backup_sheet_to_csv(sheet, backup_dir="backups")

# List to hold rows that need to be updated
rows_to_update = []

# Store column IDs into column_map dictionary with column titles
column_map = {}
for column in sheet.columns:
    if column.id is None:
        print(f"Warning: Column '{column.title}' not found in the sheet. Skipping...")
        continue
    column_map[column.title] = column.id
    print(f"Column ID for '{column.title}': {column.id}")

def get_cell_by_column_title(row, column_title):
    # Retrieves a cell from a row by column title.
    column_id = column_map[column_title]
    return row.get_column(column_id)

# Accumulate rows needing update here
rows_to_update = []

print("Evaluating rows for updates...")
for row in sheet.rows:
    row_to_update = evaluate_row_and_build_updates(
        row,
        "Current Status",
        get_cell_by_column_title=get_cell_by_column_title,
        column_map=column_map,
        smartsheet_client=smartsheet_client
    )
    print("In loop")
    if row_to_update is not None:
        rows_to_update.append(row_to_update)
print(f"Total rows to update: {len(rows_to_update)}")

# Update rows in smartsheet
if rows_to_update:
    smartsheet_client.Sheets.update_rows(sheet, rows_to_update)
    print(f"Updated {len(rows_to_update)} rows in the sheet.")
else:
    print("No rows needed updating.")