import datetime as dt

class HewanTernak:
    def __init__(self, jenis: str, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        self.jenis = jenis
        self.gender = gender
        self.tanggal_lahir = tanggal_lahir
        self.umur_bulan = (dt.date.today() - tanggal_lahir).days // 30  
        self.berat_kg = berat_kg
        self.info_potong = {}
        self.info_kembangbiak = {}

    def cek_potong(self) -> bool:
        min_potong = self.info_potong.get("min", float('inf'))
        max_potong = self.info_potong.get("max", -float('inf'))
        return min_potong <= self.umur_bulan <= max_potong

    def cek_kembangbiak(self) -> bool:
        batas_kembang = self.info_kembangbiak.get(self.gender, {})
        min_kembang = batas_kembang.get("min", float('inf'))
        max_kembang = batas_kembang.get("max", -float('inf'))
        return min_kembang <= self.umur_bulan <= max_kembang
    
    def tampilkan_info(self):
        print(f"Jenis: {self.jenis}, Gender: {self.gender}, Umur: {self.umur_bulan} bulan, Berat: {self.berat_kg} kg")

    def sapa_hewan(self):
        print(f"Halo! Saya seekor {self.jenis} dan saya berumur {self.umur_bulan} bulan!")

class Sapi(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Sapi", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 18, "max": 24}  
        self.info_kembangbiak = {"Betina": {"min": 15, "max": 18}, "Jantan": {"min": 24, "max": 36}}

class Kambing(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Kambing", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 6, "max": 12}
        self.info_kembangbiak = {"Betina": {"min": 6, "max": 9}, "Jantan": {"min": 10, "max": 12}}

class Ayam(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Ayam", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 1.5 / 4, "max": 2 / 4}  # Minggu ke bulan
        self.info_kembangbiak = {"Betina": {"min": 5, "max": 6}, "Jantan": {"min": 5, "max": 6}}

class Unta(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Unta", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 48, "max": 60}  
        self.info_kembangbiak = {"Betina": {"min": 36, "max": 48}, "Jantan": {"min": 48, "max": 60}}

# Menu pemilihan
hewan_dict = {
    "1": "Ayam",
    "2": "Kambing",
    "3": "Sapi",
    "4": "Unta"
}

jenis_hewan = None
while not jenis_hewan:
    print("Pilih jenis hewan:")
    for key, value in hewan_dict.items():
        print(f"{key}. {value}")
    pilihan = input("Masukkan angka pilihan (1-4): ")
    jenis_hewan = hewan_dict.get(pilihan)
    if not jenis_hewan:
        print("Pilihan tidak valid, coba lagi.")

gender = None
while not gender:
    gender_input = input("Masukkan gender hewan (Betina/Jantan): ").capitalize()
    if gender_input in ["Betina", "Jantan"]:
        gender = gender_input
    else:
        print("Gender tidak valid, coba lagi.")

try:
    tahun = int(input("Masukkan tahun lahir: "))
    bulan = int(input("Masukkan bulan lahir (1-12): "))
    tanggal = int(input("Masukkan tanggal lahir (1-31): "))
    berat = float(input("Masukkan berat hewan (kg): "))

    if not (1 <= bulan <= 12) or not (1 <= tanggal <= 31) or berat <= 0:
        raise ValueError("Tanggal/Bulan/berat tidak valid!")

    tanggal_lahir = dt.date(tahun, bulan, tanggal)
    hewan_class = {"Ayam": Ayam, "Kambing": Kambing, "Sapi": Sapi, "Unta": Unta}.get(jenis_hewan)
    hewan = hewan_class(gender, tanggal_lahir, berat)
    
    hewan.tampilkan_info()
    hewan.sapa_hewan()
    print("Siap disembelih?", hewan.cek_potong())
    print("Siap berkembang biak?", hewan.cek_kembangbiak())
    
except ValueError as e:
    print(f"Input tidak valid: {e}")
