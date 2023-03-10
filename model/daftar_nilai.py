Data_Mahasiswa = {}


def tambah_Data_Mahasiswa(nama,nim,tugas,uts,uas):
    akhir = round((float(tugas) * 0.3) + (float(uts) * 0.35) + (float(uas) * 0.35), 2)
    Data_Mahasiswa[nama] = nama,nim,tugas,uts,uas,akhir


def ubah_Data_Mahaiswa(nama):
    if nama in Data_Mahasiswa.keys():
        del Data_Mahasiswa[nama]
        print("\n===Masukan Perubahan Data===")
        from view.input_nilai import inputan
        inputan()
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        print("    (T)Tambah       (U)ubah      (H)Hapus     (C)Cari      (L)Lihat     (K)Keluar   ")


def cari(nama):
    if nama in Data_Mahasiswa.keys():
        print("\n=====================================================================")
        print("|      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
        print("|=================|==================|=======|=======|===============|")
        print("| {0:15} | {1:16} | {2:5} | {3:5} | {4:5} | {5:5} |".format(nama, Data_Mahasiswa[nama][1], Data_Mahasiswa[nama][2],Data_Mahasiswa[nama][3],Data_Mahasiswa[nama][4], Data_Mahasiswa[nama][5]))
        print("======================================================================")
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")


def hapus(nama):
    if nama in Data_Mahasiswa.keys():
        del Data_Mahasiswa[nama]
        return True
    else:
        print(" ________________________")
        print("| Data {} tidak ditemukan |".format(nama))
        print(" ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        return False
