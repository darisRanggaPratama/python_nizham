import openpyxl

def check_empty_cells(file_path, sheet_name):
    # Membuka file Excel
    wb = openpyxl.load_workbook(file_path)

    # Memuat sheet yang sesuai
    sheet = wb[sheet_name]

    # Mencari sel kosong dan mencetak informasinya
    for row in sheet.iter_rows():
        for cell in row:
            if cell.value is None:
                print(f"Cell kosong ditemukan di {cell.coordinate}")

    # Menutup file Excel setelah selesai
    wb.close()

# Contoh penggunaan
file_path = 'blank_cell.xlsx'
sheet_name = 'empty'
check_empty_cells(file_path, sheet_name)

# This code is work
