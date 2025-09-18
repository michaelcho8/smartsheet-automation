import smartsheet

ACCESS_TOKEN = 'w2wMKac07W77sYoUf9TaIyMH2UMeVGjPI4YL3'

# # API Endpoint
# URL = "https://app.smartsheet.com/sheets/p27W9cFxxg9VF7xj86GMVhw79qJmPvVgJ65G8MP1"

# Test URL
URL = "https://app.smartsheet.com/sheets/gv9mXfv6q3GWW3gHF4mmfv5QccXv5W5qGqhrVmP1"

# Our designated Access Token
smartsheet_client = smartsheet.Smartsheet(ACCESS_TOKEN)

# # Sheet ID for Control of NCR Register  WISA-DC-000081
# SHEET_ID = 1794600033275780

# Test Sheet ID
SHEET_ID = 2720818803986308

# Define the email recipients
EMAIL_RECIPIENTS = ["mcho@woojinisa.com"]