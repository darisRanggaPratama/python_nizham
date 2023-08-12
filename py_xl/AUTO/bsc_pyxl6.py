from openpyxl import *

# Isi Nama File
path = 'blank_cell.xlsx' # input('Type\nFile Name: ')
# Akses file excel
wbook = load_workbook(path)
# Akses sheet tertentu
sh_data = wbook['DATA']
# Akses kolom tertentu
range_col = list(sh_data.columns)[1]
# print(range_col)

print('\nCell | Value')
# Baca nilai di kolom
for cell in range_col:
    if cell.value is None:
        print(f'  {cell.coordinate}   {cell.value}')


# Akses sheet active
# sheet = wbook.active