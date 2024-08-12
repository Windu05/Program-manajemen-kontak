#Program Manejemen Kontak

kontak1 = {'nama':"Andi", 'HP':'087777272', 'email':'Andi@pyhton.com'}
kontak2 = {'nama':"Ani", 'HP':'084578999' ,'email': 'anis@pyhton.com'}
kontak = [kontak1,kontak2]


while True:
    print("\nMenu Kontak")
    print("1. Melihat Semua Kontak")
    print("2. Menambahkan Kontak Baru")
    print("3. Menghapus Kontak")
    print("4. Keluar Kontak")

    pilihan = input("Masukan pilihan menu kontak (1,2,3, atau 4): ")

    if pilihan == '1':
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}: {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak anda kosong")
    elif pilihan == '2':
        nama = input("Masukkan nama: ")
        HP = input("Masukkan no HP: ")
        email = input("Masukkan email: ")
        kontak_baru = {'nama':nama, 'HP':HP, 'email':email}
        kontak.append(kontak_baru)
    elif pilihan == '3':
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}: {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("Kontak anda kosong")

        i_hapus = int(input("Masukan nomor yang akan dihapus: "))
        del kontak [i_hapus-1]
        print("Kontak Berhasil Dihapus")
    elif pilihan == '4':
        break
    else:
        print("Anda memasukkan pilihan yang salah")




