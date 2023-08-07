import openpyxl

def check_duplicate_strings_in_column(file_path, sheet_name, column_index):
    # Load the Excel workbook
    workbook = openpyxl.load_workbook(file_path)

    # Select the specific sheet
    sheet = workbook[sheet_name]

    # Get the column to check for duplicates
    column_values = [cell.value for cell in sheet[column_index]]

    # Create a set to store unique values and a list to store duplicate values
    unique_values = set()
    duplicate_values = []

    # Iterate through the column values
    for value in column_values:
        if value in unique_values:
            duplicate_values.append(value)            
        else:
            unique_values.add(value)

    # Return the list of duplicate values
    return duplicate_values

if __name__ == "__main__":
    file_path = "blank_cell.xlsx"  # Update with the correct file path
    sheet_name = "empty"  # Replace with the name of the sheet containing the data
    column_index = "G"  # Replace with the column index (e.g., "A" for the first column)

    duplicates = check_duplicate_strings_in_column(file_path, sheet_name, column_index)
    if duplicates:
        print("Duplicate values found in column:")
        for value in duplicates:
            print(value)
    else:
        print("No duplicate values found in column.")
        

# This code is works
