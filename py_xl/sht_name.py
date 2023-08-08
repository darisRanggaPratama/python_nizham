import openpyxl

def get_sheet_names(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet_names = workbook.sheetnames
    workbook.close()
    return sheet_names

# Example usage
file_path = 'blank_cell.xlsx'
sheets = get_sheet_names(file_path)
print("Sheet names:", sheets[1])
