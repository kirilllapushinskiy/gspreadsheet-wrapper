from google.oauth2 import service_account
from googleapiclient import discovery


class GService:
    def __init__(self, service_account_file, scopes):
        self.credentials = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=scopes
        )

        self.service = discovery.build('sheets', 'v4', credentials=self.credentials)

    def spreadsheets(self):
        return self.service.spreadsheets()
