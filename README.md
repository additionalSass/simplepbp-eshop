## Informasi

Nama : Vander Gerald Sukandi

NPM  : 1906350603

## Checklist untuk Tugas PBP

**1. Membuat Proyek Django Baru**

Buka command prompt dan menjalankan perintah berikut:

django-admin startproject simplepbpshop

Perintah ini membuat sebuah folder baru dengan struktur proyek Django.

**2. Membuat Aplikasi 'main'**

Masuk ke folder proyek yang baru dibuat:

```
cd simplepbpshop
```

Kemudian, buat aplikasi baru bernama 'main':

python manage.py startapp main

**3. Routing untuk Aplikasi 'main'**

Buka file `simplepbpshop/urls.py` dan menambahkan baris berikut di dalam list `urlpatterns`:

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Tambahkan baris ini
]
```

**4. Membuat Model `Item`**

Buka file `main/models.py` dan menambahkan kode berikut:

```python
import uuid
from django.db import models
from django.core.validators import MinValueValidator

class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30, unique=True)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(default='Default')
    stocks = models.IntegerField(validators=[MinValueValidator(0)])
    recom_status_last_update = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
```

Dibuatlah model `Item` dengan atribut 'name', 'price', 'id', dan beberapa atribut lain dengan Field-Field berbeda. MinValueValidator di sini membuat nilai-nilai di tas angka tertentu saja yang valid untuk IntegerField.

**5. Fungsi Pertama di `views.py` dan Template HTML**

Buka file `main/views.py` dan menambahkan kode berikut:

```python
from django.shortcuts import render, redirect 

def first_page(request):
    context = {'application':'Simple PBP E-Shop','app':'main','name':'Vander Gerald Sukandi','NPM':'1906350603','class':'PBP A'}
    return render(request,'first_page.html', context)
```

Buat file `main/templates/first_page.html`. Perhatikan bahwa hal-hal di dalam {{ }} akan diubah sesuai dengan context dalam views.

```html
...

<h1>{{ application }}</h1>

<h2>Welcome to {{ app }}</h2>

<h3>My Student Information:</h3>
<ul>
    <li>Name: {{ name }}</li>
    <li>Student ID: {{ NPM }}</li>
    <li>Class: {{ class }}</li>
</ul>
</body>
...

```

**6. Routing di `urls.py` App `main`**

Buat file `main/urls.py` dan tambahkan kode berikut:

```python
from django.urls import path
from main.views import first_page
app_name = 'main'

urlpatterns = [
    path('', first_page, name='first_page'),
]
```

**7. Deployment ke pws DAN koyeb**

Lakukan git add ., git commit -m "message" , git push pwss master (dalam kasus ini diasumsikan bahwa remote sudah ditentukan). Perhatikan bahwa dalam `settings.py` , 'vander-gerald-simplepbpeshop.pbp.cs.ui.ac.id/' perlu diketik sebagai salah satu elemen ALLOWED_HOSTS.

Setting beberapa hal di Koyeb in case pws bermasalah. Linknya :  https://dusty-penguin-fasilkomui-750583cd.koyeb.app/

**8. Membuat `README.md`**

Buat file `README.md` di root folder proyek dan menyertakan tautan ke aplikasi yang telah di-deploy. 

**Jawaban Pertanyaan di `README.md`**

**a. Implementasi Checklist Step-by-Step (Sudah Dilakukan Diatas)**

**b. Bagan Request-Response dan Kaitan Antar Komponen**

```            
                      request
+-------------------+       +----------------------+     +-------------------+     +-------------------+
| Client (Browser)  |-----> |simplepbpshop/urls.py | --> |    main/urls.py   | --> |   main/views.py   | 
+-------------------+       +----------------------+     +-------------------+     +-------------------+
                                ^                               ^                        |
                                |                               |                        |
                                +-------------------------------+                        | Render HTML dengan data
                                                                                         | dari context yang didapatkan dalam function yang terkait
                                                                                         v
                                                                                 +-------------------+
                                                                                 |  main/templates   |
                                                                                 +-------------------+
                                                                                         |
                                                                                         | response 
                                                                                         v
                                                                                 +-------------------+
                                                                                 |  Client (Browser) |
                                                                                 +-------------------+
```

**Penjelasan:**

1. **Client (Browser)** mengirimkan HTTP request ke server.
2. **`simplepbpshop/urls.py`** (root URL configuration) akan menerima request dan mencari URL pattern yang cocok. Pada kasus ini, request akan di-routing ke `main/urls.py`.
3. **`main/urls.py`** (URL configuration aplikasi `main`) mencari URL pattern yang cocok. Jika pattern cocok, request diarahkan ke fungsi terkait di `main/views.py`.
4. **`main/views.py`** (application logic dari app 'main') memproses request, (jika di-perlukan dan ada import) akan mengambil data dari **`main/models.py`** (terkait dengan database ORM dalam Django), dan menyiapkan `context` untuk template. 
5. **`main/views.py`** me-render template HTML tertentu yang ada di **`main/templates`** sesuai dengan data yang disediakan dari `context`.
6. Django melakukan response. HTML yang telah di-render dikirimkan kembali ke **Client (Browser)**.

**c. Virtual Environment**

Virtual environment bertujuan untuk mengisolasi dependensi proyek Python. Dengan virtual environment, setiap proyek dapat memiliki set library dan versi Python berbeda yang umumnya disesuaikan dengan requirements.txt untuk setiap proyek yang berbeda.

**Tiga Alasan Orang Menggunakan Virtual Environment**

- **Mencegah Konflik Dependensi:** Proyek yang berbeda bisa jadi memakai versi library yang berbeda. Virtual environment memastikan bahwa setiap proyek menggunakan library yang tepat.
- **Mempermudah Reproduksi Lingkungan:** Jika kita sudah mendefinisikan dependensi di file `requirements.txt`, kita dapat mereproduksi lingkungan development Python itu di mesin lain.
- **Menjaga Kebersihan Sistem:** Virtual environment mencegah library proyek memengaruhi sistem Python global.

**Apakah Kita Bisa Membuat Aplikasi Django Tanpa Virtual Environment?**

Kita bisa, tetapi tidak disarankan. Tanpa virtual environment, kita berisiko mengalami konflik dependensi dan kesulitan dalam mereproduksi web development environment yang diperlukan.

**d. MVC, MVT, MVVM**

Ketiga pola ini adalah software design pattern yang bertujuan untuk memisahkan concerns (Ingat prinsip separation of concerns!) dalam aplikasi yang tidak terlalu sederhana:

**1. MVC (Model-View-Controller)**

- **Model:** Umumnya mengolah dan melibatkan data dan business logic.
- **View:** Menampilkan data kepada pengguna dan menerima input dari pengguna.
- **Controller:** Menerima input pengguna, memprosesnya, update hal-hal untuk model, dan memilih view yang tepat.

**2. MVT (Model-View-Template)**

- **Model:** Sama seperti MVC.
- **View:** Bertugas memproses request, mengambil data dari model, dan memanggil template. View ini pada Django menjadi seperti Controller di MVC. 
- **Template:** Menampilkan data ke pengguna (mirip dengan View di MVC).

**Perbedaan MVC dan MVT:**

Pada MVC, Controller memilih View yang akan ditampilkan, sedangkan pada MVT yang dimiliki oleh Django, View (fungsi di `views.py`) lah yang memilih template yang akan di-render. 

**3. MVVM (Model-View-ViewModel)**

- **Model:** Sama seperti MVC.
- **View:** Menampilkan data dan menerima input. View terhubung ke ViewModel melalui data binding. Data binding menghubungkan data dari Model dan elemen UI dari ViewModel.
- **ViewModel:** Menyediakan data yang dibutuhkan oleh View dan menangani interaksi pengguna.

**Perbedaan MVVM dengan MVC/MVT:**

MVVM menekankan pada data binding antara View dan ViewModel yang membuat pemisahan yang lebih jelas antara User Interface dan application logic.

Django menggunakan pola MVT yang mana framework ini sendiri yang bertindak sebagai Controller.