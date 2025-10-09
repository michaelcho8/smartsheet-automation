# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from config import smartsheet_client, SHEET_ID, EMAIL_RECIPIENTS # Importing API Endpoint (URL), smartsheet client, and email recipients
from backup import backup_sheet_to_csv
from read_write_sheet import initialize_column_map, build_rows_to_update

# # Fetch all rows from the sheet and Initialize client. Uses the API token in the environment variable "SMARTSHEET_ACCESS_TOKEN"
sheet = smartsheet_client.Sheets.get_sheet(SHEET_ID)
print(f"Total Rows in Sheet: {sheet.total_row_count}")

# Backup the sheet before making updates
backup_sheet_to_csv(sheet, backup_dir="backups")

# Store column IDs into column_map dictionary with column titles
column_map = initialize_column_map(sheet)

updates_col_id = column_map["Column11"]  # Replace with your actual "Updates" column name if different

# Accumulate rows needing update here
rows_to_update = []

print("Evaluating rows for updates...")

rows_to_update = build_rows_to_update(sheet, column_map, smartsheet_client, "Column11")

print(f"Total rows to update: {len(rows_to_update)}")

# Update rows in smartsheet
if rows_to_update:
    response = smartsheet_client.Sheets.update_rows(SHEET_ID, rows_to_update)
    print("Update response:", response)
else:
    print("No rows needed updating.")