# List Mahasiswa
students = [
    {"nama": "Ade", "nim": "12214001", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 80},
    {"nama": "Budi", "nim": "12214002", "nilai_uts": 75, "nilai_uas": 70, "nilai_tugas": 65},
    {"nama": "Cantika", "nim": "12214003", "nilai_uts": 60, "nilai_uas": 55, "nilai_tugas": 70},
    {"nama": "Dian", "nim": "12214004", "nilai_uts": 40, "nilai_uas": 50, "nilai_tugas": 45},
    {"nama": "Eva", "nim": "12214005", "nilai_uts": 95, "nilai_uas": 85, "nilai_tugas": 90},
]

# Fungsi untuk kalkulasi nilai akhir
def calculate_grade(student):
    nilai_akhir = (0.3 * student["nilai_uts"] +
                   0.4 * student["nilai_uas"] +
                   0.3 * student["nilai_tugas"])
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

# Penambahan nilai akhir ke mahasiswa
for student in students:
    nilai_akhir, grade = calculate_grade(student)
    student["nilai_akhir"] = nilai_akhir
    student["grade"] = grade

# Mencari mahasiswa dengan nilai akhir tertinggi dan terendah
highest_student = max(students, key=lambda x: x["nilai_akhir"])
lowest_student = min(students, key=lambda x: x["nilai_akhir"])

# Menampilkan data dalam format tabel
print(f"{'Nama':<10} {'NIM':<10} {'UTS':<5} {'UAS':<5} {'Tugas':<7} {'Akhir':<7} {'Grade':<5}")
print("-" * 50)
for student in students:
    print(f"{student['nama']:<10} {student['nim']:<10} {student['nilai_uts']:<5} {student['nilai_uas']:<5} {student['nilai_tugas']:<7} {student['nilai_akhir']:<7.2f} {student['grade']:<5}")

# Menampilkan data mahasiswa nilai tertinggi dan terendah
print("\nMahasiswa dengan nilai tertinggi:")
print(f"Nama: {highest_student['nama']}, NIM: {highest_student['nim']}, Nilai Akhir: {highest_student['nilai_akhir']:.2f}, Grade: {highest_student['grade']}")

print("\nMahasiswa dengan nilai terendah:")
print(f"Nama: {lowest_student['nama']}, NIM: {lowest_student['nim']}, Nilai Akhir: {lowest_student['nilai_akhir']:.2f}, Grade: {lowest_student['grade']}")