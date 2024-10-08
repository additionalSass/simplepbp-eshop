## Informasi

Nama : Vander Gerald Sukandi

NPM  : 1906350603

## Tugas 6 Menjawab Beberapa Pertanyaan 
```

    Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
    Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
    Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
    Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
    Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

```

**1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

Penggunaan JavaScript bermanfaat untuk pembuatan website yang interaktif dan dinamis. Hal ini berarti ada client-side scripting yang amana tanpa perlu reload , tampilan bisa berubah sesuai dengan logika tertentu dan meningkatkan kualitas pengalaman pengguna. JavaScript bisa memanipulasi html dan css secara dinamis dan menangani operasi async seperti fetch. 

**2.  Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**

Penggunaannya meunda eksekusi sampai hasil return dari fetch diselesaikan. Tanpa await, function akan execute terus menerus tanpa menunggu fetch selesai yang berarti hasilnya bisa jadi tidak sesuai dengan yang kita harapkan sebab data belum tentu tersedia saat itu juga. 

**3.     Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**

Digunakan untuk disable csrf protection untuk Django view karena saat membuat request AJAX POST, jika tidak mengirim token csrf yang benar, DJANGO CSRF protection secara default akan menolak request. Dengan dekorator ini, view bisa menerima request AJAX itu tanpa validasi csrf default.

**4.   Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**

Penting dilakukan di backend karena validasi frontend bisa dimanipulasi dan diabaikan oleh user yang mau menjadi hacker. Bisa saja dibuat request yang mengabaikan client-side check. Sanitasi data untuk backend menjamin bahwa injection attack tidak terjadi, bahwa input divalidasi dan dibersihkan sebelum processing. Menjamin bahwa data punya integritas dan aplikasi website aman terlepas dari tindakan klien yang kita tidak bisa kontrol sepenuhnya. 

**5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Membaca tutorial sebelumnya. 
Memahami kode-kode ajax yang sederhana 
Menambahkan fungsi add_item_entry_ajax dan memodifikasi show_json di views dan routing url
Menambahkan dan memodifikasi html templates dan menambah javascript
menambahkan impor strip_tags untuk membersihkan di backend
melakukan deployment 



http://vander-gerald-simplepbpeshop.pbp.cs.ui.ac.id/
