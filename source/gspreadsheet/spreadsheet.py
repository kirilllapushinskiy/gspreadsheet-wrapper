from gservice import GService


class Spreadsheet:
    def __init__(self, g_service: GService):
        self.spreadsheets = g_service.spreadsheets()
