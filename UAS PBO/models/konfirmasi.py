from datetime import datetime

class Konfirmasi:
    """
    Kelas Konfirmasi merepresentasikan konfirmasi hunian atau penggunaan area tertentu.

    Attributes:
        __lamaTinggal (int): Lama tinggal atau penggunaan area dalam satuan hari.
        __area (Area): Objek Area yang dikonfirmasi.
        __keterangan (str): Keterangan tambahan terkait konfirmasi.
        __waktuKonfirmasi (datetime): Waktu pembuatan konfirmasi secara otomatis saat objek dibuat.
    """

    def __init__(self, lama_tinggal: int, area, keterangan: str):
        """
        Inisialisasi objek Konfirmasi.

        Args:
            lama_tinggal (int): Lama tinggal atau penggunaan area dalam satuan hari.
            area (Area): Objek Area yang dikonfirmasi.
            keterangan (str): Keterangan tambahan terkait konfirmasi.
        """
        self.__lamaTinggal = lama_tinggal
        self.__area = area
        self.__keterangan = keterangan
        self.__waktuKonfirmasi = datetime.now()

    # Getter
    def getLamaTinggal(self):
        """Mengembalikan lama tinggal atau penggunaan area (dalam hari)."""
        return self.__lamaTinggal

    def getArea(self):
        """Mengembalikan objek Area yang dikonfirmasi."""
        return self.__area

    def getKeterangan(self):
        """Mengembalikan keterangan tambahan terkait konfirmasi."""
        return self.__keterangan