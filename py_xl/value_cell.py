import openpyxl
wb=openpyxl.load_workbook('blank_cell.xlsx')
s = wb.get_sheet_by_name('empty')     
for j in s['A1':'F46']:
            for cel in j:
                    print(cel.coordinate,cel.value)
            print('-------------')


# This code is work