from abc import ABC, abstractmethod
from datetime import datetime


class AbstractKonfirmasi(ABC):
    """
    Abstract class yang mendefinisikan kontrak perilaku untuk Konfirmasi.

    Kelas abstrak ini memastikan setiap kelas konfirmasi
    memiliki informasi dasar seperti lama tinggal,
    area hunian, keterangan, dan waktu konfirmasi.
    """

    @abstractmethod
    def getLamaTinggal(self):
        """
        Mengembalikan lama tinggal.

        Returns:
            int: Lama tinggal dalam satuan hari.
        """
        pass

    @abstractmethod
    def getAreaHunian(self):
        """
        Mengembalikan area hunian yang dikonfirmasi.

        Returns:
            Area: Objek Area terkait konfirmasi.
        """
        pass

    @abstractmethod
    def getKeterangan(self):
        """
        Mengembalikan keterangan konfirmasi.

        Returns:
            str: Keterangan konfirmasi.
        """
        pass

    @abstractmethod
    def getWaktuKonfirmasi(self):
        """
        Mengembalikan waktu konfirmasi dibuat.

        Returns:
            datetime: Waktu konfirmasi.
        """
        pass


class Konfirmasi(AbstractKonfirmasi):
    """
    Kelas Konfirmasi merepresentasikan proses konfirmasi hunian
    atau penggunaan suatu area oleh regu atau pengguna tertentu.

    Kelas ini menyimpan informasi lama tinggal, area hunian,
    keterangan tambahan, serta waktu konfirmasi dibuat.

    Attributes:
        __lamaTinggal (int): Lama tinggal atau penggunaan area
                             dalam satuan hari.
        __areaHunian (Area): Objek Area yang dikonfirmasi.
        __keterangan (str): Keterangan atau catatan tambahan
                            terkait konfirmasi.
        __waktuKonfirmasi (datetime): Waktu saat konfirmasi dibuat.
    """

    def __init__(self, lama_tinggal: int, area, keterangan: str):
        """
        Konstruktor Konfirmasi.

        Menginisialisasi objek Konfirmasi dengan lama tinggal,
        area hunian, keterangan, serta waktu konfirmasi otomatis
        sesuai waktu sistem.

        Args:
            lama_tinggal (int): Lama tinggal dalam satuan hari.
            area (Area): Objek Area yang dikonfirmasi.
            keterangan (str): Keterangan tambahan konfirmasi.
        """
        self.__lamaTinggal = lama_tinggal
        self.__areaHunian = area
        self.__keterangan = keterangan
        self.__waktuKonfirmasi = datetime.now()

    # Getter
    def getLamaTinggal(self):
        """
        Mengembalikan lama tinggal.

        Returns:
            int: Lama tinggal dalam satuan hari.
        """
        return self.__lamaTinggal

    def getAreaHunian(self):
        """
        Mengembalikan area hunian yang dikonfirmasi.

        Returns:
            Area: Objek Area terkait konfirmasi.
        """
        return self.__areaHunian

    def getKeterangan(self):
        """
        Mengembalikan keterangan tambahan konfirmasi.

        Returns:
            str: Keterangan konfirmasi.
        """
        return self.__keterangan

    def getWaktuKonfirmasi(self):
        """
        Mengembalikan waktu konfirmasi dibuat.

        Returns:
            datetime: Waktu konfirmasi.
        """
        return self.__waktuKonfirmasi

    # Setter
    def setLamaTinggal(self, hari: int):
        """
        Mengubah lama tinggal.

        Args:
            hari (int): Lama tinggal baru dalam satuan hari.
        """
        self.__lamaTinggal = hari

    def setAreaHunian(self, area):
        """
        Mengubah area hunian yang dikonfirmasi.

        Args:
            area (Area): Area hunian baru.
        """
        self.__areaHunian = area

    def setKeterangan(self, keterangan: str):
        """
        Mengubah keterangan atau catatan tambahan.

        Args:
            keterangan (str): Keterangan baru.
        """
        self.__keterangan = keterangan