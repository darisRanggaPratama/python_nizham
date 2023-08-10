from openpyxl import *

wbook = load_workbook('blank_cell.xlsx')
wsheet = wbook.active
wsheet.title = "testing"
wbook.save('example.xlsx')
