
import datetime as dt

"""=======================================class parent=============================================================
Kelas HewanTernak adalah kelas induk yang merepresentasikan semua hewan ternak.

Atribut:
- jenis (str): Jenis hewan (misalnya: Sapi, Kambing, Ayam, Unta).
- gender (str): Jenis kelamin hewan (Betina/Jantan).
- tanggal_lahir (datetime.date): Tanggal lahir hewan.
- umur_bulan (int): Umur hewan dalam bulan, dihitung dari tanggal lahir.
- berat_kg (float): Berat hewan dalam kilogram.
- info_potong (dict): Rentang usia hewan yang boleh disembelih.
- info_kembangbiak (dict): Rentang usia hewan yang bisa berkembang biak.

Metode:
- __init__(): Konstruktor untuk inisialisasi objek.
- cek_potong(): Mengecek apakah hewan sudah layak disembelih berdasarkan usia.
- cek_kembangbiak(): Mengecek apakah hewan sudah bisa berkembang biak berdasarkan usia dan jenis kelamin.
- tampilkan_info(): Menampilkan informasi lengkap tentang hewan.
- sapa_hewan(): Menyapa hewan dengan menampilkan jenis dan umurnya.
"""  
class HewanTernak:
    def __init__(ternak, jenis: str, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        ternak.jenis = jenis
        ternak.gender = gender
        ternak.tanggal_lahir = tanggal_lahir
        ternak.umur_bulan = (dt.date.today() - tanggal_lahir).days // 30  
        ternak.berat_kg = berat_kg
        ternak.info_potong = {}
        ternak.info_kembangbiak = {}

"""=======================================fungsi cek_potong=============================================================
Fungsi ini digunakan untuk mengecek apakah hewan sudah siap untuk disembelih.

Return:
- (bool) True jika umur hewan berada dalam rentang umur yang diperbolehkan untuk disembelih.
- (bool) False jika umur hewan belum cukup atau sudah melewati batas usia pemotongan.
"""     
    def cek_potong(ternak) -> bool:
        min_potong, max_potong = ternak.info_potong.get("min", 0), ternak.info_potong.get("max", float('inf'))
        return min_potong <= ternak.umur_bulan <= max_potong

"""=======================================fungsi cek_kembangbiak=============================================================
Fungsi ini digunakan untuk mengecek apakah hewan sudah bisa berkembang biak.

Return:
- (bool) True jika umur hewan berada dalam rentang usia berkembang biak berdasarkan jenis kelamin.
- (bool) False jika umur hewan belum cukup atau sudah melewati batas usia berkembang biak.
"""      
    def cek_kembangbiak(ternak) -> bool:
        batas_kembang = ternak.info_kembangbiak.get(ternak.gender, {})
        min_kembang, max_kembang = batas_kembang.get("min", 0), batas_kembang.get("max", float('inf'))
        return min_kembang <= ternak.umur_bulan <= max_kembang

"""=======================================fungsi tampilkan_info=============================================================
Fungsi ini digunakan untuk menampilkan informasi dasar tentang hewan ternak.

Output:
- Menampilkan jenis, gender, umur dalam bulan, dan berat dalam kg.
"""      
    def tampilkan_info(ternak):
        print(f"Jenis: {ternak.jenis}, Gender: {ternak.gender}, Umur: {ternak.umur_bulan} bulan, Berat: {ternak.berat_kg} kg")
    
"""=======================================fungsi sapa_hewan=============================================================
Fungsi ini digunakan untuk menyapa hewan ternak.

Output:
- Menampilkan pesan sapaan berdasarkan jenis dan umur hewan.
"""    
    def sapa_hewan(ternak):
        print(f"Halo! Saya seekor {ternak.jenis} dan saya berumur {ternak.umur_bulan} bulan!")

"""=======================================class child Sapi=============================================================
Kelas Sapi adalah turunan dari HewanTernak yang merepresentasikan sapi.

Umur disembelih: 18-24 bulan
Umur dikembangbiakkan:
- Betina: 15-18 bulan
- Jantan: 2-3 tahun
"""
class Sapi(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Sapi", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 18, "max": 24}  # Dalam bulan
        ternak.info_kembangbiak = {"Betina": {"min": 15, "max": 18}, "Jantan": {"min": 24, "max": 36}}

"""=======================================class child Kambing=============================================================
Kelas Kambing adalah turunan dari HewanTernak yang merepresentasikan kambing.

Umur disembelih: 6-12 bulan
Umur dikembangbiakkan:
- Betina: 6-9 bulan
- Jantan: 10-12 bulan
"""
class Kambing(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Kambing", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 6, "max": 12}
        ternak.info_kembangbiak = {"Betina": {"min": 6, "max": 9}, "Jantan": {"min": 10, "max": 12}}

"""=======================================class child Ayam=============================================================
Kelas Ayam adalah turunan dari HewanTernak yang merepresentasikan ayam.

Umur disembelih: 6-8 minggu (konversi ke bulan)
Umur dikembangbiakkan:
- Betina: 5-6 bulan
- Jantan: 5-6 bulan
"""
class Ayam(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Ayam", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 1.5/, "max": 2/4}  # Minggu dikonversi ke bulan
        ternak.info_kembangbiak = {"Betina": {"min": 5, "max": 6}, "Jantan": {"min": 5, "max": 6}}

"""=======================================class child Unta=============================================================
Kelas Unta adalah turunan dari HewanTernak yang merepresentasikan unta.

Umur disembelih: 4-5 tahun
Umur dikembangbiakkan:
- Betina: 3-4 tahun
- Jantan: 4-5 tahun
"""
class Unta(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Unta", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 48, "max": 60}  # Tahun dikonversi ke bulan
        ternak.info_kembangbiak = {"Betina": {"min": 36, "max": 48}, "Jantan": {"min": 48, "max": 60}}

# Input dari user
if __name__ == "__main__":
    jenis = input("Masukkan jenis hewan (Sapi/Kambing/Ayam/Unta): ").capitalize()
    gender = input("Masukkan gender hewan (Betina/Jantan): ").capitalize()
    tahun = int(input("Masukkan tahun lahir: "))
    bulan = int(input("Masukkan bulan lahir: "))
    tanggal = int(input("Masukkan tanggal lahir: "))
    berat = float(input("Masukkan berat hewan (kg): "))

    tanggal_lahir = dt.date(tahun, bulan, tanggal)
    
    hewan = {"Sapi": Sapi, "Kambing": Kambing, "Ayam": Ayam, "Unta": Unta}.get(jenis, None)
    
    if hewan:
        hewan = hewan(gender, tanggal_lahir, berat)
        hewan.tampilkan_info()
        hewan.sapa_hewan()
        print("Siap disembelih?", hewan.cek_potong())
        print("Siap berkembang biak?", hewan.cek_kembangbiak())
    else:
        print("Jenis hewan tidak valid.")

