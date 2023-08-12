from openpyxl import *

wbook = Workbook()
wsheet = wbook['Sheet']
wsheet['F2'] = 'Yuzi Itadori Sukuna'
wsheet['F2'].value
print('isi cell', wsheet['F2'].value)