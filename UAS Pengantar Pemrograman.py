# =======================
# CLASS DATA
# =======================
class Student:
    def __init__(self, nama, nim, kelas, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas


# =======================
# CLASS PROCESS
# =======================
class StudentProcess:
    def validasi_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus berada antara 0 - 100")

    def hitung_nilai_akhir(self, student):
        return (0.3 * student.nilai_tugas +
                0.3 * student.nilai_uts +
                0.4 * student.nilai_uas)


# =======================
# CLASS VIEW
# =======================
class StudentView:
    def input_data(self):
        try:
            nama = input("Masukkan Nama  : ")
            nim = input("Masukkan Nim  : ")
            kelas = input("Masukkan Kelas : ")

            tugas = float(input("Masukkan Nilai Tugas : "))
            uts = float(input("Masukkan Nilai UTS   : "))
            uas = float(input("Masukkan Nilai UAS   : "))

            return nama, nim, kelas, tugas, uts, uas

        except ValueError:
            raise ValueError("Input nilai harus berupa angka!")

    def tampilkan_hasil(self, student, nilai_akhir):
        print("\n========== HASIL NILAI MAHASISWA ==========")
        print("------------------------------------------")
        print(f"Nama         : {student.nama}")
        print(f"Nim          : {student.nim}")
        print(f"Kelas        : {student.kelas}")
        print("------------------------------------------")
        print(f"Nilai Tugas : {student.nilai_tugas}")
        print(f"Nilai UTS   : {student.nilai_uts}")
        print(f"Nilai UAS   : {student.nilai_uas}")
        print("------------------------------------------")
        print(f"Nilai Akhir : {nilai_akhir:.2f}")
        print("------------------------------------------")


# =======================
# MAIN PROGRAM
# =======================
def main():
    view = StudentView()
    process = StudentProcess()

    try:
        nama, nim, kelas, tugas, uts, uas = view.input_data()

        process.validasi_nilai(tugas)
        process.validasi_nilai(uts)
        process.validasi_nilai(uas)

        student = Student(nama, nim, kelas, tugas, uts, uas)
        nilai_akhir = process.hitung_nilai_akhir(student)

        view.tampilkan_hasil(student, nilai_akhir)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()