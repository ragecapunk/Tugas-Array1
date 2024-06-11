# Inisialisasi array untuk menyimpan data mahasiswa
mahasiswa = []

# Inisialisasi array untuk menyimpan data inventaris barang
inventaris = []

# Inisialisasi variabel untuk menyimpan transaksi
transaksi = []

def input_data():
    # Fungsi untuk menginput data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan prodi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    mahasiswa.append([nama, nim, prodi, nilai])
    print("Data mahasiswa berhasil ditambahkan!")

def tampilkan_data():
    # Fungsi untuk menampilkan data mahasiswa
    print("Data Mahasiswa:")
    for i, data in enumerate(mahasiswa):
        print(f"Mahasiswa {i+1}:")
        print(f"Nama: {data[0]}")
        print(f"NIM: {data[1]}")
        print(f"Prodi: {data[2]}")
        print(f"Nilai: {data[3]}")
        print()

def hitung_rata_rata():
    # Fungsi untuk menghitung dan menampilkan rata-rata nilai mahasiswa
    total_nilai = sum(data[3] for data in mahasiswa)
    rata_rata = total_nilai / len(mahasiswa)
    print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")

def cari_nilai_tertinggi_terendah():
    # Fungsi untuk mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah
    nilai_tertinggi = max(mahasiswa, key=lambda x: x[3])
    nilai_terendah = min(mahasiswa, key=lambda x: x[3])
    print("Mahasiswa dengan nilai tertinggi:")
    print(f"Nama: {nilai_tertinggi[0]}")
    print(f"NIM: {nilai_tertinggi[1]}")
    print(f"Prodi: {nilai_tertinggi[2]}")
    print(f"Nilai: {nilai_tertinggi[3]}")
    print()
    print("Mahasiswa dengan nilai terendah:")
    print(f"Nama: {nilai_terendah[0]}")
    print(f"NIM: {nilai_terendah[1]}")
    print(f"Prodi: {nilai_terendah[2]}")
    print(f"Nilai: {nilai_terendah[3]}")

def input_barang():
    # Fungsi untuk menginput data barang
    nama_barang = input("Masukkan nama barang: ")
    kode_barang = input("Masukkan kode barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    inventaris.append([nama_barang, kode_barang, jumlah_barang])
    print("Data barang berhasil ditambahkan!")

def tampilkan_barang():
    # Fungsi untuk menampilkan semua barang
    print("Data Inventaris Barang:")
    for i, barang in enumerate(inventaris):
        print(f"Barang {i+1}:")
        print(f"Nama: {barang[0]}")
        print(f"Kode: {barang[1]}")
        print(f"Jumlah: {barang[2]}")
        print()

def cari_barang():
    # Fungsi untuk mencari barang berdasarkan kode
    kode_cari = input("Masukkan kode barang yang ingin dicari: ")
    for barang in inventaris:
        if barang[1] == kode_cari:
            print("Barang ditemukan!")
            print(f"Nama: {barang[0]}")
            print(f"Kode: {barang[1]}")
            print(f"Jumlah: {barang[2]}")
            return
    print("Barang tidak ditemukan!")

def hapus_barang():
    # Fungsi untuk menghapus barang berdasarkan kode
    kode_hapus = input("Masukkan kode barang yang ingin dihapus: ")
    for i, barang in enumerate(inventaris):
        if barang[1] == kode_hapus:
            del inventaris[i]
            print("Barang berhasil dihapus!")
            return
    print("Barang tidak ditemukan!")

def tambah_transaksi():
    # Fungsi untuk menginput transaksi
    print("Tambah Transaksi")
    jenis = input("Jenis Transaksi (Pemasukan/Pengeluaran): ")
    nominal = int(input("Nominal: "))
    transaksi.append({"jenis": jenis, "nominal": nominal})
    print("Transaksi berhasil ditambahkan!")
    
def tampilkan_transaksi():
    # Fungsi untuk menampilkan semua transaksi
    print("Daftar Transaksi")
    for i, trx in enumerate(transaksi):
        print(f"{i+1}. {trx['jenis']} - {trx['nominal']}")

def menghitung_total_pemasukan_pengeluaran(jenis):
    # Fungsi untuk menghitung dan menampilkan total pemasukan/pengeluaran
    total = sum(trx["nominal"] for trx in transaksi if trx["jenis"] == jenis.capitalize())
    print(f"Total {jenis.capitalize()}: {total}")

def hitung_saldo():
    # Fungsi untuk menghitung dan menampilkan saldo akhir
    pemasukan = sum(trx["nominal"] for trx in transaksi if trx["jenis"] == "Pemasukan")
    pengeluaran = sum(trx["nominal"] for trx in transaksi if trx["jenis"] == "Pengeluaran")
    saldo = pemasukan - pengeluaran
    print(f"Saldo Akhir: {saldo}")

def main():
    while True:
        print("Menu:")
        print("1. Pengelolaan Data Mahasiswa")
        print("2. Pengelolaan Inventaris Barang")
        print("3. Pengelolaan Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            while True:
                print("Menu Pengelolaan Data Mahasiswa:")
                print("1. Input Data Mahasiswa")
                print("2. Tampilkan Data Mahasiswa")
                print("3. Hitung Rata-Rata Nilai Mahasiswa")
                print("4. Cari Mahasiswa dengan Nilai Tertinggi dan Terendah")
                print("5. Kembali")
                pilihan_mahasiswa = input("Pilih menu: ")
                if pilihan_mahasiswa == "1":
                    input_data()
                elif pilihan_mahasiswa == "2":
                    tampilkan_data()
                elif pilihan_mahasiswa == "3":
                    hitung_rata_rata()
                elif pilihan_mahasiswa == "4":
                    cari_nilai_tertinggi_terendah()
                elif pilihan_mahasiswa == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
        elif pilihan == "2":
            while True:
                print("Menu Pengelolaan Inventaris Barang:")
                print("1. Input Data Barang")
                print("2. Tampilkan Data Barang")
                print("3. Cari Barang Berdasarkan Kode")
                print("4. Hapus Barang Berdasarkan Kode")
                print("5. Kembali")
                pilihan_barang = input("Pilih menu: ")
                if pilihan_barang == "1":
                    input_barang()
                elif pilihan_barang == "2":
                    tampilkan_barang()
                elif pilihan_barang == "3":
                    cari_barang()
                elif pilihan_barang == "4":
                    hapus_barang()
                elif pilihan_barang == "5":
                    break
                else:
                    print("Pilihan tidak valid!")
        elif pilihan == "3":
            while True:
                print("Menu Pengelolaan Keuangan Pribadi:")
                print("1. Tambah Transaksi")
                print("2. Tampilkan Transaksi")
                print("3. Total Pemasukan")
                print("4. Total Pengeluaran")
                print("5. Hitung Saldo")
                print("6. Kembali")
                pilihan_keuangan = input("Pilih menu: ")
                if pilihan_keuangan == "1":
                    tambah_transaksi()
                elif pilihan_keuangan == "2":
                    tampilkan_transaksi()
                elif pilihan_keuangan == "3":
                    menghitung_total_pemasukan_pengeluaran("pemasukan")
                elif pilihan_keuangan == "4":
                    menghitung_total_pemasukan_pengeluaran("pengeluaran")
                elif pilihan_keuangan == "5":
                    hitung_saldo()
                elif pilihan_keuangan == "6":
                    break
                else:
                    print("Pilihan tidak valid!")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()