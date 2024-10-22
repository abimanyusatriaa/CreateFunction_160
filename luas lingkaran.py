import math #library untuk operasi mtk

#rumus luas lingkaran
luas_lingkaran = lambda r: math.pi * r*r
#lambda = mendefinisikan fungsi yang pendek tanpa harus menggunakan kata kunci def seperti pada fungsi biasa

#contoh penggunaan
jari_jari = 7
area = luas_lingkaran(jari_jari)
#area = digunakan untuk menyimpan hasil dari perhitungan luas lingkaran
print(f"luas lingkaran dengan jari_jari {jari_jari} adalah {area:.2f}") #menampilkan hasil 