#Program Manejemen Kontak

class Kontak:
    def __init__(self):
        self.kontak = []

    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'\n{num}: {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak anda kosong")
            return 1

    def menambah_kontak(self):
        nama = input("Masukkan nama: ")
        HP = input("Masukkan no HP: ")
        email = input("Masukkan email: ")
        kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
        self.kontak.append(kontak_baru)

    def menghapus_kontak(self):
        if self.melihat_kontak()== 1:
            return
        else:
            i_hapus = int(input("Masukan nomor yang akan dihapus: "))
            del self.kontak[i_hapus - 1]
            print("Kontak Berhasil Dihapus")

kontak_kantor = Kontak()
kontak_keluarga = Kontak()

while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3, atau 4): ")

    if pilihan == '1':
        kontak_kantor.melihat_kontak()
    elif pilihan == '2':
        kontak_kantor.menambah_kontak()

    elif pilihan == '3':
        kontak_kantor.menghapus_kontak()

    elif pilihan == '4':
        break
    else:
        print("Anda memasukkan pilihan yang salah")




