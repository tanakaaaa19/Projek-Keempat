catatan = []

def tambah_catatan():
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik belajar: ")
    durasi = input("Masukkan durasi belajar (menit): ")
    
    # Menyimpan data dalam bentuk dictionary
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": int(durasi)
    }
    
    # Menambahkan ke list catatan
    catatan.append(catatan_baru)
    print("✓ Catatan berhasil ditambahkan!\n")

def lihat_catatan():
    if len(catatan) == 0:
        print("\n⚠ Belum ada catatan belajar.\n")
    else:
        print("\n=== Daftar Catatan Belajar ===")
        for i, data in enumerate(catatan, 1):
            print(f"\nNo. {i}")
            print(f"Mapel   : {data['mapel']}")
            print(f"Topik   : {data['topik']}")
            print(f"Durasi  : {data['durasi']} menit")
            print("-" * 35)
        print()

def total_waktu():
    pass

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")