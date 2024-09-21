## Informasi

Nama : Vander Gerald Sukandi

NPM  : 1906350603

## Tugas 4 Menjawab Beberapa Pertanyaan


**1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?**

Perbedaannya adalah redirect() lebih fleksibel dan user-friendly dalam perkara menerima berbagai type dari input (URLs, view names, model), sementara HttpResponseRedirect() lebih low-level dan membutuhkan URL string yang tepat untuk inputnya. Kita bisa menyebut function lebih high-level ini sebagai sebuah shortcut. 

Dari dokumentasinya :
```
redirect(to, *args, permanent=False, **kwargs)[source]¶
    Returns an HttpResponseRedirect to the appropriate URL for the arguments passed.
    The arguments could be:
        A model: the model’s get_absolute_url() function will be called.
        A view name, possibly with arguments: reverse() will be used to reverse-resolve the name.
        An absolute or relative URL, which will be used as-is for the redirect location.
    By default issues a temporary redirect; pass permanent=True to issue a permanent redirect.
``` 


**2. Jelaskan cara kerja penghubungan model Product dengan User!**

Saya tidak memakai model Product, tetapi model Item di sini. Tetapi secara esensi sama saja. Di sini, User di dalam konteks ORM merupakan sebuah ForeignKey. Foreign key merupakan type field Django yang menciptakan relasi many-to-one. Hal ini berarti beberapa instance dari Item bisa dihubungkan dengan satu instance User. 

Untuk menghubungkannya, digunakan models.ForeignKey di dalam Item model. Baris tersebut ialah 
```
user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
``` 

Kemudian, kita bisa membuat baris seperti 'item.user = request.user' di dalam views.py untuk menyimpan instance Item tertentu yang diasosiasikan dengan user yang login.

**3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

Authentication ialah proses memverifikasi identitas dari user. Pertanyaan yang dijawab ialah siapakah kamu yang sedang mengakses website melalui browser tertentu. Hal ini dilakukan melalui form login yang mana user harus menyediakan username dan password.

Authorization ialah proses menentukan apa saja yang diperbolehkan untuk user tertentu yang sudah log-in/terautentikasi/ Pertanyaan yang dijawab ialah apa yang kamu boleh lakukan. Sistem mengecek permission untuk akses resource atau melakukan tindakan tertentu.

Ketika user log in, dilakukan authentication dari credentials (username dan password) bisa dengan AuthenticationForm . Tetapi, pada dasarnya akan dilibatan authenticate() jika kita tidak membuat function sendiri. Ada built-in system untuk authentication (django.contrib.auth) yang digunakan untuk login, logout, password.  Jika berhasil submit credentials yang sesuai , akan dibuat session untuk user, disimpan infonya, dan user ditandai logged-in dengan fungsi login(). Authentication mengecek identitas, authorization mengecek permission.  

**4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django menggunakan session untuk mengingat bahwa sebuah user sudah login. Dan session ID setiap kali login digenerate dan disimpan dalam sebuah cookie dalam browser user. Django mampu untuk melihat user yang terkait dengan request selama ada session ID. Kegunaan lain cookie adalah mengingat preferensi user, tracking, dan personalisasi konten yang tidak disimpan di database terkait website itu. Semua cookie belum tentu aman untuk digunakan.

Ada cookies yang digunakan untuk tracking dan iklan. Mereka adalah cookies beresiko yang tidak baik. Namun, untuk Django, kita bisa memastikan bahwa cookies yang dikirim hanyalah melalui HTTPS jika menggunakan SECURE_COOKIE sebagai contoh. 
**5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
Membaca tutorial sebelumnya. 
Memahami AuthenticationForm, UserCreationForm, HttpResponseRedirect, reverse yang dibutuhkan untuk tugas ini.
Mengimplementasikan login_user, logout_user, dan register pada views.py dengan meniru dan memodifikasi apa yang terjadi di tutorial. 
Menambahkan base.html di templates 
Menambahkan dan memodifikasi templates yang sesuai
Menambahkan baris baru mengenai User untuk foreign key model Item di models.py . 
Melakukan python manage.py makemigrations dan python manage.py migrate
Menambahkan @login_required(login_url='/login') ke beberapa function Tugas 3 




**5. Jelaskan cara kamu mengimplementasikan checklist di atas secare step-by-step**

Membuat forms.py. Mengimplementasikan ItemEntryForm sesuai dengan model Item yang ada. Tentu saja mengingat import
Mengubah template first_page.html dengan menambahkan it_entries dan beberapa baris untuk menampilkannya,
Membuat create_item_entry di views.py . Menambahkan elemen context baru untuk menampilkan item_entries di template first_page.html di first_page.
Menambahkan urls yang sesuai di urls.py 
Membuat create_item_entry.html dengan melihat form dari forms.py . Ingat csrf_token . 
Mengubah context views untuk first_page 



![Capture5.PNG](Tampilan halaman awal di lokal)

![Capture6.PNG](Tampilan login)

deploy di : 
http://vander-gerald-simplepbpeshop.pbp.cs.ui.ac.id/

dusty-penguin-fasilkomui-750583cd.koyeb.app