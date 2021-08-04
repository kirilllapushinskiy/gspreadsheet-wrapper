class Spreadsheet:
    def __init__(self, spreadsheet_id, spreadsheets):
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheets = spreadsheets

    def get_values(self, s_range='A:Z', value_render='FORMATTED_VALUE',
                   date_render='FORMATTED_STRING', dimension='ROWS'):
        request = self.spreadsheets.values().get(
            spreadsheetId=self.spreadsheet_id,
            range=s_range,
            valueRenderOption=value_render,
            dateTimeRenderOption=date_render,
            majorDimension=dimension
        )
        return request.execute()['values']

    def set_values(self, s_range, values,
                   value_input_option='FORMATTED_STRING', dimension='ROWS'):
        request = self.spreadsheets.values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": f"{value_input_option}",
                "data":
                    [
                        {
                            "range": f"{s_range}",
                            "majorDimension": f"{dimension}",
                            "values": [values]
                        }
                    ]
            }
        )
        return request.execute()
