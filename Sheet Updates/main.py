import requests
import smartsheet
import os
import csv
import datetime
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import smartsheet_client, SHEET_ID, EMAIL_RECIPIENTS # Importing API Endpoint (URL), smartsheet client, and email recipients
from backup import backup_sheet_to_csv
from read_write_sheet import initialize_column_map, evaluate_row_and_build_updates, build_rows_to_update

# # Fetch all rows from the sheet and Initialize client. Uses the API token in the environment variable "SMARTSHEET_ACCESS_TOKEN"
sheet = smartsheet_client.Sheets.get_sheet(SHEET_ID)
print(f"Total Rows in Sheet: {sheet.total_row_count}")

# Backup the sheet before making updates
backup_sheet_to_csv(sheet, backup_dir="backups")

# Store column IDs into column_map dictionary with column titles
column_map = initialize_column_map(sheet)
# ! Testing function in read_write_sheet.py
# for column in sheet.columns:
#     if column.id is None:
#         print(f"Warning: Column '{column.title}' not found in the sheet. Skipping...")
#         continue
#     column_map[column.title] = column.id
#     print(f"Column ID for '{column.title}': {column.id}")

# def get_cell_by_column_title(row, column_title):
#     # Retrieves a cell from a row by column title.
#     column_id = column_map[column_title]
#     return row.get_column(column_id)

updates_col_id = column_map["Column11"]  # Replace with your actual "Updates" column name if different

# Accumulate rows needing update here
rows_to_update = []

print("Evaluating rows for updates...")

rows_to_update = build_rows_to_update(sheet, column_map, smartsheet_client, "Column11")

# for row in sheet.rows:
#     # row_to_update = evaluate_row_and_build_updates(row, "Column4", smartsheet_client)
#     # if row_to_update is not None:
#     #     rows_to_update.append(row_to_update)

#     # Get the current value in the Updates cell
#     updates_cell = next((cell for cell in row.cells if cell.column_id == updates_col_id), None)
#     updates_value = getattr(updates_cell, 'value', None) if updates_cell else None

#     # Prepare the new update note
#     update_note = f"{datetime.datetime.now().strftime('%m/%d/%Y')}: Accessed via API -MC"

#     # Combine with existing value
#     if updates_value is None:
#         combined_updates = update_note
#     else:
#         combined_updates = f"{updates_value}\n{update_note}"

#     # Create a new Cell object for the update
#     cell_to_update = smartsheet_client.models.Cell()
#     cell_to_update.column_id = updates_col_id
#     cell_to_update.value = combined_updates

#     # Create a Row object with the updated cell
#     row_to_update = smartsheet_client.models.Row()
#     row_to_update.id = row.id
#     row_to_update.cells = [cell_to_update]

#     rows_to_update.append(row_to_update)

print(f"Total rows to update: {len(rows_to_update)}")

# Update rows in smartsheet
if rows_to_update:
    response = smartsheet_client.Sheets.update_rows(SHEET_ID, rows_to_update)
    print("Update response:", response)
    # smartsheet_client.Sheets.update_rows(sheet, rows_to_update)
    # print(f"Updated {len(rows_to_update)} rows in the sheet.")
else:
    print("No rows needed updating.")