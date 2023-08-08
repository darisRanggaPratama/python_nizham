from openpyxl import *

path = 'blank_cell.xlsx'
wb = load_workbook(path)
print(wb.sheetnames)
sheet = wb['DATA']

# Ambil cell
sheet['A1']
# print(sheet['A1'])

# Ambil nilai di cell
sheet['A1'].value
print(sheet['A1'].value)

val = sheet['B1']
val.value
print(val.value)

# Ambil baris, kolom & nilai dari cell
print(f'baris: {val.row} kolom: {val.column} nilai:  {val.value} huruf-kolom: {utils.get_column_letter(val.column)}')