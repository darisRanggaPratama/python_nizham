import openpyxl

def get_float_values(file_path, sheet_name):
    # Load the Excel workbook
    wb = openpyxl.load_workbook(file_path)

    # Select the sheet you want to read
    sheet = wb[sheet_name]

    # Read float values from the cells
    float_values = []
    for row in sheet.iter_rows():
        for cell in row:
            if isinstance(cell.value, (int)):
                float_values.append(cell.value)

    # Close the workbook after you're done reading
    wb.close()

    return float_values

# Example usage
file_path = 'blank_cell.xlsx'
sheet_name = 'empty'
float_values = get_float_values(file_path, sheet_name)
print(float_values)


# This code is work