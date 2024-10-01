## Informasi

Nama : Vander Gerald Sukandi

NPM  : 1906350603

## Tugas 4 Menjawab Beberapa Pertanyaan

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

**1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Ketika ada beberapa CSS selector untuk suatu elemen HTML, browser menentukan style mana yang akan diterapkan berdasarkan specificity dan urutan cascade. Specificity dihitung dengan melihat inline style (menggunakan style) dengan prioritas tertinggi, diikuti oleh ID selector (#), class dan attribute selector (.), kemudian element selector (seperti p { } ) yang memiliki specificity terendah. Menggunakan !important over-ride deklarasi lain, tetapi tidak direkomendasikan. Dan jika dua selector memiliki specificity yang sama, yang muncul terakhir di file css atau html akan mendapatkan presedens .



**2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Responsive design menjamin bahwa sebuah website atau aplikasi web memberikan pengalaman pengguna yang optimal di berbagai device, dari desktop sampai mobile. Hal ini penting karena kita menginginkan User Experience yang baik dan akomodasi user terhadap web yang bisa diakses lewat mobile phone. 

Contoh aplikasi web yang responsif: website tokopedia memiliki layout design yang berbeda tapi konsisten di desktop dan mobile.

Contoh aplikasi web yang tidak responsif: aren.cs.ui.ac.id . Desain tidak dibuat untuk mobile . 

**3.  Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

Margin, border, dan padding adalah bagian dari css box .

Margin adalah ruang diluar border yang memisahkan satu elemen dari elemen lain.
Border adalah baris yang membungkus padding dan content.
Padding adalah ruang di dalam border, di antara border dan content
```
.element {
    margin: 25px;
}
.element {
    border: 2px solid #111;
}
.element {
    padding: 15px;
}
```
Ketiga hal itu diimplementasikan oleh Django melalui CSS di template atau file static yang ditentukan lokasinya melalui STATIC_URL dan STATICFILES_DIRS. 

Dan kita bisa membuatnya dengan class dari Tailwind CSS.

```
<div class="m-5 p-4 border">
    Content
</div>
```

**4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!***

Keduanya merupakan model layout CSS untuk menciptakan web design yang responsif.

Flexbox digunakan untuk layout satu-dimensi, bisa jadi baris atau kolom. Digunakan dengan `display:flex;` untuk containernya.

Ada property penting seperti flex-direction, justify-content , dan align-items. Flex digunakan untuk menyesuaikan letak objek, membuat navbar, dan membuat ruang dalam container.

Sedangkan grid layout bersifat dua-dimensi. Didefinisikan untuk kontainernya dengan `display:grid;`  . Digunakan untuk layout yang rumit seperti galeri gambar untuk sebuah website, struktur seperti tabel, dashboard, dll.

**5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Membaca tutorial sebelumnya. 
Memahami AuthenticationForm, UserCreationForm, HttpResponseRedire 
Menambahkan dan memodifikasi templates yang sesuai
Menambahkan baris baru mengenai User untuk foreign key model Item di models.py . 
Melakukan python manage.py makemigrations dan python manage.py migrate
Menambahkan @login_required(login_url='/login') ke beberapa function Tugas 3 


**5. Jelaskan cara kamu mengimplementasikan checklist di atas secare step-by-step**
Membaca tutorial
Menambahkan functions terkait edit dan delete Item di views.py dan menambahkan url routing terkait. 
Menambahkan tailwind.css .
Membuat navbar.html .
Mengubah base.html.
Mengubah template
Mengubah settings.py untuk static . 
Menambahkan gambar...
Melakukan deployment.. 



http://vander-gerald-simplepbpeshop.pbp.cs.ui.ac.id/
