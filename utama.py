#Program Manejemen Kontak

def membuka_kontak(path= 'kontak.txt'):
    with open(path, mode = 'r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path = 'kontak.txt', isi = []):
    with open(path, mode = 'w') as file:
        file.writelines(isi)




class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        if self.kontak:
            for num, item in enumerate(self.kontak, start=1):
                print(f'{num}.' + item)
        else:
            print("Kontak anda kosong")
            return 1

    def menambah_kontak(self):
        nama = input("Masukkan nama: ")
        HP = input("Masukkan no HP: ")
        email = input("Masukkan email: ")
        kontak_baru = f'{nama} ({HP}, {email})' + '\n'
        self.kontak.append(kontak_baru)
        print("Kontak baru berhasil ditambahkan")

    def menghapus_kontak(self):
        try:
            if self.melihat_kontak()== 1:
                return
            else:
                i_hapus = int(input("Masukan nomor yang akan dihapus: "))
                del self.kontak[i_hapus - 1]
                print("Kontak Berhasil Dihapus")
        except:
            print("Input yang anda masukkan salah")

    def keluar_kontak(self):
            menyimpan_kontak(isi=self.kontak)


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
        kontak_kantor.keluar_kontak()
        break
    else:
        print("Anda memasukkan pilihan yang salah")




