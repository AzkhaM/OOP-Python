import datetime as dt

class HewanTernak:
    def __init__(self, jenis, gender=None, tanggal_lahir=None, berat_kg=None):
        self.jenis = jenis
        self.gender = gender
        self.tanggal_lahir = tanggal_lahir
        self.umur_bulan = None
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

class HewanTernakBuilder:
    def __init__(self, jenis):
        self.hewan = HewanTernak(jenis)

    def dengan_gender(self, gender):
        self.hewan.gender = gender
        return self

    def dengan_tanggal_lahir(self, tahun, bulan, tanggal):
        self.hewan.tanggal_lahir = dt.date(tahun, bulan, tanggal)
        self.hewan.umur_bulan = (dt.date.today() - self.hewan.tanggal_lahir).days // 30
        return self

    def dengan_berat(self, berat_kg):
        self.hewan.berat_kg = berat_kg
        return self

    def dengan_info_potong(self, min_potong, max_potong):
        self.hewan.info_potong = {"min": min_potong, "max": max_potong}
        return self

    def dengan_info_kembangbiak(self, info_kembangbiak):
        self.hewan.info_kembangbiak = info_kembangbiak
        return self

    def bangun(self):
        return self.hewan

class Sapi(HewanTernak):
    def __init__(self, gender, tahun, bulan, tanggal, berat_kg):
        hewan = HewanTernakBuilder("Sapi") \
            .dengan_gender(gender) \
            .dengan_tanggal_lahir(tahun, bulan, tanggal) \
            .dengan_berat(berat_kg) \
            .dengan_info_potong(18, 24) \
            .dengan_info_kembangbiak({"Betina": {"min": 15, "max": 18}, "Jantan": {"min": 24, "max": 36}}) \
            .bangun()
        self.__dict__.update(hewan.__dict__)

class Kambing(HewanTernak):
    def __init__(self, gender, tahun, bulan, tanggal, berat_kg):
        hewan = HewanTernakBuilder("Kambing") \
            .dengan_gender(gender) \
            .dengan_tanggal_lahir(tahun, bulan, tanggal) \
            .dengan_berat(berat_kg) \
            .dengan_info_potong(6, 12) \
            .dengan_info_kembangbiak({"Betina": {"min": 6, "max": 9}, "Jantan": {"min": 10, "max": 12}}) \
            .bangun()
        self.__dict__.update(hewan.__dict__)

class Ayam(HewanTernak):
    def __init__(self, gender, tahun, bulan, tanggal, berat_kg):
        hewan = HewanTernakBuilder("Ayam") \
            .dengan_gender(gender) \
            .dengan_tanggal_lahir(tahun, bulan, tanggal) \
            .dengan_berat(berat_kg) \
            .dengan_info_potong(1.5 / 4, 2 / 4) \
            .dengan_info_kembangbiak({"Betina": {"min": 5, "max": 6}, "Jantan": {"min": 5, "max": 6}}) \
            .bangun()
        self.__dict__.update(hewan.__dict__)

class Unta(HewanTernak):
    def __init__(self, gender, tahun, bulan, tanggal, berat_kg):
        hewan = HewanTernakBuilder("Unta") \
            .dengan_gender(gender) \
            .dengan_tanggal_lahir(tahun, bulan, tanggal) \
            .dengan_berat(berat_kg) \
            .dengan_info_potong(48, 60) \
            .dengan_info_kembangbiak({"Betina": {"min": 36, "max": 48}, "Jantan": {"min": 48, "max": 60}}) \
            .bangun()
        self.__dict__.update(hewan.__dict__)

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
    hewan = hewan_class(gender, tahun, bulan, tanggal, berat)
    
    hewan.tampilkan_info()
    hewan.sapa_hewan()
    print("Siap disembelih?", hewan.cek_potong())
    print("Siap berkembang biak?", hewan.cek_kembangbiak())
    
except ValueError as e:
    print(f"Input tidak valid: {e}")