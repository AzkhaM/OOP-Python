import datetime as dt

class HewanTernak:
    def __init__(ternak, jenis: str, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        ternak.jenis = jenis
        ternak.gender = gender
        ternak.tanggal_lahir = tanggal_lahir
        ternak.umur_bulan = (dt.date.today() - tanggal_lahir).days // 30  
        ternak.berat_kg = berat_kg
        ternak.info_potong = {}
        ternak.info_kembangbiak = {}

    def cek_potong(ternak) -> bool:
        min_potong, max_potong = ternak.info_potong.get("min", 0), ternak.info_potong.get("max", float('inf'))
        return min_potong <= ternak.umur_bulan <= max_potong

    def cek_kembangbiak(ternak) -> bool:
        batas_kembang = ternak.info_kembangbiak.get(ternak.gender, {})
        min_kembang, max_kembang = batas_kembang.get("min", 0), batas_kembang.get("max", float('inf'))
        return min_kembang <= ternak.umur_bulan <= max_kembang
    
    def tampilkan_info(ternak):
        print(f"Jenis: {ternak.jenis}, Gender: {ternak.gender}, Umur: {ternak.umur_bulan} bulan, Berat: {ternak.berat_kg} kg")

    def sapa_hewan(ternak):
        print(f"Halo! Saya seekor {ternak.jenis} dan saya berumur {ternak.umur_bulan} bulan!")

class Sapi(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Sapi", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 18, "max": 24}  # Dalam bulan
        ternak.info_kembangbiak = {"Betina": {"min": 15, "max": 18}, "Jantan": {"min": 24, "max": 36}}

class Kambing(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Kambing", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 6, "max": 12}
        ternak.info_kembangbiak = {"Betina": {"min": 6, "max": 9}, "Jantan": {"min": 10, "max": 12}}

class Ayam(HewanTernak):
    def __init__(ternak, gender: str, tanggal_lahir: dt.date, berat_kg: float):
        super().__init__("Ayam", gender, tanggal_lahir, berat_kg)
        ternak.info_potong = {"min": 1.5/4, "max": 2/4}  # Minggu dikonversi ke bulan
        ternak.info_kembangbiak = {"Betina": {"min": 5, "max": 6}, "Jantan": {"min": 5, "max": 6}}

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
    
    ternak = {"Sapi": Sapi, "Kambing": Kambing, "Ayam": Ayam, "Unta": Unta}.get(jenis, None)
    
    if ternak:
        ternak = ternak(gender, tanggal_lahir, berat)
        ternak.tampilkan_info()
        ternak.sapa_hewan()
        print("Siap disembelih?", ternak.cek_potong())
        print("Siap berkembang biak?", ternak.cek_kembangbiak())
    else:
        print("Jenis hewan tidak valid.")
