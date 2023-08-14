import openpyxl

# Isi Nama File
path = input('\nFIND WORD\nFile Name: ')

# Isi yang dicari
word = input('Word: ')

# Buka workbook Excel
workbook = openpyxl.load_workbook(path)  # Ganti 'nama_file.xlsx' dengan nama file Anda
sheet_names = workbook.sheetnames

# Kata yang ingin dicari dalam sel
kata_tertentu = word # word  # Ganti 'contoh_kata' dengan kata yang ingin Anda cari

# Fungsi untuk mencari nilai dalam worksheet
def cari_nilai(worksheet, kata):
    for row in worksheet.iter_rows():
        for cell in row:
            if isinstance(cell.value, str) and kata in cell.value:
                return cell

# Cari nilai dalam setiap worksheet
print(f'\nNo ; Sheet ; Cell ; Value ;')
print('-' * 40)
x = 0
for sheet_name in sheet_names:
    x += 1
    sheet = workbook[sheet_name]
    cell_with_value = cari_nilai(sheet, kata_tertentu)
    if cell_with_value:
        print(f'{x} ; {sheet_name} ; {cell_with_value.coordinate} ; {cell_with_value.value} ;')



# Tutup workbook
workbook.close()
