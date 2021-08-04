from .spreadsheet import Spreadsheet
from .gservice import GService


class GSpreadsheets:
    def __init__(self, g_service: GService):
        self.spreadsheets = g_service.spreadsheets()

    def get_spreadsheet(self, spreadsheet_id):
        return Spreadsheet(spreadsheet_id, self.spreadsheets)