from models.hunian import Hunian


class HunianRepository:
    """
    Repository Hunian untuk menyimpan dan mengelola data Hunian
    menggunakan struktur data List.

    Attributes:
        __list_hunian (list of Hunian): List yang menyimpan seluruh
                                        objek Hunian dalam sistem.
    """

    def __init__(self):
        """
        Konstruktor HunianRepository.

        Menginisialisasi repository dengan list kosong
        sebagai media penyimpanan data Hunian.
        """
        self.__list_hunian = []

    def tambah_hunian(self, hunian: Hunian):
        """
        Menambahkan data hunian baru ke dalam repository.

        Args:
            hunian (Hunian): Objek Hunian yang akan disimpan.
        """
        self.__list_hunian.append(hunian)

    def get_semua_hunian(self):
        """
        Mengambil seluruh data hunian.

        Returns:
            list: Daftar objek Hunian.
        """
        return self.__list_hunian

    def get_hunian_by_id(self, id_hunian):
        """
        Mencari hunian berdasarkan ID.

        Args:
            id_hunian (int): ID hunian.

        Returns:
            Hunian | None: Objek Hunian jika ditemukan,
                           None jika tidak ditemukan.
        """
        for hunian in self.__list_hunian:
            if hunian.getIdHunian() == id_hunian:
                return hunian
        return None

    def update_hunian(self, id_hunian, nama=None, lokasi=None, kapasitas=None):
        """
        Memperbarui data hunian berdasarkan ID.

        Args:
            id_hunian (int): ID hunian.
            nama (str, optional): Nama baru hunian.
            lokasi (str, optional): Lokasi baru hunian.
            kapasitas (int, optional): Kapasitas baru hunian.
        """
        hunian = self.get_hunian_by_id(id_hunian)
        if hunian:
            if nama is not None:
                hunian.setNamaHunian(nama)
            if lokasi is not None:
                hunian.setLokasi(lokasi)
            if kapasitas is not None:
                hunian.setKapasitas(kapasitas)

    def hapus_hunian(self, id_hunian):
        """
        Menghapus data hunian berdasarkan ID.

        Args:
            id_hunian (int): ID hunian.
        """
        hunian = self.get_hunian_by_id(id_hunian)
        if hunian:
            self.__list_hunian.remove(hunian)
