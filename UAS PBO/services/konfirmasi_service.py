from models.konfirmasi import Konfirmasi
from repositories.konfirmasi_repo import KonfirmasiRepository


class KonfirmasiService:
    """
    Service layer untuk menangani logika bisnis Konfirmasi.

    Tanggung jawab:
    - Memvalidasi aturan bisnis sebelum data disimpan
    - Mengatur alur pembuatan, pengambilan, perubahan, dan penghapusan konfirmasi
    - Tidak menyimpan data langsung (delegasi ke Repository)
    """

    def __init__(self, konfirmasi_repo: KonfirmasiRepository):
        """
        Konstruktor KonfirmasiService.

        Args:
            konfirmasi_repo (KonfirmasiRepository):
                Repository yang menangani penyimpanan data Konfirmasi.
        """
        self._repo = konfirmasi_repo

    # ===== LOGIKA BISNIS =====

    def buat_konfirmasi(self, lama_tinggal, area, keterangan):
        """
        Membuat konfirmasi baru.

        Aturan bisnis:
        - Lama tinggal harus lebih dari 0 hari

        Args:
            lama_tinggal (int): Lama tinggal dalam satuan hari
            area (Area): Area hunian yang dikonfirmasi
            keterangan (str): Keterangan tambahan

        Returns:
            Konfirmasi: Objek konfirmasi yang berhasil dibuat
        """
        if lama_tinggal <= 0:
            raise ValueError("Lama tinggal harus lebih dari 0 hari")

        konfirmasi = Konfirmasi(
            lama_tinggal=lama_tinggal,
            area=area,
            keterangan=keterangan
        )

        self._repo.tambah_konfirmasi(konfirmasi)
        return konfirmasi

    def get_semua_konfirmasi(self):
        """
        Mengambil seluruh data konfirmasi.

        Returns:
            list: Daftar objek Konfirmasi
        """
        return self._repo.get_semua_konfirmasi()

    def get_konfirmasi_by_area(self, id_area):
        """
        Mengambil data konfirmasi berdasarkan ID area.

        Args:
            id_area (int): ID area hunian

        Returns:
            list: Daftar Konfirmasi sesuai area
        """
        return self._repo.get_konfirmasi_by_area(id_area)

    def update_konfirmasi(self, index, lama_tinggal=None, area=None, keterangan=None):
        """
        Memperbarui data konfirmasi.

        Aturan bisnis:
        - Jika lama tinggal diubah, nilainya harus > 0

        Args:
            index (int): Posisi data konfirmasi dalam list
            lama_tinggal (int, optional): Lama tinggal baru
            area (Area, optional): Area baru
            keterangan (str, optional): Keterangan baru
        """
        if lama_tinggal is not None and lama_tinggal <= 0:
            raise ValueError("Lama tinggal harus lebih dari 0 hari")

        self._repo.update_konfirmasi(
            index=index,
            lama_tinggal=lama_tinggal,
            area=area,
            keterangan=keterangan
        )

    def hapus_konfirmasi(self, index):
        """
        Menghapus data konfirmasi berdasarkan indeks.

        Args:
            index (int): Posisi konfirmasi dalam list
        """
        self._repo.hapus_konfirmasi(index)
