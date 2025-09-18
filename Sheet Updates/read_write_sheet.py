import datetime

# The API identifies columns by Id, but it's more convenient to refer to column names. Store a map here
column_map = {}

def initialize_column_map(sheet):    
    for column in sheet.columns:
        if column.id is None:
            print(f"Warning: Column '{column.title}' not found in the sheet. Skipping...")
            continue
        column_map[column.title] = column.id
        print(f"Column ID for '{column.title}': {column.id}")
    return column_map

def get_cell_by_column_id(row, column_id):
    # Retrieves a cell from a row by column ID.
    return row.get_column(column_id)

def build_rows_to_update(sheet, column_map, smartsheet_client, updates_column_name):
    # need to add check_column_name for additional conditions for the code
    updates_col_id = column_map[updates_column_name]  # Replace with your actual "Updates" column name if different
    rows_to_update = []
    for row in sheet.rows:
        # Get the current value in the Updates cell
        updates_cell = next((cell for cell in row.cells if cell.column_id == updates_col_id), None)
        updates_value = getattr(updates_cell, 'value', None) if updates_cell else None

        # Prepare the new update note
        update_note = f"{datetime.datetime.now().strftime('%m/%d/%Y')}: Accessed via API -MC"

        # Combine with existing value
        if updates_value is None:
            combined_updates = update_note
        else:
            combined_updates = f"{updates_value}\n{update_note}"

        # Create a new Cell object for the update
        cell_to_update = smartsheet_client.models.Cell()
        cell_to_update.column_id = updates_col_id
        cell_to_update.value = combined_updates

        # Create a Row object with the updated cell
        row_to_update = smartsheet_client.models.Row()
        row_to_update.id = row.id
        row_to_update.cells = [cell_to_update]

        rows_to_update.append(row_to_update)
    return rows_to_update

def evaluate_row_and_build_updates(source_row, status_column_id, smartsheet_client):
    """
    Evaluates a Smartsheet row and builds an update if needed.
    Looks for rows with 'Current Status' == 'Complete' and updates the 'Updates' column.
    Returns a new Row with updated cell values, else None to leave unchanged.
    """
    # Get the 'Current Status' cell value
    current_status_cell = get_cell_by_column_id(source_row, column_map[status_column_id])
    status_value = getattr(current_status_cell, 'display_value', None)

    # print("1. Raw value:", getattr(current_status_cell, 'value', None))
    # print("2. Display value:", getattr(current_status_cell, 'display_value', None))
    # print(f"Current Status Cell: {current_status_cell}")
    # print(f"Status Value: {status_value} (type: {type(status_value)})")

    if status_value is None:
        print("Status value is None (cell may be empty or missing).")
    else:
        print(f"Status value is present: {status_value}")

    if status_value == "Complete":
        remaining_cell = get_cell_by_column_id(source_row, column_map.get("Column11"))
        if remaining_cell != 0:
            print("Needs to update row #" + str(source_row.id) + ".")

            # Create a new Cell object for Column11
            new_cell = smartsheet_client.models.Cell()
            new_cell.column_id = column_map["Column11"]

            # Get the 'Updates' cell
            updates_cell = get_cell_by_column_id(source_row, new_cell.column_id)
            updates_value = getattr(updates_cell, 'value', None) if updates_cell else None

            # Prepare the new update string
            update_note = f"{datetime.datetime.now().strftime('%m/%d/%Y')}: Accessed via API -MC"
            
            # Combine the existing updates_value and the new update_note into a single string (with line breaks)
            if updates_value is None:
                combined_updates = update_note
            else:
                combined_updates = f"{updates_value}\n{update_note}"

            # Create a new Cell object for the update
            cell_to_update = smartsheet_client.models.Cell()
            cell_to_update.column_id = new_cell.column_id  # Column11
            cell_to_update.value = combined_updates

            # Create a Row object with the updated cell
            row_to_update = smartsheet_client.models.Row()
            row_to_update.id = source_row.id
            row_to_update.cells = [cell_to_update]

            return row_to_update
        
        #return None
            # # Update the row in Smartsheet
            # response = smartsheet_client.Sheets.update_rows(SHEET_ID, [row_to_update])
            # print("Update response:", response)
            
            # # Get the 'Updates' cell
            # updates_cell = get_cell_by_column_id(source_row, updates_column_id)
            # updates_value = getattr(updates_cell, 'value', None)

            # # Prepare the new update string
            # update_note = f"{datetime.datetime.now().strftime('%m/%d/%Y')}: Accessed via API -MC"

            # # If the cell is empty, start a new list; if it's a list, append; if it's a string, convert to list
            # if updates_value is None:
            #     new_updates_value = [update_note]
            # elif isinstance(updates_value, list):
            #     new_updates_value = updates_value + [update_note]
            # else:
            #     new_updates_value = [str(updates_value), update_note]

            # # Build new cell value
            # new_cell = smartsheet_client.models.Cell()
            # new_cell.column_id = updates_column_id
            # new_cell.value = new_updates_value

            # # Build the row to update
            # new_row = smartsheet_client.models.Row()
            # new_row.id = source_row.id
            # new_row.cells.append(new_cell)

        #         return new_row
    #     return None
