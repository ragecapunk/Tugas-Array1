# Inisialisasi array untuk menyimpan data inventaris barang
inventaris = []

def input_barang():
    # Fungsi untuk menginput data barang
    nama_barang = input("Masukkan nama barang: ")
    kode_barang = input("Masukkan kode barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))
    #append: sebuah metode dalam python untuk menambah elemen dalam list.
    inventaris.append([nama_barang, kode_barang, jumlah_barang])
    print("Data barang berhasil ditambahkan!")

def tampilkan_barang():
    # Fungsi untuk menampilkan semua barang
    print("Data Inventaris Barang:")
    #enumerate: digunakan untuk menghitung indeks dan nilai secara bersamaan dari sebuah iterasi.
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
    #enumerate: digunakan untuk menghitung indeks dan nilai secara bersamaan dari sebuah iterasi.
    for i, barang in enumerate(inventaris):
        if barang[1] == kode_hapus:
            #del digunakan untuk menghapus elemen tertentu dari list
            del inventaris[i]
            print("Barang berhasil dihapus!")
            return
    print("Barang tidak ditemukan!")

while True:
    print("Menu:")
    print("1. Input data barang")
    print("2. Tampilkan semua barang")
    print("3. Cari barang berdasarkan kode")
    print("4. Hapus barang berdasarkan kode")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        input_barang()
    elif pilihan == "2":
        tampilkan_barang()
    elif pilihan == "3":
        cari_barang()
    elif pilihan == "4":
        hapus_barang()
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid!")