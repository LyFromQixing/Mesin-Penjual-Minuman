print("Selamat Datang di Mesin Penjual Minuman")

a = {"no": "1A", "item": "Frestea", "harga": 3500}
b = {"no": "1B", "item": "Teh Botol Sosro", "harga": 3500}
c = {"no": "1C", "item": "Teh Gelas Botol", "harga": 3000}
d = {"no": "2A", "item": "Good Day", "harga": 7000}
e = {"no": "2B", "item": "Kopiko 78", "harga": 7000}
f = {"no": "2C", "item": "Golda Coffee", "harga": 7000}
g = {"no": "3A", "item": "Sprite", "harga": 4000}
h = {"no": "3B", "item": "Coca Cola", "harga": 4000}
i = {"no": "3C", "item": "Fanta", "harga": 4000}
items = [a, b, c, d, e, f, g, h, i]

def vending(a):
    trials = 3
    while trials != 0:
        Pin = int(input("Pin Anda: "))
        print()
        #Kalau salah
        if Pin != a[0]:
            trials -= 1
            print ("Pin yang Anda masukkan salah! Anda memiliki sisa", trials, "percobaan lagi")
        #Kalau benar
        else:
            # Buat fungsi untuk menunjukkan pilihan items ke pelanggan
            def menunjukkan(items):
                for item in items:
                    # .get berfungsi untuk mengambil item yang terdapat pada list
                    print(item.get("no"), item.get("item"), "Rp.", item.get("harga"))
                print("")
            # Kita panggil lagi fungsi yang sudah dibuat supaya bekerja
            menunjukkan(items)
            while a[1] > 0:
                print("Saldo Anda: ", a[1], "Rupiah")
                pilihan = input('Lanjutkan transaksi? (Y/N): ')
                while pilihan == 'Y' or pilihan =='y' or pilihan=='N' or pilihan=='n':
                    if pilihan == 'Y' or 'y':
                        # Buat fungsi untuk menunjukkan pilihan items ke pelanggan
                        def menunjukkan(items):
                            for item in items:
                        # .get berfungsi untuk mengambil item yang terdapat pada list
                                print(item.get("no"), item.get("item"), "Rp.", item.get("harga"))
                            print()                             
                        # Kita panggil lagi fungsi yang sudah dibuat supaya bekerja
                        menunjukkan(items)
                        Barang = input("Silakan masukkan kode minuman yang ingin dibeli = ")
                        #Frestea
                        if Barang == '1A':
                            #Kalau uangnya ga cukup
                            if a[1] < 3500:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            #Kalau uangnya cukup
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Frestea")
                                print()
                                a[1] -= 3500
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Teh Botol Sosro
                        elif Barang == '1B':
                            if a[1] < 3500:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Teh Botol Sosro")
                                print()
                                a[1] -= 3500
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Teh Gelas Botol
                        elif Barang == '1C':
                            if a[1] < 3000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Teh Gelas Botol")
                                print()
                                a[1] -= 3000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Good Day
                        elif Barang == '2A':
                            if a[1] < 7000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli GoodMood")
                                print()
                                a[1] -= 7000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Kopiko 78
                        elif Barang == '2B':
                            if a[1] < 7000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Kopiko 78")
                                print()
                                a[1] -= 7000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Golda Coffee
                        elif Barang == '2C':
                            if a[1] < 7000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Golda Coffee")
                                print()
                                a[1] -= 7000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Sprite
                        elif Barang == '3A':
                            if a[1] < 4000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Sprite")
                                print()
                                a[1] -= 4000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Coca Cola
                        elif Barang == '3B':
                            if a[1] < 4000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Coca Cola")
                                print()
                                a[1] -= 4000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                        #Fanta
                        elif Barang == '3C':
                            if a[1] < 4000:
                                print("Uang anda tidak cukup")
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                            else:
                                print("Transaksi Anda Berhasil! Anda telah membeli Fanta")
                                print()
                                a[1] -= 4000
                                option = input('Lanjutkan transaksi? (Y/N): ')
                                if option == 'Y':
                                    print()
                                elif option == 'N':
                                    print()
                                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                                    break
                    elif pilihan == 'N' or 'n':
                        print()
                        print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                        break
                    break
                break
            break
    # Coba kalau tidak pakai return?
    
Najmi = [1234, 10000]
Rafli = [2345, 100000]
Sadhira = [3456, 50000]
Azhar = [4567, 20000]

B1 = ['Fanta', 3500]

Username = input("Masukkan Username: ")
if Username == 'Najmi':
    vending(Najmi)
elif Username == 'Rafli':
    vending(Rafli)
elif Username == 'Sadhira':
    vending(Sadhira)
elif Username == 'Azhar':
    vending(Azhar)