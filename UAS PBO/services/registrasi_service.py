# services/registrasi_service.py

from models.registrasi import Registrasi
from repositories.registrasi_repo import RegistrasiRepository
from utils.date_helper import tanggal_valid
from utils.status_helper import (
    STATUS_PENDING,
    STATUS_DISETUJUI,
    STATUS_DITOLAK
)


class RegistrasiService:
    """
    Service layer yang menangani seluruh logika bisnis terkait Registrasi.

    Kelas ini berfungsi sebagai perantara antara:
    - Model (Registrasi) sebagai representasi data
    - Repository (RegistrasiRepository) sebagai penyimpanan data

    Tanggung jawab utama:
    - Validasi aturan bisnis registrasi
    - Mengatur perubahan status registrasi
    - Menjaga konsistensi alur proses registrasi

    Kelas ini TIDAK:
    - Menyimpan data secara langsung
    - Melakukan perhitungan teknis tanggal
    - Berurusan dengan detail implementasi repository
    """

    def __init__(self, registrasi_repo: RegistrasiRepository):
        """
        Konstruktor RegistrasiService.

        Args:
            registrasi_repo (RegistrasiRepository):
                Repository yang bertugas menyimpan dan mengelola data Registrasi.
        """
        self._repo = registrasi_repo

    # ===== LOGIKA BISNIS =====

    def buat_registrasi(self, id_registrasi, tgl_masuk, tgl_keluar):
        """
        Membuat registrasi baru berdasarkan aturan bisnis yang berlaku.

        Aturan bisnis:
        - Tanggal keluar tidak boleh lebih awal dari tanggal masuk
        - Status awal registrasi selalu PENDING

        Args:
            id_registrasi (int):
                ID unik untuk registrasi.
            tgl_masuk (date):
                Tanggal mulai hunian.
            tgl_keluar (date):
                Tanggal berakhir hunian.

        Returns:
            Registrasi:
                Objek registrasi yang berhasil dibuat dan disimpan.

        Raises:
            ValueError:
                Jika tanggal keluar lebih awal dari tanggal masuk.
        """

        if not tanggal_valid(tgl_masuk, tgl_keluar):
            raise ValueError("Tanggal keluar tidak boleh sebelum tanggal masuk")

        registrasi = Registrasi(
            id_registrasi,
            tgl_masuk,
            tgl_keluar,
            STATUS_PENDING
        )

        self._repo.tambah_registrasi(registrasi)
        return registrasi

    def setujui_registrasi(self, id_registrasi):
        """
        Menyetujui registrasi yang berstatus PENDING.

        Aturan bisnis:
        - Hanya registrasi dengan status PENDING yang dapat disetujui

        Args:
            id_registrasi (int):
                ID registrasi yang akan disetujui.

        Returns:
            Registrasi:
                Objek registrasi dengan status diperbarui menjadi DISETUJUI.

        Raises:
            ValueError:
                Jika registrasi tidak ditemukan atau status bukan PENDING.
        """

        registrasi = self._ambil_registrasi(id_registrasi)

        if registrasi.getStatus() != STATUS_PENDING:
            raise ValueError("Registrasi hanya bisa disetujui dari status PENDING")

        registrasi.setStatus(STATUS_DISETUJUI)
        return registrasi

    def tolak_registrasi(self, id_registrasi):
        """
        Menolak registrasi yang berstatus PENDING.

        Aturan bisnis:
        - Hanya registrasi dengan status PENDING yang dapat ditolak

        Args:
            id_registrasi (int):
                ID registrasi yang akan ditolak.

        Returns:
            Registrasi:
                Objek registrasi dengan status diperbarui menjadi DITOLAK.

        Raises:
            ValueError:
                Jika registrasi tidak ditemukan atau status bukan PENDING.
        """

        registrasi = self._ambil_registrasi(id_registrasi)

        if registrasi.getStatus() != STATUS_PENDING:
            raise ValueError("Registrasi hanya bisa ditolak dari status PENDING")

        registrasi.setStatus(STATUS_DITOLAK)
        return registrasi

    def get_semua_registrasi(self):
        """
        Mengambil seluruh data registrasi yang tersimpan di repository.

        Method ini bersifat read-only dan tidak memodifikasi data.

        Returns:
            list:
                Daftar seluruh objek Registrasi.
        """
        return self._repo.get_semua_registrasi()

    # ===== HELPER INTERNAL (DRY) =====

    def _ambil_registrasi(self, id_registrasi):
        """
        Mengambil objek registrasi berdasarkan ID.

        Method ini bersifat internal dan digunakan untuk:
        - Menghindari duplikasi kode pencarian registrasi
        - Menyederhanakan logika pada method lain

        Args:
            id_registrasi (int):
                ID registrasi yang dicari.

        Returns:
            Registrasi:
                Objek Registrasi yang ditemukan.

        Raises:
            ValueError:
                Jika registrasi dengan ID tersebut tidak ditemukan.
        """

        registrasi = self._repo.get_registrasi_by_id(id_registrasi)
        if not registrasi:
            raise ValueError("Registrasi tidak ditemukan")
        return registrasi
