from models.konfirmasi import Konfirmasi


class KonfirmasiRepository:
    """
    Repository Konfirmasi berfungsi untuk menyimpan dan mengelola
    data Konfirmasi menggunakan struktur data List.

    Attributes:
        __list_konfirmasi (list of Konfirmasi): Menyimpan seluruh
                                                objek Konfirmasi
                                                yang tercatat dalam sistem.
    """

    def __init__(self):
        """
        Konstruktor KonfirmasiRepository.

        Menginisialisasi repository dengan list kosong
        sebagai media penyimpanan data Konfirmasi.
        """
        self.__list_konfirmasi = []

    def tambah_konfirmasi(self, konfirmasi: Konfirmasi):
        """
        Menambahkan data konfirmasi baru ke repository.

        Args:
            konfirmasi (Konfirmasi): Objek Konfirmasi yang akan disimpan.
        """
        self.__list_konfirmasi.append(konfirmasi)

    def get_semua_konfirmasi(self):
        """
        Mengambil seluruh data konfirmasi.

        Returns:
            list: Daftar objek Konfirmasi.
        """
        return self.__list_konfirmasi

    def get_konfirmasi_by_area(self, id_area):
        """
        Mengambil data konfirmasi berdasarkan ID area hunian.

        Args:
            id_area (int): ID area hunian.

        Returns:
            list: Daftar Konfirmasi yang berkaitan dengan area tersebut.
        """
        hasil = []
        for konfirmasi in self.__list_konfirmasi:
            if konfirmasi.getAreaHunian().getIdArea() == id_area:
                hasil.append(konfirmasi)
        return hasil

    def update_konfirmasi(self, index, lama_tinggal=None, area=None, keterangan=None):
        """
        Memperbarui data konfirmasi berdasarkan indeks list.

        Args:
            index (int): Posisi konfirmasi dalam list.
            lama_tinggal (int, optional): Lama tinggal baru.
            area (Area, optional): Area hunian baru.
            keterangan (str, optional): Keterangan baru.
        """
        if 0 <= index < len(self.__list_konfirmasi):
            konfirmasi = self.__list_konfirmasi[index]

            if lama_tinggal is not None:
                konfirmasi.setLamaTinggal(lama_tinggal)
            if area is not None:
                konfirmasi.setAreaHunian(area)
            if keterangan is not None:
                konfirmasi.setKeterangan(keterangan)

    def hapus_konfirmasi(self, index):
        """
        Menghapus data konfirmasi berdasarkan indeks list.

        Args:
            index (int): Posisi konfirmasi dalam list.
        """
        if 0 <= index < len(self.__list_konfirmasi):
            self.__list_konfirmasi.pop(index)
