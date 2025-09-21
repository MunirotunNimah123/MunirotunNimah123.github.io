# 🚀 Latihan API dengan Flask
Project ini dibuat untuk latihan **UTS** dengan implementasi **REST API** menggunakan **Flask**.  
Mendukung operasi **CRUD**:
- **GET** → Menampilkan data
- **POST** → Menambah data
- **PUT** → Mengubah data sepenuhnya
- **PATCH** → Mengubah sebagian data
- **DELETE** → Menghapus data

---

## 📂 Struktur Folder
latihan_api/
│
├── app.py # File utama API
└── README.md # Dokumentasi project

yaml
Copy code

---

## 🛠️ Persiapan Awal
### 1. Install Python
Pastikan Python sudah terpasang di perangkat.  
Cek versi Python:
```bash
python --version
Jika belum terinstall, download di Python.org.

2. Install Flask
Buka terminal/cmd di folder latihan_api lalu jalankan:

bash
Copy code
pip install flask
▶️ Menjalankan API
Pastikan kamu berada di folder project:

bash
Copy code
cd latihan_api
Jalankan perintah berikut:

bash
Copy code
python app.py
Jika berhasil, akan muncul pesan:

csharp
Copy code
* Running on http://127.0.0.1:5000
Jangan tutup terminal selama API dijalankan.
Jika ingin berhenti, tekan CTRL + C.

🌐 Endpoint yang Tersedia
METHOD	ENDPOINT	DESKRIPSI
GET	/tasks	Ambil semua data
GET	/tasks/<id>	Ambil data berdasarkan ID
POST	/tasks	Tambah data baru
PUT	/tasks/<id>	Update seluruh data berdasarkan ID
PATCH	/tasks/<id>	Update sebagian data berdasarkan ID
DELETE	/tasks/<id>	Hapus data berdasarkan ID

💻 Cara Uji API Menggunakan Postman
1. Install Postman
Download Postman di https://www.postman.com/downloads/.

2. Uji Endpoint
Gunakan URL dasar:

cpp
Copy code
http://127.0.0.1:5000
METHOD	URL	BODY (JSON)
GET	/tasks	-
GET	/tasks/1	-
POST	/tasks	json { "judul": "Belajar API", "status": "belum selesai" }
PUT	/tasks/3	json { "judul": "Update", "status": "selesai" }
PATCH	/tasks/3	json { "status": "belum selesai" }
DELETE	/tasks/3	-

Langkah Uji di Postman
GET (Semua Data)

Method: GET

URL: http://127.0.0.1:5000/tasks

Klik Send

POST (Tambah Data)

Method: POST

URL: http://127.0.0.1:5000/tasks

Tab Body → raw → JSON

Input JSON:

json
Copy code
{
  "judul": "Belajar API",
  "status": "belum selesai"
}
Klik Send

PUT (Update Semua Data)

Method: PUT

URL: http://127.0.0.1:5000/tasks/1

Body:

json
Copy code
{
  "judul": "Belajar Flask Lanjutan",
  "status": "selesai"
}
Klik Send

PATCH (Update Sebagian Data)

Method: PATCH

URL: http://127.0.0.1:5000/tasks/1

Body:

json
Copy code
{
  "status": "belum selesai"
}
Klik Send

DELETE (Hapus Data)

Method: DELETE

URL: http://127.0.0.1:5000/tasks/1

Klik Send

📝 Contoh Hasil JSON
Berikut contoh hasil saat melakukan GET:

json
Copy code
[
  {
    "id": 1,
    "judul": "Belajar Flask",
    "status": "belum selesai"
  },
  {
    "id": 2,
    "judul": "Kerjakan UTS",
    "status": "belum selesai"
  }
]
🐞 Troubleshooting
Masalah	Penyebab	Solusi
Method Not Allowed	Salah memilih method di Postman	Pastikan pilih GET/POST/PUT/PATCH/DELETE yang sesuai
Internal Server Error	Ada error di kode Python	Lihat terminal untuk detail error
Tidak bisa akses 127.0.0.1	Server belum dijalankan	Jalankan python app.py