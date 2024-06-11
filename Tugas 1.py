# Inisialisasi array untuk menyimpan data mahasiswa
mahasiswa = []

def input_data():
    # Fungsi untuk menginput data mahasiswa
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan prodi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    #append: sebuah metode dalam python untuk menambah elemen dalam list.
    mahasiswa.append([nama, nim, prodi, nilai])
    print("Data mahasiswa berhasil ditambahkan!")

def tampilkan_data():
    # Fungsi untuk menampilkan data mahasiswa
    print("Data Mahasiswa:")
    #enumerate: digunakan untuk menghitung indeks dan nilai secara bersamaan dari sebuah iterasi.
    for i, data in enumerate(mahasiswa):
        print(f"Mahasiswa {i+1}:")
        print(f"Nama: {data[0]}")
        print(f"NIM: {data[1]}")
        print(f"Prodi: {data[2]}")
        print(f"Nilai: {data[3]}")
        print()

def hitung_rata_rata():
    # Fungsi untuk menghitung dan menampilkan rata-rata nilai mahasiswa
    #sum: berfungsi untuk menjumlahkan semua elemen dalam sebuah iterabel, seperti list
    total_nilai = sum(data[3] for data in mahasiswa)
    #len: digunakan untuk menghitunh semua elemen dalam sebuah iteraebel
    rata_rata = total_nilai / len(mahasiswa)
    #rata-rata :.2f yang digunakan untuk mencetak rata-rata nilai mahasiswa dengan dua angka di belakang koma
    print(f"Rata-rata nilai mahasiswa: {rata_rata:.2f}")

def cari_nilai_tertinggi_terendah():
    # Fungsi untuk mencari dan menampilkan mahasiswa dengan nilai tertinggi dan terendah
    # key=lambda digunakan dalam fungsi max dan min untuk menentukan kriteria perbandingan
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

while True:
    print("Menu:")
    print("1. Input data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Hitung rata-rata nilai mahasiswa")
    print("4. Cari mahasiswa dengan nilai tertinggi dan terendah")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1":
        input_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        hitung_rata_rata()
    elif pilihan == "4":
        cari_nilai_tertinggi_terendah()
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid!")