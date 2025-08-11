import smartsheet

def main ():
    # Initialize the Smartsheet client
    smartsheet_client = smartsheet.SmartsheetClient()

    # Fetch the list of sheets
    sheets = smartsheet_client.ListSheets()

    # Print the names of the sheets
    for sheet in sheets:
        print(sheet.name)