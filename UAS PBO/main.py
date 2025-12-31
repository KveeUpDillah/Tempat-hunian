# main.py
from datetime import date
import logging

# ==============================
# KONFIGURASI LOGGER
# ==============================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

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
    logger.info("Sistem Manajemen Hunian dimulai")

    # ==============================
    # INISIALISASI REPOSITORY
    # ==============================
    area_repo = AreaRepository()
    hunian_repo = HunianRepository()
    registrasi_repo = RegistrasiRepository()
    logger.info("Repository berhasil diinisialisasi")

    # ==============================
    # INISIALISASI SERVICE
    # ==============================
    hunian_service = HunianService(hunian_repo)
    registrasi_service = RegistrasiService(registrasi_repo)
    logger.info("Service berhasil diinisialisasi")

    try:
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
        logger.info("Area berhasil ditambahkan: %s", area1.getNamaArea())

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
        logger.info("Hunian ditambahkan: %s", hunian1.getNamaHunian())

        # ==============================
        # REGISTRASI
        # ==============================
        registrasi1 = registrasi_service.buat_registrasi(
            id_registrasi=1001,
            tgl_masuk=date(2025, 1, 1),
            tgl_keluar=date(2025, 1, 10)
        )
        logger.info("Registrasi berhasil dibuat (ID=%s)", registrasi1.getIdRegistrasi())
        logger.info("Status awal registrasi: %s", registrasi1.getStatus())

        # ==============================
        # SETUJUI REGISTRASI
        # ==============================
        registrasi_service.setujui_registrasi(1001)
        logger.info("Registrasi ID 1001 berhasil disetujui")

        # ==============================
        # TAMPILKAN DATA
        # ==============================
        logger.info("Menampilkan daftar hunian")
        semua_hunian = hunian_service.get_semua_hunian()
        if not semua_hunian:
            logger.warning("Tidak ada data hunian")
        for h in semua_hunian:
            logger.info("Hunian: %s | Lokasi: %s", h.getNamaHunian(), h.getLokasi())

        logger.info("Menampilkan daftar registrasi")
        semua_registrasi = registrasi_service.get_semua_registrasi()
        if not semua_registrasi:
            logger.warning("Tidak ada data registrasi")
        for r in semua_registrasi:
            logger.info("Registrasi ID %s | Status: %s",
                        r.getIdRegistrasi(), r.getStatus())

    except Exception as e:
        logger.error("Terjadi kesalahan fatal: %s", str(e))


# ==============================
# ENTRY POINT
# ==============================
if __name__ == "__main__":
    main()
