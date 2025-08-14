import requests
import smartsheet
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import smartsheet_client, EMAIL_RECIPIENTS

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
    last_updated_cell = next(cell for cell in row.cells if cell.column_id == LAST_UPDATED_COLUMN)    
    ncr_number_cell = next(cell for cell in row.cells if cell.column_id == NCR_NUMBER_COLUMN)
    
