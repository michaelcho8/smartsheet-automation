import smartsheet

ACCESS_TOKEN = 'w2wMKac07W77sYoUf9TaIyMH2UMeVGjPI4YL3'

# API Endpoint
URL = "https://app.smartsheet.com/sheets/p27W9cFxxg9VF7xj86GMVhw79qJmPvVgJ65G8MP1"

smartsheet_client = smartsheet.Smartsheet(ACCESS_TOKEN)

# Define the email recipients
EMAIL_RECIPIENTS = ["mcho@woojinisa.com"]