import datetime as dt

class ImplementasiHewanTernak:  # Interface Implementasi
    def cek_potong(self, umur_bulan: int) -> bool: pass
    def cek_kembangbiak(self, umur_bulan: int, gender: str) -> bool: pass
    def tampilkan_info(self, hewan): pass
    def sapa_hewan(self, hewan): pass

class ImplementasiSapi(ImplementasiHewanTernak):
    def cek_potong(self, umur_bulan: int) -> bool:
        return 18 <= umur_bulan <= 24

    def cek_kembangbiak(self, umur_bulan: int, gender: str) -> bool:
        batas = {"Betina": (15, 18), "Jantan": (24, 36)}.get(gender)
        return batas and batas[0] <= umur_bulan <= batas[1]

    def tampilkan_info(self, hewan):
        print(f"Sapi: Gender: {hewan.gender}, Umur: {hewan.umur_bulan}, Berat: {hewan.berat_kg}")

    def sapa_hewan(self, hewan):
        print(f"Moo! Saya Sapi berumur {hewan.umur_bulan} bulan!")

class ImplementasiKambing(ImplementasiHewanTernak):
    def cek_potong(self, umur_bulan: int) -> bool:
        return 6 <= umur_bulan <= 12

    def cek_kembangbiak(self, umur_bulan: int, gender: str) -> bool:
        batas = {"Betina": (6, 9), "Jantan": (10, 12)}.get(gender)
        return batas and batas[0] <= umur_bulan <= batas[1]

    def tampilkan_info(self, hewan):
        print(f"Kambing: Gender: {hewan.gender}, Umur: {hewan.umur_bulan}, Berat: {hewan.berat_kg}")

    def sapa_hewan(self, hewan):
        print(f"Mbeeek! Saya Kambing berumur {hewan.umur_bulan} bulan!")

class ImplementasiAyam(ImplementasiHewanTernak):
    def cek_potong(self, umur_bulan: int) -> bool:
        return 1.5 <= umur_bulan * 4 <= 2  # Konversi minggu ke bulan

    def cek_kembangbiak(self, umur_bulan: int, gender: str) -> bool:
        batas = {"Betina": (5, 6), "Jantan": (5, 6)}.get(gender)
        return batas and batas[0] <= umur_bulan <= batas[1]

    def tampilkan_info(self, hewan):
        print(f"Ayam: Gender: {hewan.gender}, Umur: {hewan.umur_bulan}, Berat: {hewan.berat_kg}")

    def sapa_hewan(self, hewan):
        print(f"Kok! Saya Ayam berumur {hewan.umur_bulan} bulan!")

class ImplementasiUnta(ImplementasiHewanTernak):
    def cek_potong(self, umur_bulan: int) -> bool:
        return 48 <= umur_bulan <= 60

    def cek_kembangbiak(self, umur_bulan: int, gender: str) -> bool:
        batas = {"Betina": (36, 48), "Jantan": (48, 60)}.get(gender)
        return batas and batas[0] <= umur_bulan <= batas[1]

    def tampilkan_info(self, hewan):
        print(f"Unta: Gender: {hewan.gender}, Umur: {hewan.umur_bulan}, Berat: {hewan.berat_kg}")

    def sapa_hewan(self, hewan):
        print(f"Hrrr! Saya Unta berumur {hewan.umur_bulan} bulan!")

class HewanTernak: # Abstraksi
    def __init__(self, jenis: str, gender: str, tanggal_lahir: dt.date, berat_kg: float, implementasi: ImplementasiHewanTernak):
        self.jenis = jenis
        self.gender = gender
        self.tanggal_lahir = tanggal_lahir
        self.umur_bulan = (dt.date.today() - tanggal_lahir).days // 30
        self.berat_kg = berat_kg
        self.implementasi = implementasi # Bridge

    def cek_potong(self) -> bool:
        return self.implementasi.cek_potong(self.umur_bulan)

    def cek_kembangbiak(self) -> bool:
        return self.implementasi.cek_kembangbiak(self.umur_bulan, self.gender)

    def tampilkan_info(self):
        self.implementasi.tampilkan_info(self)

    def sapa_hewan(self):
        self.implementasi.sapa_hewan(self)

class Sapi(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Sapi", gender, tanggal_lahir, berat_kg, ImplementasiSapi())

class Kambing(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Kambing", gender, tanggal_lahir, berat_kg, ImplementasiKambing())

class Ayam(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Ayam", gender, tanggal_lahir, berat_kg, ImplementasiAyam())

class Unta(HewanTernak):
    def __init__(self, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Unta", gender, tanggal_lahir, berat_kg, ImplementasiUnta())

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
    hewan_class = hewan_dict.get(jenis_hewan)
    hewan = hewan_class(gender, tanggal_lahir, berat)

    hewan.tampilkan_info()
    hewan.sapa_hewan()
    print("Siap disembelih?", hewan.cek_potong())
    print("Siap berkembang biak?", hewan.cek_kembangbiak())

except ValueError as e:
    print(f"Input tidak valid: {e}")