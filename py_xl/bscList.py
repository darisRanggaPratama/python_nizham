# 1: Buat sebuah List berisi angka ganjil antara angka 1 hingga 31 menggunakan Python Generator Expressions.
ganjil = (x for x in range(1, 32) if x % 2 != 0)

# 2: Tampilkan semua isi List di atas.
ls_ganjil = list(ganjil)
y = 0
for x in ls_ganjil:
	y += 1	
	print(y, f' ', x)


# 3: Tampilkan semua isi List di atas yang habis dibagi 5.
ganjil_5 = [x for x in ls_ganjil if x % 5 == 0 ]
ls_ganjil_5 = list(ganjil_5)
print("Elemen habis dibagi 5", ganjil_5)

# 4: Tampilkan elemen ke 6
isi_6 = next(x for idx, x in enumerate(ls_ganjil) if idx == 5)
print("index ke 6: ", isi_6)

# 5: Ubah elemen ke 6
ls_ganjil[5] = 10
print("ubah index ke 6: ", ls_ganjil[5])

y = 0
for x in ls_ganjil:
	y += 1	
	print(y, f' ', x)


# 6: Hapus index ke 7
hapus_idx7 = 6
if hapus_idx7 < len(ls_ganjil):
	del ls_ganjil[hapus_idx7]
	print("hapus index 7: ", hapus_idx7)

y = 0
for x in ls_ganjil:
	y += 1	
	print(y, f' ', x)


# 7: Mengurutkan Descending
ls_ganjil.sort(reverse=True)
print("Sort: Descending")
y = 0
for x in ls_ganjil:
	y += 1	
	print(y, f' ', x)