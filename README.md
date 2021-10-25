# Vending_Machine_(Mesin_Penjual_Minuman)
Project Tugas Besar  pertama Pengenalan Komputasi Institut Teknologi Bandung

  # Raw Sketch untuk Essay

# Ringkasan
Pada tugas besar ini, kami akan membuat suatu program yang merepresentasikan sebuah Vending Machine atau Mesin Penjual Otomatis. Mesin ini akan menerima uang, menampilkan display minuman, mengecek jumlah uang, menampilkan jumlah saldo, serta memberikan output berupa minuman kepada pembeli.

# Menampilkan Display
"Sebagai penjual, kami ingin pelanggan dapat melihat barang apa saja yang tersedia pada mesin kami."

Mesin akan menampilkan display ketika ada pelanggan yang ingin membeli minuman. Mesin akan menampilkan minuman-minuman yang tersedia pada mesin termasuk Kode Minuman, Nama Minuman, dan Harga Minuman. Pada proses ini, tampilan sangat berperan penting dalam memikat hati pelanggan. Maka dari itu, kami membuat bagian display ini semenarik mungkin. 

# User Login
Sebelum pelanggan dapat memilih produk, mesin akan meminta username dan pin pelanggan. Jika username atau pin yang dimasukkan oleh pelanggan salah, pelanggan masih dapat memasukkan username dan pin sampai tiga kali. Setelah tiga kali percobaan, mesin akan mati dan pelanggan tidak dapat melanjutkan transaksi.

Catatan: Tujuan dari proses ini adalah, program dapat mengenali pelanggan melalui username dan pin yang dimasukkan oleh pelanggan.

# Memberi Informasi Saldo
"Sebagai penjual, kami tidak ingin para pelanggan kesulitan memilih produk kami lantaran lupa mengenai informasi saldo terakhirnya."

Setelah pelanggan dapat login, mesin akan memberi informasi saldo pelanggan supaya pelanggan dapat memilih produk yang sesuai dengan budget mereka.

# Memilih Produk
"Sebagai penjual, kami ingin para pelanggan dapat memilih produk yang ditawarkan oleh mesin."

Kami menyediakan berbagai minuman pada mesin kami. Terdapat aneka teh, kopi, dan soft drink. Minuman jenis teh kami identifikasikan dengan kode A, minuman jenis kopi kami identifikasikan dengan kode B, serta jenis soft drink dengan kode C. Masing-masing jenis terdapat 3 produk berbeda misalnya pada soft drink, terdapat Sprite, Fanta, dan Coca Cola. 

Ketika pelanggan sudah menentukan minuman yang ingin mereka beli, mesin akan meminta Kode Minuman kepada pelanggan. Di sini, pelanggan harus memasukkan kode dengan benar supaya Mesin Penjual Minuman dapat berjalan dengan lancar.

# Verifikasi Pelanggan
"Sebagai penjual, kami tidak ingin mengecewakan pelanggan. Salah satunya adalah ketika pelanggan masih ingin melanjutkan transaksi."

Dalam hal ini, dibuatlah program untuk memverifikasi pelanggan. Ketika pelanggan sudah memasukkan Kode Minuman serta mendapatkan minuman yang pelanggan inginkan, mesin akan memberikan pilihan kepada pelanggan. “Lanjutkan transaksi? (Y/N): ”. Jika pelanggan masih ingin melanjutkan transaksi (dalam hal ini ingin membeli minuman lagi), pelanggan akan diarahkan untuk menekan tombol “Y” sebagai bentuk verifikasi kepada mesin. Namun, jika pelanggan ingin menyudahi proses transaksi, maka pelanggan akan diarahkan untuk menekan tombol “N”.

# Menghitung Uang
"Sebagai penjual, kami menginginkan mesin yang dapat menghitung dan menerima uang. Supaya kami dapat mengambil keuntungan dari sana."

Setelah proses verifikasi pelanggan, mesin kami akan menghitung jumlah uang yang tersisa pada saldo pelanggan. Jika saldo pelanggan kurang dari harga minuman, maka mesin akan menampilkan pesan "Uang Anda tidak cukup" kepada pelanggan. Namun, jika saldo pelanggan uang masih mencukupi, mesin akan meneruskan transaksi dari pelanggan.

Catatan: Tujuannya adalah untuk membuat program yang dapat menghitung jumlah uang yang harus dibayar serta mengenali nominal uang yang harus dibayar oleh pelanggan.   

# Memberi Minuman
Hal terakhir yang sangat krusial adalah memberi output berupa minuman kepada pelanggan.

Mesin kami akan memberi minuman sesuai dengan kode yang sudah dimasukkan oleh pelanggan. Kami juga memberikan pesan terakhir kepada pelanggan berupa “Terima kasih telah mengunjungi Mesin Penjual Minuman Kami.” “Have a Nice Day!”.
