# Data mahasiswa
data_mahasiswa = [
    {"nama": "Luthfiandri", "nim": "122140089", "nilai_uts": 85, "nilai_uas": 85, "nilai_tugas": 91},
    {"nama": "Florian Wirtz", "nim": "122140010", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 68},
    {"nama": "Thibaut Courtois", "nim": "122140080", "nilai_uts": 88, "nilai_uas": 90, "nilai_tugas": 85},
    {"nama": "Declan Rice", "nim": "122140107", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
    {"nama": "Viktor Gyokeres", "nim": "122140066", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50},
]

# Fungsi menghitung nilai akhir dan grade
def hitung_nilai_akhir(mahasiswa):
    nilai_akhir = (
        0.3 * mahasiswa["nilai_uts"]
        + 0.4 * mahasiswa["nilai_uas"]
        + 0.3 * mahasiswa["nilai_tugas"]
    )
    if nilai_akhir >= 80:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    elif nilai_akhir >= 50:
        grade = "D"
    else:
        grade = "E"
    return nilai_akhir, grade

# Menambahkan nilai akhir dan grade ke data
for mhs in data_mahasiswa:
    nilai_akhir, grade = hitung_nilai_akhir(mhs)
    mhs["nilai_akhir"] = round(nilai_akhir, 2)
    mhs["grade"] = grade

# Menampilkan data dalam bentuk tabel
print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<12} {:<6}".format(
    "Nama", "NIM", "UTS", "UAS", "Tugas", "Nilai Akhir", "Grade"
))
print("-" * 73)
for mhs in data_mahasiswa:
    print("{:<15} {:<10} {:<10} {:<10} {:<10} {:<12} {:<6}".format(
        mhs["nama"], mhs["nim"], mhs["nilai_uts"], mhs["nilai_uas"],
        mhs["nilai_tugas"], mhs["nilai_akhir"], mhs["grade"]
    ))

# Mencari mahasiswa dengan nilai tertinggi dan terendah
mahasiswa_tertinggi = max(data_mahasiswa, key=lambda x: x["nilai_akhir"])
mahasiswa_terendah = min(data_mahasiswa, key=lambda x: x["nilai_akhir"])

print("\nMahasiswa dengan nilai tertinggi:")
print(f"{mahasiswa_tertinggi['nama']} ({mahasiswa_tertinggi['nim']}) - {mahasiswa_tertinggi['nilai_akhir']} ({mahasiswa_tertinggi['grade']})")

print("Mahasiswa dengan nilai terendah:")
print(f"{mahasiswa_terendah['nama']} ({mahasiswa_terendah['nim']}) - {mahasiswa_terendah['nilai_akhir']} ({mahasiswa_terendah['grade']})")
