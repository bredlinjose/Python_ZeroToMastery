import os

import openpyxl


wb = openpyxl.load_workbook(os.path.join(os.path.dirname(__file__), "sampledata.xlsx"))
ws = wb["Dummy"]

for row in ws.iter_rows(min_row=2, max_row=4, values_only=True):
    print(row)
