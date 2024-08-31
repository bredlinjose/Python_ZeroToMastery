import openpyxl


def read_data_from_excel(file, sheet_name, row, column):
    workbook = openpyxl.open(file)
    sheet = workbook[sheet_name]
    sheet.cell(row, column).value