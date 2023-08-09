from openpyxl import *

wbook = load_workbook('blank_cell.xlsx')
sh_data = wbook['DATA']
#RANGE
range = tuple(sh_data['A1':'F46'])
print(tuple(sh_data['A1':'B5']))
print("\nCELL | VALUE\n")
for row in range:
    for cell in row:
        print(f'  {cell.coordinate}   {cell.value}')
    print('---END OF ROW---\n')
