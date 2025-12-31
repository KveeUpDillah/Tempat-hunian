from abc import ABC, abstractmethod


class AbstractPengelola(ABC):
    """
    Abstract class yang mendefinisikan kontrak perilaku untuk Pengelola.

    Kelas abstrak ini memastikan bahwa setiap kelas pengelola
    memiliki identitas, nama, dan jabatan yang dapat diakses
    melalui method yang telah ditentukan.
    """

    @abstractmethod
    def getIdPetugas(self):
        """
        Mengembalikan ID petugas.

        Returns:
            int: ID unik petugas.
        """
        pass

    @abstractmethod
    def getNama(self):
        """
        Mengembalikan nama petugas.

        Returns:
            str: Nama petugas.
        """
        pass

    @abstractmethod
    def getJabatan(self):
        """
        Mengembalikan jabatan petugas.

        Returns:
            str: Jabatan atau posisi petugas.
        """
        pass


class Pengelola(AbstractPengelola):
    """
    Kelas Pengelola merepresentasikan petugas atau pengelola
    suatu area atau hunian.

    Attributes:
        __idPetugas (int): ID unik petugas.
        __nama (str): Nama petugas.
        __jabatan (str): Jabatan atau posisi petugas.
    """

    def __init__(self, id_petugas, nama, jabatan):
        """
        Inisialisasi objek Pengelola.

        Args:
            id_petugas (int): ID unik petugas.
            nama (str): Nama petugas.
            jabatan (str): Jabatan atau posisi petugas.
        """
        self.__idPetugas = id_petugas
        self.__nama = nama
        self.__jabatan = jabatan

    # Getter
    def getIdPetugas(self):
        """
        Mengembalikan ID petugas.

        Returns:
            int: ID yang unik pada petugas.
        """
        return self.__idPetugas

    def getNama(self):
        """
        Mengembalikan nama petugas.

        Returns:
            str: Nama petugas.
        """
        return self.__nama

    def getJabatan(self):
        """
        Mengembalikan jabatan petugas.

        Returns:
            str: Jabatan atau posisi petugas.
        """
        return self.__jabatan

    # Setter
    def setNama(self, nama):
        """
        Mengubah nama petugas.

        Args:
            nama (str): Nama baru untuk petugas.
        """
        self.__nama = nama

    def setJabatan(self, jabatan):
        """
        Mengubah jabatan petugas.

        Args:
            jabatan (str): Jabatan baru untuk petugas.
        """
        self.__jabatan = jabatan