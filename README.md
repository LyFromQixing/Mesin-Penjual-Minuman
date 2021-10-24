# Vending_Machine_(Mesin_Penjual_Minuman)
Project Tugas Besar  pertama Pengenalan Komputasi Institut Teknologi Bandung

  # Raw Sketch untuk Essay

# Ringkasan
Pada tugas besar ini, kami akan membuat suatu program yang merepresentasikan sebuah Vending Machine atau Mesin Penjual Otomatis. Mesin ini akan menerima uang, menampilkan display minuman, memberikan diskon pada situasi tertentu, mengecek uang, memberi kembalian, serta memberikan output berupa minuman kepada pembeli.

# Menampilkan Display
"Sebagai penjual, kami ingin pelanggan dapat melihat barang apa saja yang tersedia pada mesin kami."

Mesin akan menampilkan display ketika ada pelanggan yang ingin membeli minuman. Mesin akan menampilkan minuman-minuman yang tersedia pada mesin termasuk Kode Minuman, Nama Minuman, dan Harga Minuman. Pada proses ini, tampilan sangat berperan penting dalam memikat hati pelanggan. Maka dari itu, kami membuat bagian display ini semenarik mungkin. 

# Memilih Produk
"Sebagai penjual, kami ingin para pelanggan dapat memilih produk yang ditawarkan oleh mesin."

Kami menyediakan berbagai minuman pada mesin kami. Terdapat aneka teh, kopi, dan soft drink. Minuman jenis teh kami identifikasikan dengan kode 1, minuman jenis kopi kami identifikasikan dengan kode 2, serta jenis soft drink dengan kode 3. Masing-masing jenis terdapat 3 produk berbeda misalnya pada soft drink, terdapat Sprite, Fanta, dan Coca Cola. 

Ketika pelanggan sudah menentukan minuman yang ingin mereka beli, mesin akan meminta Kode Minuman kepada pelanggan. Di sini, pelanggan harus memasukkan kode dengan benar supaya Mesin Penjual Minuman dapat berjalan dengan lancar.

# Verifikasi Produk
"Sebagai penjual, kami tidak ingin mengecewakan pelanggan. Salah satunya adalah ketika pelanggan tidak sengaja memasukkan kode yang salah."

Dalam hal ini, dibuatlah program untuk memverifikasi suatu produk. Ketika pelanggan sudah memasukkan Kode Minuman, mesin akan memberikan pilihan kepada pelanggan. “Anda akan membeli Fanta. Apakah Anda sudah yakin?”. Jika barang yang ingin dibeli oleh pelanggan sudah benar, pelanggan akan diarahkan untuk menekan tombol “Ya” sebagai bentuk verifikasi kepada mesin. Namun, jika pelanggan keliru memasukkan kode, maka pelanggan harus menekan tombol “Tidak”.

# Memberi Diskon
"Sebagai penjual, kamu ingin memberikan diskon khusus bagi mahasiswa ITB dan FMIPA ITB."

Setelah verifikasi produk, mesin akan menanyakan satu hal dari pelanggan sebelum beralih ke pembayaran. Di sini mesin akan menanyakan apakah pelanggan adalah Mahasiswa ITB atau bukan. Jika pelanggan adalah mahasiswa ITB, mesin akan memberikan diskon sebesar 10 %. Jika pelanggan adalah mahasiswa FMIPA ITB, mesin akan memberikan diskon sebesar 40 %.

Supaya mesin dapat mengenali pelanggan, mesin akan meminta NIM dari pelanggan. Jika NIM yang dimasukkan memiliki angka 160xxxxx, maka pelanggan tersebut adalah mahasiswa FMIPA ITB. Jika NIM yang dimasukkan memiliki angka 1xxxxxxx, maka pelanggan adalah mahasiswa ITB. 

# Menerima Uang
"Sebagai penjual, kami menginginkan mesin yang dapat menghitung dan menerima uang. Supaya kami dapat mengambil keuntungan dari sana."

Setelah penentuan diskon, mesin kami akan menghitung jumlah uang yang harus dimasukkan oleh pelanggan. Jika pelanggan memasukkan uang dengan nominal yang kurang dari harga minuman, maka mesin akan terus meminta jumlah uang yang kurang. Namun, jika pelanggan memasukkan uang dengan nominal yang lebih, mesin akan memberi kembalian kepada pelanggan.

Catatan: Tujuannya adalah untuk membuat program yang dapat menghitung jumlah uang yang harus dibayar serta mengenali nominal uang.   

# Memberi Minuman
Hal terakhir yang sangat krusial adalah memberi output berupa minuman kepada pelanggan.

Mesin kami akan memberi minuman sesuai dengan kode yang sudah dimasukkan oleh pelanggan. Kami juga memberikan pesan kepada pelanggan berupa “Terima kasih telah mengunjungi Mesin Penjual Minuman Kami.” “Have a Nice Day!”.
