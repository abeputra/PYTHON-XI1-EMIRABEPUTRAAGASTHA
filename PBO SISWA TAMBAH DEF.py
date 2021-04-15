class siswa:
    '''Dasar kelas untuk semua siswa'''
    jumlah_siswa = 0

    def __init__(self, nama, kelas, absen, alamat, panggilan):
        self.nama = nama
        self.kelas = kelas
        self.absen = absen
        self.alamat = alamat
        self.panggilan = panggilan
        siswa.jumlah_siswa += 1
    
    def tampilkan_jumlah(self):
        print("Total siswa : ", siswa.jumlah_siswa)
    
    def tampilkan_profil(self):
        print("Nama : ", self.nama)
        print("Kelas : ", self.kelas)
        print("Absen : ", self.absen)
        print("Alamat : ", self.alamat)
        print()
    
    def tampilkan_panggilan(self):
        print(self.nama, " : ", self.panggilan)

#Membuat objek pertama dari kelas siswa
siswa1 = siswa("Muhammad Dary Arkan", "XI MIA 4", 19, "Bantul", "Arkan")
#Membuat objek kedua dari kelas siswa
siswa2 = siswa("Muhammad Fardan Arrizieq", "XI MIA 2", 15, "Bantul", "Fardan")
#Membuat objek ketiga dari kelas siswa
siswa3 = siswa("Muhammad Alauddin Hilmy", "XI MIA 1", 26, "Kota Yogyakarta", "Hilmy")
#Membuat objek keempat dari kelas siswa
siswa4 = siswa("Muhammad Zacky Kusnail", "XI MIA 3", 21, "Sleman", "Zakus")

print("Profil lengkap")
siswa1.tampilkan_panggilan(), siswa1.tampilkan_profil()
siswa2.tampilkan_panggilan(), siswa2.tampilkan_profil()
siswa3.tampilkan_panggilan(), siswa3.tampilkan_profil()
siswa4.tampilkan_panggilan(), siswa4.tampilkan_profil()

print("Daftar nama dan panggilan")
siswa1.tampilkan_panggilan()
siswa2.tampilkan_panggilan()
siswa3.tampilkan_panggilan()
siswa4.tampilkan_panggilan()

print()
print("Total siswa : ", siswa.jumlah_siswa)