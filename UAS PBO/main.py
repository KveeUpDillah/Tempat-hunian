# main.py
from datetime import date

# Models
from models.area import Area

# Repositories
from repositories.area_repo import AreaRepository
from repositories.hunian_repo import HunianRepository
from repositories.registrasi_repo import RegistrasiRepository

# Services
from services.hunian_service import HunianService
from services.registrasi_service import RegistrasiService


def main():
    print("=== SISTEM MANAJEMEN HUNIAN ===")

    # ==============================
    # INISIALISASI REPOSITORY
    # ==============================
    area_repo = AreaRepository()
    hunian_repo = HunianRepository()
    registrasi_repo = RegistrasiRepository()

    # ==============================
    # INISIALISASI SERVICE
    # ==============================
    hunian_service = HunianService(hunian_repo)
    registrasi_service = RegistrasiService(registrasi_repo)

    # ==============================
    # DATA AREA
    # ==============================
    area1 = Area(
        id_area=1,
        nama="Area Asrama Putra",
        kapasitas=100,
        status="TERSEDIA"
    )
    area_repo.tambah_area(area1)

    # ==============================
    # TAMBAH HUNIAN
    # ==============================
    hunian1 = hunian_service.tambah_hunian(
        id_hunian=101,
        nama="Hunian A1",
        lokasi="Lantai 1",
        kapasitas=10,
        area=area1
    )

    print(f"Hunian ditambahkan: {hunian1.getNamaHunian()}")

    # ==============================
    # REGISTRASI
    # ==============================
    registrasi1 = registrasi_service.buat_registrasi(
        id_registrasi=1001,
        tgl_masuk=date(2025, 1, 1),
        tgl_keluar=date(2025, 1, 10)
    )

    print("Registrasi berhasil dibuat")
    print("Status awal:", registrasi1.getStatus())

    # ==============================
    # SETUJUI REGISTRASI
    # ==============================
    registrasi_service.setujui_registrasi(1001)
    print("Status setelah disetujui:", registrasi1.getStatus())

    # ==============================
    # TAMPILKAN DATA
    # ==============================
    print("\n=== DAFTAR HUNIAN ===")
    for h in hunian_service.get_semua_hunian():
        print(f"- {h.getNamaHunian()} | Lokasi: {h.getLokasi()}")

    print("\n=== DAFTAR REGISTRASI ===")
    for r in registrasi_service.get_semua_registrasi():
        print(f"- ID {r.getIdRegistrasi()} | Status: {r.getStatus()}")


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()
