import requests
import smartsheet
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import smartsheet_client

# The API endpoint
url = "https://app.smartsheet.com/sheets/p27W9cFxxg9VF7xj86GMVhw79qJmPvVgJ65G8MP1"

sheet_id = 1794600033275780

# Define the column names
LAST_UPDATED_COLUMN = "Last Updated"
NCR_NUMBER_COLUMN = "NCR Number"

# Get the current date
two_weeks_ago = datetime.datetime.now() - datetime.timedelta(weeks=2)

# Fetch all rows from the sheet
sheet = smartsheet_client.Sheets.get_sheet(sheet_id)
rows_to_update = []

# Iterate through each row in the sheet
for row in sheet.rows:
    print(f"Processing Row ID: {row.row_number}")

cell_update = smartsheet.models.Cell()
cell_update.column_id = YOUR_COLUMN_ID
cell_update.row_id = YOUR_ROW_ID
cell_update.value = "Your Value"
cell_update.format = "1,1,1,1,1,1,1,1,1,6"  # Example: bold, red font

smartsheet_client.Sheets.update_rows(sheet_id, [smartsheet.models.Row({
    'id': YOUR_ROW_ID,
    'cells': [cell_update]
})])
    
print(f"Current Row and NCR Number: {ncr_number_cell}\n Last Updated: {last_updated_cell}")