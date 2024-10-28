class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        self.spp_bayar = False
        self.nilai = []

    def bayar_spp(self):
        self.spp_bayar = True
        print(f"{self.nama} telah membayar SPP.")

    def ambil_mata_kuliah(self, nama_mk):
        print(f"{self.nama} mengambil mata kuliah {nama_mk}.")

    def masukkan_nilai(self, nilai):
        self.nilai.append(nilai)
        print(f"{self.nama} telah mendapatkan nilai {nilai}.")

    def hitung_nilai_akhir(self):
        if not self.nilai:
            return 0
        return sum(self.nilai) / len(self.nilai)

def main():
    print("Selamat datang di sistem kuliah Informatika!")
    
    # Membuat objek mahasiswa
    nama_mahasiswa = input("Masukkan nama mahasiswa: ")
    mahasiswa = Mahasiswa(nama_mahasiswa)

    # Proses pembayaran SPP
    bayar = input("Apakah anda ingin membayar SPP? (ya/tidak): ")
    if bayar.lower() == 'ya':
        mahasiswa.bayar_spp()
    else:
        print("Anda harus membayar SPP untuk melanjutkan.")

    # Mengambil mata kuliah
    mata_kuliah = input("Masukkan nama mata kuliah yang diambil: ")
    mahasiswa.ambil_mata_kuliah(mata_kuliah)

    # Memasukkan nilai
    while True:
        nilai = input("Masukkan nilai yang diperoleh (atau ketik 'selesai' untuk selesai): ")
        if nilai.lower() == 'selesai':
            break
        try:
            nilai = float(nilai)
            mahasiswa.masukkan_nilai(nilai)
        except ValueError:
            print("Nilai tidak valid. Silakan masukkan angka.")

    # Menghitung dan menampilkan nilai akhir
    nilai_akhir = mahasiswa.hitung_nilai_akhir()
    print(f"Nilai akhir {mahasiswa.nama} adalah: {nilai_akhir:.2f}")

if __name__ == "__main__":
    main()
