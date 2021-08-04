class Spreadsheet:
    def __init__(self, spreadsheet_id, spreadsheets):
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheets = spreadsheets

    def get_values(self, ranges='A:Z', value_render='FORMATTED_VALUE',
                   date_render='FORMATTED_STRING', dimension='ROWS'):
        request = self.spreadsheets.values().get(
            spreadsheetId=self.spreadsheet_id,
            range=ranges,
            valueRenderOption=value_render,
            dateTimeRenderOption=date_render,
            majorDimension=dimension
        )
        return request.execute()['values']

    def set_values(self, ranges, values,
                   value_input_option='FORMATTED_STRING', dimension='ROWS'):
        request = self.spreadsheets.values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": f"{value_input_option}",
                "data":
                    [
                        {
                            "range": f"{ranges}",
                            "majorDimension": f"{dimension}",
                            "values": [values]
                        }
                    ]
            }
        )
        return request.execute()
