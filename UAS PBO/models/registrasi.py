from datetime import date

class Registrasi:
    """
    Kelas Registrasi merepresentasikan proses registrasi atau pencatatan masuk-keluar hunian/area.

    Attributes:
        __idRegistrasi (int): ID unik registrasi.
        __tglMasuk (date): Tanggal masuk/hunian dimulai.
        __tglKeluar (date): Tanggal keluar/hunian berakhir.
        __status (str): Status registrasi (misal: 'aktif', 'selesai', 'dibatalkan').
    """

    def __init__(self, id_registrasi, tgl_masuk: date, tgl_keluar: date, status: str):
        """
        Inisialisasi objek Registrasi.

        Args:
            id_registrasi (int): ID unik registrasi.
            tgl_masuk (date): Tanggal mulai registrasi.
            tgl_keluar (date): Tanggal berakhir registrasi.
            status (str): Status registrasi.
        """
        self.__idRegistrasi = id_registrasi
        self.__tglMasuk = tgl_masuk
        self.__tglKeluar = tgl_keluar
        self.__status = status

    # Getter
    def getIdRegistrasi(self):
        """Mengembalikan ID registrasi."""
        return self.__idRegistrasi

    def getTglMasuk(self):
        """Mengembalikan tanggal masuk registrasi."""
        return self.__tglMasuk

    def getTglKeluar(self):
        """Mengembalikan tanggal keluar registrasi."""
        return self.__tglKeluar

    def getStatus(self):
        """Mengembalikan status registrasi."""
        return self.__status

    # Setter
    def setStatus(self, status):
        """Mengubah status registrasi."""
        self.__status = status
