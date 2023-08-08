import openpyxl

def get_column_names(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]

    column_names = []
    for col in sheet.iter_cols(min_row=1, max_row=1, values_only=True):
        column_names.extend(col)

    workbook.close()
    return column_names

# Example usage
file_path = 'blank_cell.xlsx'
sheet_name = 'DATA'
columns = get_column_names(file_path, sheet_name)
print("Column names:", columns[5])
