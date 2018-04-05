from texttable import Texttable
import getpass


def menu():
    print("**********************************************")
    print("\n\t(--Pilihan--)")
    print("\t1 : Penilaian Mahasiswa")
    print("\t2 : Pembayaran Mahasiswa")

    pilih = input("\n\tSilahakan Pilih : ")
    if pilih == "1":
        nilai_mahasiswa()
    elif pilih == "2":
        pembayaran ()
    else :
        exit
    tanya()

def tanya():
    tanya = input("\nKembali ke Menu (Y/T) ? ")
    if tanya == "y" :
        menu()
    elif tanya == "t" :
        exit
    else:
        print("\n\tSalah input .. :b")


def nilai_mahasiswa():
    table = Texttable()
    jawab = "y"
    no = 0
    nama = []
    nim = []
    nilai_tugas = []
    nilai_uts = []
    nilai_uas = []
    while(jawab == "y"):
        nama.append(input ("Masukan Nama : "))
        nim.append(input ("Masukan NIM : "))
        nilai_tugas.append(input ("Nilai Tugas : "))
        nilai_uts.append(input ("Nilai UTS : "))
        nilai_uas.append(input ("Nilai UAS : "))
        jawab = input("Tambah Data (y/n)?")
        no += 1
    for i in range(no):
        tugas = int(nilai_tugas[i])
        uts = int(nilai_uts[i])
        uas = int(nilai_uas[i])
        akhir = (tugas + uts + uas)/3
        table.add_rows([['No','Nama','NIM','Nilai Tugas', 'Nilai UTS', 'Nilai UAS', 'Nilai Akhir'],
                        [i+1, nama[i],nim[i],nilai_tugas[i],nilai_uts[i],nilai_uas[i],akhir]])
    print (table.draw() )

def pembayaran():
    print("\n************************************")
    nama = input("\n\tMasukan nama : ")
    nim = input("\tMAsukan NIM : ")
    semester = input("\tMasukan Semester anda sekarang : ")
    print("\n\t---Pilihan Pembayaran---")
    print("\t1 * Pembayaran SPP")
    print("\t2 * Pembayaran UTS")
    print("\t3 * Pembayaran UAS")
    print("\t4 * Pembayaran SPP & UTS")
    print("\t5 * Pembayaran SPP & UAS")
    pilih = input("\n\tSilahkan Pilih :")
    if pilih == "1" :
        spp()
    elif pilih == "2" :
        uts()
    elif pilih == "3" :
         uas()
    elif pilih == "4" :
        spp_uts()
    elif pilih == "5" :
        spp_uas()
    else:
        exit
        tanya()

def spp() :
    bulan = int(input("\n\t Jumlah bulan yang di bayar = "))
    bulan = float(bulan)
    total = 350000 * bulan
    print("***************************************")
    print("\tTotal bayar spp Rp. 350.000 " , bulan ," = Rp. ",total)

def uas() :
    matkul = int(input("\n\t Jumlah mata kuliah = "))
    matkul = float(matkul)
    byr_uas = 50000*matkul
    print("***************************************")
    print("\tTotal bayar uas Rp. 50000*", matkul ," = Rp. ",byr_uas)

def uts() :
    matkul_uts = int(input("\n\t Jumlah mata kuliah = "))
    matkul_uts = float(matkul_uts)
    byr_uts = 25000*matkul_uts
    print("***************************************")
    print("\tTotal bayar uas Rp. 25000*",matkul_uts," = Rp. ",byr_uts)

def spp_uas() :
    bulan = int(input("\n\t Jumlah bulan yang di bayar = "))
    matkul = int(input("\n\t Jumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 350000 *bulan
    byr_uas = 50000*matkul
    total = total_spp + byr_uas + 5000
    print("\tTotal bayar spp Rp. 350000*",bulan," = Rp. ",total_spp)
    print("\tTotal bayar uas Rp. 50000*",matkul," = Rp. ",byr_uas)
    print("\tBiaya tambahan server Rp. 5000")
    print("***************************************")
    print("\tTotal yang harus di bayar : ",total )

def spp_uts() :
    bulan = int(input("\n\t Jumlah bulan yang di bayar = "))
    matkul = int(input("\n\t Jumlah mata kuliah = "))
    bulan = float(bulan)
    matkul = float(matkul)
    total_spp = 350000 *bulan
    byr_uts = 25000*matkul
    total = total_spp + byr_uts + 5000
    print("\tTotal bayar spp Rp. 350000*",bulan," = Rp. ",total_spp)
    print("\tTotal bayar uas Rp. 25000*",matkul," = Rp. ",byr_uts)
    print("\tBiaya tambahan server Rp. 5000")
    print("***************************************")
    print("\tTotal yang harus di bayar : ",total )

username = input("\nUsername : ")
password = getpass.getpass()
print("***************************************")

if username == "a" and password == "2":
    menu()

else:
    print ("Password lu salah mblo ..")
