# Create List
number = [1, 2, 3, 4, 5]

print("\nRead List Element: while")
i = 0
while i < len(number):
	print(number[i])
	i += 1

print("\nRead List Element: for")
for angka in number:	
	print(angka)


print("\nEdit element:")
number[2] = 100
for angka in number:
	print(angka)


print("\nMultiple List")
data = [
	["Car", "Color", "Price"],
	["Toyota", "Silver", 500],
	["Honda", "Black", 340],
	["Suzuki", "Blue", 410]
	]
for item in data:
	print(item)


print("\nMencetak semua elemen\ndari Multiple List data")
for row in data:
    for item in row:
        print(item, end=" ")
	# Memberikan baris baru setelah setiap baris data
    print()  


print("\nPerbedaan Append(), Insert(), extend()\n")
def show_list(list):
	x = -1
	for item in list:
		x += 1
		print(x, f' ', item)


# Contoh list awal
fruits = ['apple', 'banana', 'orange']
show_list(fruits)

# Menambahkan elemen baru ke akhir list
print("\n1. Append: ")
fruits.append('grape')

# Hasil setelah penambahan elemen
show_list(fruits)

# Menyisipkan elemen baru "grape" pada indeks 1
print("\n2. Insert: ")
fruits.insert(2, 'strawberry')

# Hasil setelah menyisipkan elemen
show_list(fruits)

print("\nDuplikat isi List")

fruit_copy = fruits.copy()
show_list(fruit_copy)

# List baru yang akan ditambahkan ke akhir list awal
print("\n3. Extend: ")
new_fruits = ['melon', 'mango']

# Menambahkan elemen-elemen dari list baru ke akhir list awal
fruit_copy.extend(new_fruits)

# Hasil setelah penambahan elemen
print("List Awal: ")
show_list(fruits)
print("Extend: ")
show_list(new_fruits)
print("List Akhir: ")
show_list(fruit_copy)

