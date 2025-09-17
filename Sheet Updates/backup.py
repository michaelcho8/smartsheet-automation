
import csv
import smartsheet
import os
from datetime import datetime

def backup_sheet_to_csv(sheet, backup_dir="backups"):
    # Ensure backup directory exists
    os.makedirs(backup_dir, exist_ok=True)
    # Create a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{backup_dir}/backup_{sheet.name}_{timestamp}.csv"
    # Backup the given Smartsheet sheet to a CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header
        header = [col.title for col in sheet.columns]
        writer.writerow(header)
        # Write rows
        for row in sheet.rows:
            writer.writerow([cell.value for cell in row.cells])
    print(f"Backup of sheet '{sheet.name}' completed to file '{filename}'")
    return filename

