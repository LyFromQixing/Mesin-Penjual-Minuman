Awal = """
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*  __        __  _____   ___     _   _____     _   ___     _     ______   *
*  \ \      / / |  ___| |   \   | | |  __ \   | | |   \   | |   / _____|  *
*   \ \    / /  | |___  | |\ \  | | | |  \ \  | | | |\ \  | |  / /  ___   *
*    \ \  / /   |  ___| | | \ \ | | | |   | | | | | | \ \ | | | |  |_  |  *
*     \ \/ /    | |___  | |  \ \| | | |__/ /  | | | |  \ \| |  \ \___| |  *
*      \__/     |_____| |_|   \___| |_____/   |_| |_|   \___|   \______|  *
*  ___        ___       __        ____    _    _   _   ___     _   _____  *
* |   \      /   |     /  \      / __ \  | |  | | | | |   \   | | |  ___| *
* | |\ \    / /| |    / /\ \    / /  \_\ | |__| | | | | |\ \  | | | |___  *
* | | \ \  / / | |   / /__\ \  | |    __ |  __  | | | | | \ \ | | |  ___| *
* | |  \ \/ /  | |  / ______ \  \ \__/ / | |  | | | | | |  \ \| | | |___  *
* |_|   \__/   |_| /_/      \_\  \____/  |_|  |_| |_| |_|   \___| |_____| *
*                        _   _________   ______                           *
*                       | | |___   ___| |  __  \                          *
*                       | |     | |     | |__| |                          *
*                       | |     | |     |  __  \                          *
*                       | |     | |     | |__|  |                         *
*                       |_|     |_|     |______/                          *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
print(Awal)
A1 = {"no": "A1", "item": "Frestea        ", "harga": 3500}
A2 = {"no": "A2", "item": "Teh Botol Sosro", "harga": 3500}
A3 = {"no": "A3", "item": "Teh Gelas Botol", "harga": 3000}
B1 = {"no": "B1", "item": "Good Day       ", "harga": 7000}
B2 = {"no": "B2", "item": "Kopiko 78      ", "harga": 7000}
B3 = {"no": "B3", "item": "Golda Coffee   ", "harga": 7000}
C1 = {"no": "C1", "item": "Sprite         ", "harga": 4000}
C2 = {"no": "C2", "item": "Coca Cola      ", "harga": 4000}
C3 = {"no": "C3", "item": "Fanta          ", "harga": 4000}
Z = '*  Kode: 0  || exit                                         *'
items = [A1, A2, A3 ,B1, B2, B3, C1, C2, C3]

def vending(a):
    trials = 3
    while trials != 0:
        Pin = int(input("Pin Anda         : "))
        print()
        #Kalau salah
        if Pin != a[0]:
            trials -= 1
            print ("Pin yang Anda masukkan salah! Anda memiliki sisa", trials, "percobaan lagi")
        #Kalau benar
        else:
            while a[1] >= 0:
                # Buat fungsi untuk menunjukkan pilihan items ke pelanggan
                def menunjukkan(items):
                    print("* " * 31)
                    print('*', ' ' * 25, '|MENU|', ' ' * 24, '*')
                    for item in items:
                        # .get berfungsi untuk mengambil item yang terdapat pada list
                        print("* ", "Kode:", item.get("no"), "||", "Barang:", item.get("item"), "||", "Harga:", "Rp.",
                            item.get("harga"), "  *")
                # Kita panggil lagi fungsi yang sudah dibuat supaya bekerja
                menunjukkan(items)
                print(Z)
                print("* " * 31)
                print()
                print("Saldo Anda: ", a[1], "Rupiah")
                Barang = input("Silakan masukkan kode minuman yang ingin dibeli = ")
                if Barang == 'A1':
                    #Kalau uangnya ga cukup
                    if a[1] < A1["harga"]:
                        print()
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
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", A1["item"])
                        print()
                        a[1] -= A1["harga"]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'A2':
                    if a[1] < A2['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", A2['item'])
                        print()
                        a[1] -= A2['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                                print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'A3':
                    if a[1] < A3['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", A3['item'])
                        print()
                        a[1] -= A3['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'B1':
                    if a[1] < B1['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", B1['item'])
                        print()
                        a[1] -= B1['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'B2':
                    if a[1] < B2['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", B2['item'])
                        print()
                        a[1] -= B2['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'B3':
                    if a[1] < B3['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", B3['item'])
                        print()
                        a[1] -= B3['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'C1':
                    if a[1] < C1['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", C1['item'])
                        print()
                        a[1] -= C1['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'C2':
                    if a[1] < C2['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", C2['item'])
                        print()
                        a[1] -= C2['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                elif Barang == 'C3':
                    if a[1] < C3['harga']:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", C3['item'])
                        print()
                        a[1] -= C3['harga']
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            break
                #exit
                elif Barang == '0':
                    print ()
                    print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                    break
                else:
                    print()
                    print('Kode yang Anda masukkan salah! Coba lagi!')
                    print()
            break
    return     
    
NAJMI = [1234, 10000]
RAFLI = [2345, 100000]
SADHIRA = [3456, 50000]
AZHAR = [4567, 20000]

Username = input("Masukkan Username: ")
if Username == 'NAJMI':
    vending(NAJMI)
elif Username == 'RAFLI':
    vending(RAFLI)
elif Username == 'SADHIRA':
    vending(SADHIRA)
elif Username == 'AZHAR':
    vending(AZHAR)