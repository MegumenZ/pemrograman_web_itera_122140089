# Cara 1: import seluruh modul (pake math_operations.nama_fungsi biar berjalan)
import math_operations

# Cara 2: import langsung fungsi tertentu (cuma pake beberapa fungsi dan biar langsung pake nama fungsinya)
from math_operations import celsius_ke_fahrenheit, keliling_lingkaran


print("=== PERHITUNGAN GEOMETRI ===")

# Persegi
sisi = float(input("Masukkan sisi persegi: "))
print(f"Luas persegi = {math_operations.luas_persegi(sisi)}")
print(f"Keliling persegi = {math_operations.keliling_persegi(sisi)}\n")

# Persegi panjang
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
print(f"Luas persegi panjang = {math_operations.luas_persegi_panjang(panjang, lebar)}")
print(f"Keliling persegi panjang = {math_operations.keliling_persegi_panjang(panjang, lebar)}\n")

# Lingkaran
jari = float(input("Masukkan jari-jari lingkaran: "))
print(f"Luas lingkaran = {math_operations.luas_lingkaran(jari):.2f}")
print(f"Keliling lingkaran = {keliling_lingkaran(jari):.2f}\n") # pake cara kedua

print("=== KONVERSI SUHU ===")
cel = float(input("Masukkan suhu dalam Celsius: "))
print(f"{cel}°C ke Fahrenheit = {celsius_ke_fahrenheit(cel):.2f}°F") # pake cara kedua
print(f"{cel}°C ke Kelvin = {math_operations.celsius_ke_kelvin(cel):.2f}K\n")

print("=== KONSTANTA ===")
print(f"Nilai PI = {math_operations.PI}")
