# **LAPORAN PENUGASAN OOP - PYTHON**

## **Masalah yang Diangkat**
Manajemen peternakan yang efisien merupakan faktor penting dalam meningkatkan produktivitas hewan ternak. Namun, banyak peternak masih mengelola usaha mereka secara sederhana, tanpa pemahaman yang cukup tentang manajemen pakan, kesehatan hewan, serta penentuan waktu yang tepat untuk pengembangbiakan dan penyembelihan ternak. Hal ini berdampak pada kurang optimalnya hasil produksi peternakan.

Sumber referensi: [NA Ternak Ruminansia](https://ppid.boyolali.go.id/ft_infopublik/showdoc/7.%20NA%20Ternak%20Ruminansia.pdf)

## **Solusi**
Untuk membantu peternak dalam mengambil keputusan terkait hewan ternak mereka, program ini dirancang untuk:
- Memberikan informasi apakah suatu hewan sudah cukup umur untuk dikembangbiakkan.
- Menentukan apakah suatu hewan telah mencapai usia yang layak untuk disembelih.

Program ini dibuat dengan pendekatan Pemrograman Berorientasi Objek (OOP) menggunakan bahasa Python. Hewan ternak yang didukung dalam program ini meliputi:
- **Sapi**
- **Kambing**
- **Ayam**
- **Unta**

## **Class Diagram**

![class diagram](https://github.com/user-attachments/assets/4b2ca69b-640b-450f-9e95-55e4567b8f20)

_Class diagram ini menunjukkan struktur utama dari program, termasuk hubungan antara kelas induk dan kelas turunannya._

## **Use case Diagram**

![Diagram Tanpa Judul drawio (2)](https://github.com/user-attachments/assets/d18b2bb4-4b6c-4561-afe7-bf2f418d45e8)

_Use case diagram ini menggambarkan bagaimana pengguna (peternak) dapat berinteraksi dengan sistem._

## **Sequence Diagram**

![Screenshot 2025-02-05 013802](https://github.com/user-attachments/assets/c1f9efcc-f63b-46b4-9a06-a89c130c7b48)

_Sequence diagram ini menunjukkan alur eksekusi program dalam menentukan keputusan terkait hewan ternak._

## **Kode Program**
Kode program yang telah dibuat menggunakan konsep OOP dapat dilihat pada repository ini. Berikut adalah gambaran umum dari kode yang telah diimplementasikan:
- **Kelas HewanTernak**: Kelas dasar yang mencakup atribut umum seperti jenis hewan, gender, tanggal lahir, umur dalam bulan, dan berat badan.
- **Kelas Sapi, Kambing, Ayam, dan Unta**: Kelas turunan yang memiliki aturan spesifik mengenai usia minimal dan maksimal untuk penyembelihan serta pengembangbiakan.
- **Fungsi cek_potong()**: Mengecek apakah hewan sudah layak untuk disembelih.
- **Fungsi cek_kembangbiak()**: Mengecek apakah hewan sudah cukup umur untuk berkembang biak.
- **Fungsi tampilkan_info()**: Menampilkan informasi hewan ternak.

