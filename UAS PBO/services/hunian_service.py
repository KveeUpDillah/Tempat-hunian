from models.hunian import Hunian
from repositories.hunian_repo import HunianRepository


class HunianService:
    """
    Service layer untuk menangani logika bisnis Hunian.

    Tanggung jawab:
    - Mengatur aturan bisnis terkait Hunian
    - Memvalidasi data sebelum disimpan atau diubah
    - Menjadi penghubung antara Controller/Main dan Repository
    """

    def __init__(self, hunian_repo: HunianRepository):
        """
        Konstruktor HunianService.

        Args:
            hunian_repo (HunianRepository):
                Repository yang bertanggung jawab atas penyimpanan data Hunian.
        """
        self._repo = hunian_repo

    # ===== LOGIKA BISNIS =====

    def tambah_hunian(self, id_hunian, nama, lokasi, kapasitas, area):
        """
        Menambahkan hunian baru ke sistem.

        Aturan bisnis:
        - Kapasitas tidak boleh negatif
        - ID hunian tidak boleh duplikat

        Args:
            id_hunian (int): ID unik hunian
            nama (str): Nama hunian
            lokasi (str): Lokasi hunian
            kapasitas (int): Kapasitas hunian
            area (Area): Objek Area induk

        Returns:
            Hunian: Objek Hunian yang berhasil ditambahkan

        Raises:
            ValueError: Jika ID hunian sudah ada atau kapasitas tidak valid
        """
        if kapasitas < 0:
            raise ValueError("Kapasitas hunian tidak boleh negatif")

        if self._repo.get_hunian_by_id(id_hunian):
            raise ValueError("ID hunian sudah terdaftar")

        hunian = Hunian(
            id_hunian=id_hunian,
            nama=nama,
            lokasi=lokasi,
            kapasitas=kapasitas,
            area=area
        )

        self._repo.tambah_hunian(hunian)
        return hunian

    def get_semua_hunian(self):
        """
        Mengambil seluruh data hunian.

        Returns:
            list: Daftar objek Hunian
        """
        return self._repo.get_semua_hunian()

    def get_hunian_by_id(self, id_hunian):
        """
        Mengambil data hunian berdasarkan ID.

        Args:
            id_hunian (int): ID hunian

        Returns:
            Hunian

        Raises:
            ValueError: Jika hunian tidak ditemukan
        """
        hunian = self._repo.get_hunian_by_id(id_hunian)
        if not hunian:
            raise ValueError("Hunian tidak ditemukan")
        return hunian

    def update_hunian(self, id_hunian, nama=None, lokasi=None, kapasitas=None):
        """
        Memperbarui data hunian.

        Aturan bisnis:
        - Kapasitas tidak boleh negatif

        Args:
            id_hunian (int): ID hunian
            nama (str, optional): Nama baru
            lokasi (str, optional): Lokasi baru
            kapasitas (int, optional): Kapasitas baru
        """
        if kapasitas is not None and kapasitas < 0:
            raise ValueError("Kapasitas hunian tidak boleh negatif")

        hunian = self._repo.get_hunian_by_id(id_hunian)
        if not hunian:
            raise ValueError("Hunian tidak ditemukan")

        self._repo.update_hunian(
            id_hunian=id_hunian,
            nama=nama,
            lokasi=lokasi,
            kapasitas=kapasitas
        )

    def hapus_hunian(self, id_hunian):
        """
        Menghapus hunian dari sistem.

        Args:
            id_hunian (int): ID hunian

        Raises:
            ValueError: Jika hunian tidak ditemukan
        """
        hunian = self._repo.get_hunian_by_id(id_hunian)
        if not hunian:
            raise ValueError("Hunian tidak ditemukan")

        self._repo.hapus_hunian(id_hunian)
