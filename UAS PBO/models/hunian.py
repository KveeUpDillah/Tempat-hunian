from abc import ABC, abstractmethod
from models.area import Area


class AbstractHunian(ABC):
    """
    Abstract class yang mendefinisikan kontrak perilaku untuk Hunian.

    Kelas abstrak ini digunakan untuk memastikan bahwa setiap kelas
    yang merepresentasikan Hunian wajib mengimplementasikan method-method
    dasar seperti identitas, nama, lokasi, dan kapasitas hunian.

    Tujuan:
    - Menerapkan konsep Abstraksi (ABC)
    - Menjadi kontrak/interface bagi kelas Hunian
    """

    @abstractmethod
    def getIdHunian(self):
        """
        Mengembalikan ID hunian.

        Method ini harus diimplementasikan oleh kelas turunan
        untuk menyediakan identitas unik hunian.

        Returns:
            int: ID unik hunian.
        """
        pass

    @abstractmethod
    def getNamaHunian(self):
        """
        Mengembalikan nama hunian.

        Method ini merepresentasikan nama unit hunian
        yang bersifat spesifik dan dapat berbeda dengan nama area.

        Returns:
            str: Nama hunian.
        """
        pass

    @abstractmethod
    def getLokasi(self):
        """
        Mengembalikan lokasi hunian.

        Lokasi dapat berupa alamat, zona, atau keterangan posisi hunian.

        Returns:
            str: Lokasi hunian.
        """
        pass

    @abstractmethod
    def getKapasitas(self):
        """
        Mengembalikan kapasitas hunian.

        Kapasitas hunian berbeda dengan kapasitas area,
        sehingga method ini wajib dioverride oleh kelas konkret.

        Returns:
            int: Kapasitas hunian.
        """
        pass


class Hunian(Area, AbstractHunian):
    """
    Kelas Hunian, turunan dari Area, merepresentasikan sebuah hunian
    dengan atribut tambahan dan kapasitas khusus hunian.

    Kelas ini mengimplementasikan AbstractHunian dan mewarisi Area
    untuk mendapatkan atribut umum seperti ID area, nama area,
    kapasitas area, dan status area.

    Attributes:
        __idHunian (int): ID unik hunian.
        __namaHunian (str): Nama hunian.
        __lokasi (str): Lokasi hunian.
        __kapasitas (int): Kapasitas khusus hunian.

    Inherits:
        Area: Menyediakan informasi umum area.
        AbstractHunian: Kontrak perilaku hunian.
    """

    def __init__(self, id_hunian, nama, lokasi, kapasitas, area: Area):
        """
        Inisialisasi objek Hunian.

        Konstruktor ini menginisialisasi:
        - Data area melalui konstruktor superclass (Area)
        - Data spesifik hunian seperti ID, nama, lokasi, dan kapasitas hunian

        Args:
            id_hunian (int): ID unik hunian.
            nama (str): Nama hunian.
            lokasi (str): Lokasi hunian.
            kapasitas (int): Kapasitas khusus hunian.
            area (Area): Objek Area yang menjadi basis hunian.
        """
        super().__init__(
            area.getIdArea(),
            area.getNamaArea(),
            area.getKapasitas(),  # kapasitas AREA
            area.getStatus()
        )
        self.__idHunian = id_hunian
        self.__namaHunian = nama
        self.__lokasi = lokasi
        self.__kapasitas = kapasitas

    # Getter
    def getIdHunian(self):
        """
        Mengembalikan ID hunian.

        Returns:
            int: ID unik hunian.
        """
        return self.__idHunian

    def getNamaHunian(self):
        """
        Mengembalikan nama hunian.

        Returns:
            str: Nama hunian.
        """
        return self.__namaHunian

    def getLokasi(self):
        """
        Mengembalikan lokasi hunian.

        Returns:
            str: Lokasi hunian.
        """
        return self.__lokasi

    def getKapasitas(self):
        """
        Mengembalikan kapasitas hunian.

        Method ini mengoverride method getKapasitas dari Area
        untuk merepresentasikan kapasitas khusus hunian.

        Returns:
            int: Kapasitas hunian.
        """
        return self.__kapasitas

    # Setter
    def setNamaHunian(self, nama):
        """
        Mengubah nama hunian.

        Args:
            nama (str): Nama baru hunian.
        """
        self.__namaHunian = nama

    def setLokasi(self, lokasi):
        """
        Mengubah lokasi hunian.

        Args:
            lokasi (str): Lokasi baru hunian.
        """
        self.__lokasi = lokasi

    def setKapasitas(self, kapasitas):
        """
        Mengubah kapasitas hunian.

        Kapasitas hunian harus bernilai non-negatif.

        Args:
            kapasitas (int): Kapasitas baru hunian.

        Raises:
            ValueError: Jika kapasitas bernilai negatif.
        """
        if kapasitas < 0:
            raise ValueError("Kapasitas hunian tidak boleh negatif")
        self.__kapasitas = kapasitas
