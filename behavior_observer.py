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
        self._observers = []  # Daftar observer

    def attach(self, observer):  # Menambahkan observer
        self._observers.append(observer)

    def detach(self, observer):  # Menghapus observer
        self._observers.remove(observer)

    def notify_observers(self, event, data=None):  # Memberi tahu observer
        for observer in self._observers:
            observer.update(event, data)

    # Setter untuk atribut yang perlu diamati
    def set_berat_kg(self, berat_kg):
        self.berat_kg = berat_kg
        self.notify_observers("berat_berubah", berat_kg)  # Notifikasi

    def set_info_potong(self, info_potong):
        self.info_potong = info_potong
        self.notify_observers("info_potong_berubah", info_potong)

    def set_info_kembangbiak(self, info_kembangbiak):
        self.info_kembangbiak = info_kembangbiak
        self.notify_observers("info_kembangbiak_berubah", info_kembangbiak)

    # ... (method lainnya tetap sama)

class Observer:  # Interface Observer
    def update(self, event, data=None):
        pass

class Peternak(Observer):  # Contoh Observer
    def update(self, event, data=None):
        if event == "berat_berubah":
            print(f"Peternak: Berat hewan berubah menjadi {data} kg.")
        # ... (reaksi terhadap event lainnya)

class Penjual(Observer):  # Contoh Observer
    def update(self, event, data=None):
        if event == "info_potong_berubah":
            print(f"Penjual: Info potong hewan berubah menjadi {data}.")
        # ... (reaksi terhadap event lainnya)

# Kelas anak Sapi, Kambing, Ayam, Unta
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

    peternak = Peternak()
    penjual = Penjual()

    hewan.attach(peternak)  # Daftarkan peternak sebagai observer
    hewan.attach(penjual)  # Daftarkan penjual sebagai observer

    hewan.set_berat_kg(250)  # Contoh perubahan berat, akan memicu notifikasi
    hewan.set_info_potong({"min": 20, "max": 30}) # contoh perubahan info potong, akan memicu notifikasi

    hewan.tampilkan_info()
    hewan.sapa_hewan()
    print("Siap disembelih?", hewan.cek_potong())
    print("Siap berkembang biak?", hewan.cek_kembangbiak())

except ValueError as e:
    print(f"Input tidak valid: {e}")