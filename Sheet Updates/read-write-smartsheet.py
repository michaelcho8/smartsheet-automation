import datetime

# The API identifies columns by Id, but it's more convenient to refer to column names. Store a map here
column_map = {}

def get_cell_by_column_title(row, column_title):
    # Retrieves a cell from a row by column title.
    column_id = column_map[column_title]
    return row.get_column(column_id)

def evaluate_row_and_build_updates(source_row, column_id, get_cell_by_column_title, column_map, smartsheet_client):
    """
    Evaluates a Smartsheet row and builds an update if needed.
    Looks for rows with 'Current Status' == 'Complete' and updates the 'Updates' column.
    Returns a new Row with updated cell values, else None to leave unchanged.
    """
    current_status_cell = get_cell_by_column_title(source_row, column_id)
    status_value = current_status_cell.display_value
    print(f"Status Value: {status_value}")
    if status_value is column_id:
        updates_cell = get_cell_by_column_title(source_row, "Updates")
        if updates_cell.display_value is not None:  # Skip if already 0
            print("Need to update row #" + str(source_row.row_number))

            # Build new cell value
            new_cell = smartsheet_client.models.Cell()
            new_cell.column_id = column_map["Updates"]
            new_cell.value = current_status_cell.value + [f"{datetime.datetime.now().strftime('%m/%d/%Y')}: Accessed via API -MC"]
            print(new_cell.value)

            # Build the row to update
            new_row = smartsheet_client.models.Row()
            new_row.id = source_row.id
            new_row.cells.append(new_cell)

            return new_row
    return None
