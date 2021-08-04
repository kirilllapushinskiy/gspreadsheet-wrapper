from .gservice import GService


class Spreadsheet:
    def __init__(self, g_service: GService, spreadsheet_id):
        self.spreadsheets = g_service.spreadsheets()
        self.spreadsheet_id = spreadsheet_id

    def get_table_values(self, address='A:Z', date_render='SERIAL_NUMBER', dimension='ROWS'):
        request = self.spreadsheets.values().get(
            spreadsheetId=self.spreadsheet_id,
            range=address,
            dateTimeRenderOption=date_render,
            majorDimension=dimension
        )
        return request.execute()['values']
