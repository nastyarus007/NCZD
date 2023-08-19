import gspread
from gspread.utils import ExportFormat

gc = gspread.service_account(filename='linen-fuze-396409-c83f7e831fab.json')
files = ["Панели", "Example spreadsheet"]
for file in files:
    sh = gc.open(file)
    export_file = sh.export(format=ExportFormat.EXCEL)
    with open('{0}.xlsx'.format(file), 'wb') as f:
        f.write(export_file)
