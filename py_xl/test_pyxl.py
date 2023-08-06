from openpyxl import Workbook
# load workbook
from openpyxl import load_workbook


# workbook = wb
wb = Workbook()

# sheet = sht
sht = wb.active 

sht['A1'] = "Kolom 1"
sht['B1'] = "Kolom 2"
sht['C1'] = "Kolom 3"
sht['A2'] = "Test 1"
sht['B2'] = "Test 2"
sht['C2'] = "Test 3"

wb.save(filename="test.xls")

nilai1 = sht['A1']
print(nilai1.value)