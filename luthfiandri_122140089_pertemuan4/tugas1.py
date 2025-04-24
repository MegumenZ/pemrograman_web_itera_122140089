# Input user
berat_badan = float(input("Masukkan berat badan Anda (dalam kg): "))
tinggi_badan = float(input("Masukkan tinggi badan Anda (dalam meter): "))

# Perhitungan BMI
nilai_bmi_anda = berat_badan / (tinggi_badan ** 2)

# Menentukan kategori BMI
if nilai_bmi_anda < 18.5:
    kategori_bmi = "Berat badan kurang"
elif 18.5 <= nilai_bmi_anda < 25:
    kategori_bmi = "Berat badan normal"
elif 25 <= nilai_bmi_anda < 30:
    kategori_bmi = "Berat badan berlebih"
else:
    kategori_bmi = "Obesitas"

# Menampilkan hasil
print(f"\nBMI Anda adalah: {nilai_bmi_anda:.2f}")
print(f"Kategori: {kategori_bmi}")
