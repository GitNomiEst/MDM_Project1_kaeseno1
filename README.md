App starten: Flask run
App starts on: http://localhost:5000/ 
Update requirements: pip freeze > requirements.txt

Upload auf Blob:
# cd model
# python save.py -c '***AZURE_STORAGE_CONNECTION_STRING***'
# https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli
# Erlaubnis auf eigenes Konto geben :-)
