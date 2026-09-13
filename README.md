Nama : Asmiranda Ghina W
NPM : 2506656482
Kelas : PBP E

### Tugas 1
1. Ya, saya menggunakan elemen semantik HTML5 seperti <header>, <nav>, <main>, <section>, <footer> untuk menampilkan data. Elemen-elemen ini membantu memisahkan bagian profil dan bagian kegemaran secara jelas, sehingga kode lebih mudah dibaca.

2. Tantangan utama saya pada mengatur tata letak adalah menentukan section mana yang benar butuh tata letak grid multi-kolom dan bagaimana urutannya berubah dari desktop ke mobile. Selanjutnya pada section kegemaran, saya sempat meniru pola grid milik .hero-grid. Setelah saya evaluasi, saya ubah jadi satu kolom lalu menerapkan grid tiga kolom langsung, dan melakukan penyesuaian juga di media query agar pada layar yang sempit tetap rapi hasil akhirnya.

3. Batasan yang saya rasakan adalah saya harus tulis ulang manual di HTML setiap kali ada perubahan, dan tidak ada cara bagi pengunjung untuk berinteraksi lebih dari sekadar membaca. Saya berharap di iterasi berikutnya bisa mengurangi proses edit manual ini, meski saya belum tahu detail fitur seperti apa yang paling tepat.

Penggunaan AI:
Saya menggunakan Claude untuk membantu debug error contohnya berupa typo yang menyebabkan kode tidak bekerja, serta memahami konsep dan artian yang lebih jelas dari setiap baris kode yang ada pada tutorial 0. Bagian yang saya putuskan sendiri adalah dari pemilihan warna, font, isi dan struktur section Kegemaran. Keterbatasan yang saya temukan pada penggunaan AI adalah pada saat AI menyarankan menggabungkan section kegemaran pada grid yang sama dengan section .hero, yang kemudian setelah saya evaluasi lebih sesuai untuk dipisah dan membuat grid tersendiri.

### Tugas 2
1. Ketika pengguna mengakses halaman baru, permintaan pertama diterima oleh urls.py proyek yang tugasnya melihat awalan URL dan meneruskannya lewat include() ke urls.py aplikasi. Pemisahan ini membuat lebih terorganisir, karena urls.py proyek tidak perlu mengetahui detail setiap path, cukup oper ke urls.py aplikasi yang bersangkutan. Di urls.py aplikasi, path yang cocok akan memanggil view yang sesuai. View kemudian mengambil data dari model lewat sintaks Activity.objects.all() yang dibungkus dalam dictionary context, lalu meneruskannya ke template lewat render(). Template memproses menggunakan Django Template Language untuk ditampilkan sebagai HTML, yang akhirnya dikembalikan sebagai respons ke pengguna.

2. Karena data bersifat dinamis dan jumlahnya bisa berubah sewaktu-waktu. Kalau ditulis manual di HTML, harus buka dan edit file HTML setiap kali ingin menambah atau mengubah data, yang rawan timbul typo. Karena data dinamis, template menggunakan {% for %} dan {% empty %} agar bisa menangani kemungkinan kasus.

3. makemigrations berfungsi untuk membuat berkas migrasi yang berisi rencana perubahan model yang belum diterapkan ke database, sedangkan migrate berfungsi untuk menerapkan perubahan ke database. Kalau hanya menjalankan makemigrations tanpa migrate, berkas migrasinya sudah terbuat tetapi database belum benar-benar berubah. Kalau menjalankan migrate tanpa makemigrations terlebih dahulu, Django tidak akan mengetahui adanya perubahan baru karena Django hanya membaca dari berkas migrasi yang sudah ada, bukan langsung dari models.py.