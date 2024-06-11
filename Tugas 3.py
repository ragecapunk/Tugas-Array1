# Program Pengelolaan Keuangan Pribadi (ATM)

# Inisialisasi variabel untuk menyimpan transaksi
transaksi = []

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
        print("1. Tambah Transaksi")
        print("2. Tampilkan Transaksi")
        print("3. Total Pemasukan")
        print("4. Total Pengeluaran")
        print("5. Hitung Saldo")
        print("6. Keluar")
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tambah_transaksi()
        elif pilihan == "2":
            tampilkan_transaksi()
        elif pilihan == "3":
            menghitung_total_pemasukan_pengeluaran("pemasukan")
        elif pilihan == "4":
            menghitung_total_pemasukan_pengeluaran("pengeluaran")
        elif pilihan == "5":
            hitung_saldo()
        elif pilihan == "6":
            break
        else:
            print("Menu tidak tersedia. Silakan coba lagi!")

if __name__ == "__main__":
    main()