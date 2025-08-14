# Smartsheet Automation

## 1. File Structure

```
smartsheet-automation/
├── LICENSE
├── README.md
├── Downloaded Excel Files/
│   └── download.xlsx
├── List sheet Test/
│   ├── authorization.py
│   ├── config.py
│   ├── JSON_File/
│   ├── main.py
│   ├── output.xlsx
│   └── __pycache__/
│       └── config.cpython-310.pyc
```

## 2. Goals of the Project

- Automate interactions with Smartsheet for reporting, notifications, and data management.
- Streamline the process of monitoring sheet updates and sending alerts.
- Enable easy export and manipulation of Smartsheet data.

## 3. What It Currently Can Do

- Download Smartsheet sheets as Excel files.
- Check each row in a sheet for the "Last Updated" column and identify rows older than two weeks.
- Highlight the "NCR Number" cell for outdated rows.
- Send selected rows as emails to specified recipients using the Smartsheet API.

## 4. Features in Development

- Customizable recipient lists and notification templates.
- Automated updates to Smartsheet cells based on business logic.
- Integration with other reporting tools and dashboards.
- Enhanced error handling and logging.
- User interface for configuration and monitoring.