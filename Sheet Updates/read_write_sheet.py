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