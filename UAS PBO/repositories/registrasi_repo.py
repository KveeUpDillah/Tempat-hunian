from models.registrasi import Registrasi


class RegistrasiRepository:
    """
    Repository Registrasi untuk menyimpan dan mengelola data Registrasi
    menggunakan struktur data List.

    Attributes:
        __list_registrasi (list of Registrasi): List yang menyimpan
                                                seluruh objek Registrasi.
    """

    def __init__(self):
        """
        Konstruktor RegistrasiRepository.

        Menginisialisasi repository dengan list kosong
        sebagai media penyimpanan data Registrasi.
        """
        self.__list_registrasi = []

    def tambah_registrasi(self, registrasi: Registrasi):
        """
        Menambahkan data registrasi baru ke dalam repository.

        Args:
            registrasi (Registrasi): Objek Registrasi yang akan disimpan.
        """
        self.__list_registrasi.append(registrasi)

    def get_semua_registrasi(self):
        """
        Mengambil seluruh data registrasi.

        Returns:
            list: Daftar objek Registrasi.
        """
        return self.__list_registrasi

    def get_registrasi_by_id(self, id_registrasi):
        """
        Mencari registrasi berdasarkan ID.

        Args:
            id_registrasi (int): ID registrasi.

        Returns:
            Registrasi | None: Objek Registrasi jika ditemukan,
                               None jika tidak ditemukan.
        """
        for reg in self.__list_registrasi:
            if reg.getIdRegistrasi() == id_registrasi:
                return reg
        return None

    def update_registrasi(self, id_registrasi, tgl_masuk=None, tgl_keluar=None, status=None):
        """
        Memperbarui data registrasi berdasarkan ID.

        Args:
            id_registrasi (int): ID registrasi.
            tgl_masuk (date, optional): Tanggal masuk baru.
            tgl_keluar (date, optional): Tanggal keluar baru.
            status (str, optional): Status baru registrasi.
        """
        registrasi = self.get_registrasi_by_id(id_registrasi)
        if registrasi:
            if tgl_masuk is not None:
                registrasi.setTglMasuk(tgl_masuk)
            if tgl_keluar is not None:
                registrasi.setTglKeluar(tgl_keluar)
            if status is not None:
                registrasi.setStatus(status)

    def hapus_registrasi(self, id_registrasi):
        """
        Menghapus data registrasi berdasarkan ID.

        Args:
            id_registrasi (int): ID registrasi.
        """
        registrasi = self.get_registrasi_by_id(id_registrasi)
        if registrasi:
            self.__list_registrasi.remove(registrasi)
