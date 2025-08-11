import requests
import smartsheet
import os

# The API endpoint
url = "https://app.smartsheet.com/sheets/p27W9cFxxg9VF7xj86GMVhw79qJmPvVgJ65G8MP1"

sheet_id = 1794600033275780

dir_name = "Downloaded Excel Files"
if not os.path.isdir(dir_name):
    os.makedirs(dir_name)
else:
    print(f'Directory "{dir_name}" already exists.')

sheet = smartsheet_client.Sheets.get_sheet_as_excel(sheet_id, dir_name)

# A GET request to the API
response = requests.get(url)

# Print the response
print(response.json())
