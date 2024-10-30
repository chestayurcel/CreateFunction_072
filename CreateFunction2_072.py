# Fungsi Lambda untuk menghitung luas lingkaran dari jari-jari
luas_lingkaran = lambda jari2: 3.14 * (jari2 ** 2)

jari2 = 10 # Memasukkan nilai jari2 nya
luas = luas_lingkaran(jari2) # Menghitung luas lingkaran menggunakan fungsi Lambda
print(f"Luas lingkaran dengan jari-jari {jari2} adalah {luas}") # Menampilkan hasilnya