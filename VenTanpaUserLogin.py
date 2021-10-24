# Prototype Program Vending Machine

# Kamus:
# def vending(): fungsi untuk vending machine
# def menunjukkan(items): fungsi untuk menampilkan list barang yang terdapat pada vending ke user (sebagai display)
# items: menyimpan list dari dictionary item (kode barang, barang, dan harga)
# uang: variabel yang merepresentasikan uang yang dimasukkan oleh user
# pilihan: variabel yang merepresentasikan pilihan kode yang dimasukkan oleh user
# harga: variabel harga dari list item
# opsi: variabel yang menentukan apakah user akan melanjutkan transaksi atau tidak
# .get(): fungsi untuk mengambil nilai elemen dari dictionary

# Buat prosedur/fungsinya terlebih dahulu supaya vending machine mudah untuk dimanage oleh penjual
def vending():

    # Buat kumpulan listnya dari nomor item, nama item, dan harga item
    # Harga dan barang masih dapat diganti atau ditambah oleh penjual
    # Untuk menambah opsi barang, buat list lalu masukkan listnya ke dalam list items
    a = {"no": "1A", "item": "Frestea        ", "harga": 3500}
    b = {"no": "1B", "item": "Teh Botol Sosro", "harga": 3500}
    c = {"no": "1C", "item": "Teh Gelas Botol", "harga": 3000}
    d = {"no": "2A", "item": "Good Day       ", "harga": 7000}
    e = {"no": "2B", "item": "Kopiko 78      ", "harga": 7000}
    f = {"no": "2C", "item": "Golda Coffee   ", "harga": 7000}
    g = {"no": "3A", "item": "Sprite         ", "harga": 4000}
    h = {"no": "3B", "item": "Coca Cola      ", "harga": 4000}
    i = {"no": "3C", "item": "Fanta          ", "harga": 4000}
    items = [a, b, c, d, e, f, g, h, i]

    # Inisialisasi keadaan ketika uangnya masih sama dengan nol
    uang = 0

    print("")
    print("* "*31)
    print("*                   Mesin Penjual Minuman" + (" "*19) + "*")
    print("*           Sedia aneka Teh, Kopi, dan Soft Drink" + (" "*11) + "*")
    print("* "*31)
    print("")
    print("* "*31)

    # Buat fungsi untuk menunjukkan pilihan items ke pelanggan
    def menunjukkan(items):

        for item in items:

            # .get berfungsi untuk mengambil item yang terdapat pada list
            print("* ", "Kode:", item.get("no"), "||", "Barang:", item.get("item"), "||", "Harga:", "Rp.", item.get("harga"), "  *")

        print("* "*31)
        print("")

    # Kita panggil lagi fungsi yang sudah dibuat supaya bekerja
    menunjukkan(items)

    # Pilihan input oleh user
    pilihan = input("Silakan masukkan kode minuman yang ingin Anda beli: ")

    # Algoritma:
    for item in items:

        # Jika user sudah memasukkan kode dengan benar
        if pilihan == item.get("no"):

          # Program akan menampilkan barang yang ingin user beli
            pilihan = item
            harga = pilihan.get("harga")
            print("")
            print("Anda akan membeli " + pilihan.get("item"))
            print("Apakah Anda sudah yakin?")
            print("")
            print("1. Ya")
            print("2. Tidak")
            print("")
            opsi = int(input("Tekan tombol 1 atau 2: "))

            # Jika user sudah yakin, maka program akan menampilkan dan meminta besaran harga yang harus dibayar
            if opsi == 1:

                print("")
                print("Total harga: Rp. " + str(harga - uang))
                uang = uang + int(input('Masukkan uang: Rp. '))

                # Ketika uang yang dimasukkan user kurang dari harga, program akan terus meminta sisa uang yang kurang
                while uang < harga:
                    print("")
                    print("Uang yang Anda masukkan masih kurang sebesar Rp. " + str(harga - uang))
                    uang = uang + int(input('Masukkan uang: Rp. '))

                # Ketika uang yang dimasukkan sudah sesuai, program akan memberikan barang kepada user sesuai dengan kode yang sudah dimasukkan
                print("")
                print("Transaksi Anda berhasil!")
                print("Anda telah membeli " + pilihan.get('item'))

                # Program akan mengupdate uang dari user
                uang -= harga

                # Jika jumlah uang bersisa, maka program akan mengembalikan sisa uang kepada user sebagai kembalian
                if uang != 0:

                    print("")
                    print("Kembalian: Rp. " + str(uang))
                    print("")
                    uang = 0
                    print("Terima kasih telah mengunjungi Mesin Penjual Minuman kami.")
                    print("Have a Nice Day!")
                    break

                # Jika uang pas, maka program akan memberikan ucapan terima kasih
                else:

                    print("")
                    print("Terima kasih telah mengunjungi Mesin Penjual Minuman kami.")
                    print("Have a Nice Day!")
                    break

            # Jika user belum yakin, program akan berhenti dan user diminta merestart vending machine jika ingin memilih barang lagi
            elif opsi == 2:

                print("")
                print("Jika ingin melanjutkan transaksi,")
                print("Silahkan restart Mesin Penjual Minuman kami")
                break

# Memanggil fungsi yang sudah kita buat di paling awal supaya program bekerja
vending()