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
*                         _   _________   ______                          *
*                        | | |___   ___| |  __  \                         *
*                        | |     | |     | |__| |                         *
*                        | |     | |     |  __  \                         *
*                        | |     | |     | |__|  |                        *
*                        |_|     |_|     |______/                         *
*                                                                         *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
"""
print(Awal)

#MENU MINUMAN
A1 = ["*  Kode: A1 ||", "Frestea         ", 3500]
A2 = ["*  Kode: A2 ||", "Teh Botol Sosro ", 3500]
A3 = ["*  Kode: A3 ||", "Teh Gelas Botol ", 3000]
B1 = ["*  Kode: B1 ||", "Good Day        ", 7000]
B2 = ["*  Kode: B2 ||", "Kopiko 78       ", 7000]
B3 = ["*  Kode: B3 ||", "Golda Coffee    ", 7000]
C1 = ["*  Kode: C1 ||", "Sprite          ", 4000]
C2 = ["*  Kode: C2 ||", "Coca Cola       ", 4000]
C3 = ["*  Kode: C3 ||", "Fanta           ", 4000]
Z = '*  Kode: 0  || Exit                                         *'

#USER ID
NAJMI = [1234, 10000]
RAFLI = [2345, 100000]
SADHIRA = [3456, 50000]
AZHAR = [4567, 20000]

#FUNGSI PROGRAM
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
                print("* " * 31)
                print('*', ' ' * 25, '|MENU|', ' ' * 24, '*')
                print(A1[0], 'Barang:', A1[1], '||', 'Harga: Rp.', A1[2], ' *')
                print(A2[0], 'Barang:', A2[1], '||', 'Harga: Rp.', A2[2], ' *')
                print(A3[0], 'Barang:', A3[1], '||', 'Harga: Rp.', A3[2], ' *')
                print(B1[0], 'Barang:', B1[1], '||', 'Harga: Rp.', B1[2], ' *')
                print(B2[0], 'Barang:', B2[1], '||', 'Harga: Rp.', B2[2], ' *')
                print(B3[0], 'Barang:', B3[1], '||', 'Harga: Rp.', B3[2], ' *')
                print(C1[0], 'Barang:', C1[1], '||', 'Harga: Rp.', C1[2], ' *')
                print(C2[0], 'Barang:', C2[1], '||', 'Harga: Rp.', C2[2], ' *')
                print(C3[0], 'Barang:', C3[1], '||', 'Harga: Rp.', C3[2], ' *')
                print(Z)
                print("* " * 31)
                print()
                print("Saldo Anda                                     :", 'Rp.', a[1])
                Barang = input("Silakan masukkan kode minuman yang ingin dibeli: ")
                if Barang == 'A1':
                    #Kalau uangnya ga cukup
                    if a[1] < A1[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    #Kalau uangnya cukup
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", A1[1])
                        print()
                        a[1] -= A1[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'A2':
                    if a[1] < A2[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", A2[1])
                        print()
                        a[1] -= A2[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                                print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'A3':
                    if a[1] < A3[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", A3[1])
                        print()
                        a[1] -= A3[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'B1':
                    if a[1] < B1[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", B1[1])
                        print()
                        a[1] -= B1[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'B2':
                    if a[1] < B2[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", B2[1])
                        print()
                        a[1] -= B2[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'B3':
                    if a[1] < B3[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", B3[1])
                        print()
                        a[1] -= B3[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'C1':
                    if a[1] < C1[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", C1[1])
                        print()
                        a[1] -= C1[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'C2':
                    if a[1] < C2[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", C2[1])
                        print()
                        a[1] -= C2[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                elif Barang == 'C3':
                    if a[1] < C3[2]:
                        print()
                        print("Uang anda tidak cukup")
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                exit
                                break
                            elif option2 == 'N':
                                print()
                    else:
                        print()
                        print("Transaksi Anda Berhasil! Anda telah membeli", C3[1])
                        print()
                        a[1] -= C3[2]
                        option = input('Lanjutkan transaksi? (Y/N): ')
                        if option == 'Y':
                            print()
                        elif option == 'N':
                            print()
                            print('Terima kasih telah mengunjungi Mesin Penjual Minuman kami, Have a Nice Day!')
                            option2 = input('Exit? (Y/N): ')
                            if option2 == 'Y':
                                break
                            elif option2 == 'N':
                                print()
                #exit
                elif Barang == '0':
                    break
                else:
                    print()
                    print('Kode yang Anda masukkan salah! Coba lagi!')
                    print()
            break
    return     

#PROGRAM DENGAN MEMANGGIL FUNGSI YANG TELAH DITULIS SEBELUMNYA  
Username = input("Masukkan Username: ")
if Username == 'NAJMI':
    vending(NAJMI)
elif Username == 'RAFLI':
    vending(RAFLI)
elif Username == 'SADHIRA':
    vending(SADHIRA)
elif Username == 'AZHAR':
    vending(AZHAR)