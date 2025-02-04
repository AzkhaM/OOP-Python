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
        min_potong, max_potong = self.info_potong.get("min", 0), self.info_potong.get("max", float('inf'))
        return min_potong <= self.umur_bulan <= max_potong
    
    def cek_kembangbiak(self) -> bool:
        batas_kembang = self.info_kembangbiak.get(self.gender, {})
        min_kembang, max_kembang = batas_kembang.get("min", 0), batas_kembang.get("max", float('inf'))
        return min_kembang <= self.umur_bulan <= max_kembang
    
    def tampilkan_info(self):
        print(f"Jenis: {self.jenis}, Gender: {self.gender}, Umur: {self.umur_bulan} bulan, Berat: {self.berat_kg} kg")
    
    def sapa_hewan(self):
        print(f"Halo! Saya seekor {self.jenis} dan saya berumur {self.umur_bulan} bulan!")

class Sapi(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Sapi", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 18 * 12, "max": 24 * 12}  # Dalam bulan
        self.info_kembangbiak = {"Betina": {"min": 15 * 12, "max": 18 * 12}, "Jantan": {"min": 2 * 12, "max": 3 * 12}}

class Kambing(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Kambing", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 6 * 12, "max": 12 * 12}
        self.info_kembangbiak = {"Betina": {"min": 6 * 12, "max": 9 * 12}, "Jantan": {"min": 10 * 12, "max": 12 * 12}}

class Ayam(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Ayam", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 6 * 4, "max": 8 * 4}  # Minggu ke bulan
        self.info_kembangbiak = {"Betina": {"min": 5 * 12, "max": 6 * 12}, "Jantan": {"min": 5 * 12, "max": 6 * 12}}

class Unta(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Unta", gender, tanggal_lahir, berat_kg)
        self.info_potong = {"min": 4 * 12, "max": 5 * 12}
        self.info_kembangbiak = {"Betina": {"min": 3 * 12, "max": 4 * 12}, "Jantan": {"min": 4 * 12, "max": 5 * 12}}

# Input dari user
if __name__ == "__main__":
    jenis = input("Masukkan jenis hewan (Sapi/Kambing/Ayam/Unta): ").capitalize()
    gender = input("Masukkan gender hewan (Betina/Jantan): ").capitalize()
    tahun = int(input("Masukkan tahun lahir: "))
    bulan = int(input("Masukkan bulan lahir: "))
    tanggal = int(input("Masukkan tanggal lahir: "))
    berat = float(input("Masukkan berat hewan (kg): "))
    
    tanggal_lahir = dt.date(tahun, bulan, tanggal)
    
    if jenis == "Sapi":
        hewan = Sapi(gender, tanggal_lahir, berat)
    elif jenis == "Kambing":
        hewan = Kambing(gender, tanggal_lahir, berat)
    elif jenis == "Ayam":
        hewan = Ayam(gender, tanggal_lahir, berat)
    elif jenis == "Unta":
        hewan = Unta(gender, tanggal_lahir, berat)
    else:
        print("Jenis hewan tidak valid.")
        exit()
    
    hewan.tampilkan_info()
    print("Siap disembelih?", hewan.cek_potong())
    print("Siap berkembang biak?", hewan.cek_kembangbiak())