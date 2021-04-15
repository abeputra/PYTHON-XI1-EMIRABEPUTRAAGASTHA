class siswa:
    '''Dasar kelas untuk semua siswa'''
    jumlah_siswa = 0

    def __init__(self, nama, kelas, absen, alamat):
        self.nama = nama
        self.kelas = kelas
        self.absen = absen
        self.alamat = alamat
        siswa.jumlah_siswa += 1
    
    def tampilkan_jumlah(self):
        print("Total siswa : ", siswa.jumlah_siswa)
    
    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Absen : ", self.absen)
        print("Alamat : ", self.alamat)

#Membuat objek pertama dari kelas siswa
siswa1 = siswa("Muhammad Dary Arkan", "XI MIA 4", 19, "Bantul")
#Membuat objek kedua dari kelas siswa
siswa2 = siswa("Muhammad Fardan Arrizieq", "XI MIA 3", 15, "Bantul")
#Membuat objek ketiga dari kelas siswa
siswa3 = siswa("Muhammad Alauddin Hilmy", "XI MIA 1", 26, "Kota Yogyakarta")
#Membuat objek keempat dari kelas siswa
siswa4 = siswa("Muhammad Zacky Kusnail", "XI MIA 3", 21, "Sleman")

siswa1.tampilkan_profil()
siswa2.tampilkan_profil()
siswa3.tampilkan_profil()
siswa4.tampilkan_profil()
print("Total siswa : ", siswa.jumlah_siswa)