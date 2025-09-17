from O365 import Account

# Replace with your Azure app credentials
client_id = 'your_client_id'
client_secret = 'your_client_secret'
credentials = (client_id, client_secret)

# Authenticate (first run will prompt for login and save token)
account = Account(credentials)
if not account.is_authenticated:
    account.authenticate(scopes=['basic', 'sharepoint_all'])

# Connect to SharePoint site
sharepoint = account.sharepoint()
site = sharepoint.get_site('yourcompany.sharepoint.com', site_name='yoursite')

# Get the document library (folder)
library = site.get_default_document_library()
folder = library.get_folder('Shared Documents/YourFolder')  # Change to your folder path

# List files in the folder
for item in folder.get_items():
    print(item.name)

# from shareplum import Site
# from requests_ntlm import HttpNtlmAuth

# # Replace with your SharePoint site URL, username, and password
# site_url = 'https://woojinisamerica.sharepoint.com/:f:/r/sites/PQWTeam/Quality%20Department/NCR%202025?csf=1&web=1&e=80dMS3ite'
# username = "MCho@woojinisa.com"
# password = "Rat@WOOJIN6988"
# folder_name = 'https://woojinisamerica.sharepoint.com/sites/PQWTeam/Quality%20Department/NCR%202025' # Replace with your folder path

# # Authenticate with NTLM
# auth = HttpNtlmAuth(username, password)

# # Connect to the SharePoint site
# site = Site(site_url, auth=auth)

# # Access the desired folder and list files
# folder = site.Folder(folder_name)
# files = folder.files()

# print(f"Files in '{folder_name}':")
# for file in files:
#     print(file['Name'])