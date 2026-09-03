# print("="*50)

# nama_siswa = input("Masukan nama anda : ")

# nilai_tugas = float(input("Masukan nilai tugas : "))

# nilai_uts = float(input("Masukan nilai uts : "))

# nilai_uas =  float(input("Masukan nilai uas : "))

# print("="*50)
# nilai = nilai_tugas, nilai_uas, nilai_uts

# if nilai is None:
#     print("Masukan nilai dengan benar!")



def inputNilai(jenis_nilai):

    while True:

        if jenis_nilai == "nilai_tugas":
            nilai_tugas = float(input("Masukan nilai tugas : "))
            return nilai_tugas

        elif jenis_nilai == "nilai_uts":
            nilai_uts = float(input("Masukan nilai uts : "))
            return nilai_uts

        elif jenis_nilai == "nilai_uas":
             nilai_uas = float(input("Masukan nilai uas : "))
             return nilai_uas

        try:
            if isinstance(jenis_nilai,(float)):
                return "Nilai bukan angka!"
        except: 
            return "Nilai Angka!"


nama_siswa = input("Masukan nama siswa : ")

nilai_tugas = inputNilai("nilai_tugas")
nilai_uts = inputNilai("nilai_uts")
nilai_uas = inputNilai("nilai_uas")

nilai_akhir = ((0.3 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas))

def kalkulasiNilai(nama, nilai_akhir):


    print("Mengkalkulasi Nilai")

    grade = ""

    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 75: 
        grade = "B"
    elif nilai_akhir >= 65: 
        grade = "C"
    elif nilai_akhir >= 50: 
        grade = "D"
    elif nilai_akhir <= 50: 
        grade = "E"
    else:
        return "Data nilai tidak valid!"

    status = ""

    if nilai_akhir >= 65:
         status = "Anda lulus!"
    else:
        status = "Anda Tidak lulus"

    print()
    print(f"Nama           : {nama}")
    print(f"Nilai Akhir    : {nilai_akhir}")
    print(f"Grade          : {grade}")
    print(f"Status         : {status}")

kalkulasiNilai(nama_siswa, nilai_akhir)



