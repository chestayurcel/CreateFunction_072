# Fungsi untuk mengonversi suhu antara Celsius dan Fahrenheit
def konversi_suhu(nilai, satuan):
    if satuan == 'C':
        fahrenheit = (nilai * 9) / 5 + 32 # Rumus konversi Celsius ke Fahrenheit
        return fahrenheit
    elif satuan == 'F':
        celsius = (nilai - 32) * 5 / 9 # Rumus konversi Fahrenheit ke Celsius
        return celsius
    else:
        return "satuan tidak valid. Silakan gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit."
    # Jika satuan yang dimasukkan tidak valid, berikan pesan kesalahan

# Masukkan nilai suhu Celsius
nilai_c = 30
# Memanggil fungsi untuk mengonversi dari Celsius ke Fahrenheit
c_ke_f = konversi_suhu(nilai_c, 'C')
print(f"{nilai_c}°C Sama dengan {c_ke_f}°F")

# Masukkan nilai suhu Fahrenheit
nilai_f = 86
# Memanggil fungsi untuk mengonversi dari Fahrenheit ke Celsius
f_ke_c = konversi_suhu(nilai_f, 'F')
print(f"{nilai_f}°F Sama dengan {f_ke_c}°C")
