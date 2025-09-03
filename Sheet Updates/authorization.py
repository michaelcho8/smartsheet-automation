import requests
import smartsheet
import os
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import smartsheet_client, ACCESS_TOKEN, SHEET_ID, EMAIL_RECIPIENTS # Importing API Endpoint (URL), smartsheet client, and email recipients

# Get the current date
two_weeks_ago = datetime.datetime.now() - datetime.timedelta(weeks=2)

# Fetch all rows from the sheet
sheet = smartsheet_client.Sheets.get_sheet(SHEET_ID)
rows_to_update = []

# Store column IDs into column_map dictionary with column titles
column_map = {}
for column in sheet.columns:
    if column.id is None:
        print(f"Warning: Column '{column.title}' not found in the sheet. Skipping...")
        continue
    column_map[column.title] = column.id
    print(f"Column ID for '{column.title}': {column.id}")


def get_cell_by_column_name(row, column_name):
    # Retrieves a cell from a row by column name.
    column_id = column_map[column_name]
    return row.get_column(column_id)

# # Extract row_id for a specific row (e.g., based on a cell value in the column)
# row_id = None
# target_value = 5  # Replace with the value you're looking for
# for row in sheet.rows:
#     for cell in row.cells:
#         if cell.column_id == column_id and cell.value == target_value:
#             row_id = row.id
#             break
#     if row_id is not None:
#         break

# if row_id is None:
#     raise ValueError(f"Row with value '{target_value}' not found in column '{column_name}'.")

# print(f"Column ID: {column_id}, Row ID: {row_id}")



# # Find the cell in the specified row and column
# target_row_number = 5  # Replace with the row number you are looking for
# target_column_id = column_id  # Replace with the column ID you are looking for

# target_cell = None
# for row in sheet.rows:
#     if row.row_number == target_row_number:
#         for cell in row.cells:
#             if cell.column_id == target_column_id:
#                 target_cell = cell
#                 break
#         break

# if target_cell is None:
#     raise ValueError(f"Cell not found in row {target_row_number} and column ID {target_column_id}.")

# print(f"Found cell in row {target_row_number} and column ID {target_column_id}: {target_cell.value}")

# for column in sheet.columns:
#     print(f"Column Name: {column.title}, Column ID: {column.id}")

# Iterate through each row in the sheet
current_status_col_id = 65371578257284
for row in sheet.rows:
    print(f"Processing Row ID: {row.row_number}")
    if row.row_number > sheet.total_row_count:
        break
    for cell in row.cells:
        if cell.column_id != current_status_col_id:
            continue
        print(f"Current Cell Value: {cell.value}")  # Print the cell's current value
        cell_update = smartsheet.models.Cell()
        cell_update.column_id = current_status_col_id
        # Define the new picklist value to add (must be a valid picklist option)
        new_picklist_value = f"{datetime.datetime.now().strftime('%m/%d/%Y')}: Accessed via API -MC"
        # Ensure the value is a list and append the new value if not present
        if isinstance(cell.value, list):
            updated_values = cell.value.copy()
            if new_picklist_value not in updated_values:
                updated_values.append(new_picklist_value)
        else:
            updated_values = [new_picklist_value]
        cell_update.value = updated_values
        print(f"Updated Cell Value: {cell_update.value}")  # Print the updated value
        updated_row = smartsheet.models.Row()
        updated_row.id = row.id
        updated_row.cells = [cell_update]
        rows_to_update.append(updated_row)
            


# Update rows in smartsheet
if rows_to_update:
    smartsheet_client.Sheets.update_rows(sheet_id, rows_to_update)
    
# print(f"Current Row and NCR Number: {ncr_number_cell}\n Last Updated: {last_updated_cell}")