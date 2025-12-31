from abc import ABC, abstractmethod
from typing import List

# ABSTRAKSI (INTERFACE)
class AbstractAnggota(ABC):
    """
    AbstractAnggota adalah kelas abstrak yang mendefinisikan
    kontrak perilaku untuk anggota dalam sebuah regu.

    Kelas ini digunakan sebagai bentuk penerapan
    Dependency Inversion Principle (DIP),
    di mana kelas tingkat tinggi (Regu) bergantung
    pada abstraksi, bukan implementasi konkret.
    """

    @abstractmethod
    def getNama(self) -> str:
        """
        Mengembalikan nama anggota.

        Method ini wajib diimplementasikan oleh setiap
        kelas konkret yang merepresentasikan anggota.

        Returns:
            str: Nama anggota.
        """
        pass


# IMPLEMENTASI KONKRET
class Anggota(AbstractAnggota):
    """
    Kelas Anggota merupakan implementasi konkret dari
    AbstractAnggota.

    Kelas ini merepresentasikan anggota regu secara nyata
    dengan atribut nama.
    """

    def __init__(self, nama: str):
        """
        Inisialisasi objek Anggota.

        Args:
            nama (str): Nama anggota.
        """
        self.__nama = nama

    def getNama(self) -> str:
        """
        Mengembalikan nama anggota.

        Returns:
            str: Nama anggota.
        """
        return self.__nama


# HIGH LEVEL MODULE
class Regu:
    """
    Kelas Regu merepresentasikan sebuah tim atau kelompok
    yang terdiri dari beberapa anggota.

    Kelas ini merupakan High Level Module dan telah
    memenuhi Dependency Inversion Principle (DIP)
    karena tidak bergantung langsung pada kelas konkret
    Anggota, melainkan pada abstraksi AbstractAnggota.

    Dengan desain ini, Regu tetap stabil meskipun
    terdapat perubahan atau penambahan jenis anggota baru.
    """

    def __init__(
        self,
        id_regu: int,
        nama_regu: str,
        anggota: List[AbstractAnggota]
    ):
        """
        Inisialisasi objek Regu.

        Args:
            id_regu (int): ID unik regu.
            nama_regu (str): Nama regu.
            anggota (List[AbstractAnggota]): Daftar anggota
                                             yang tergabung
                                             dalam regu.
        """
        self.__idRegu = id_regu
        self.__namaRegu = nama_regu
        self.__anggota = anggota

    # GETTER
    def getIdRegu(self) -> int:
        """
        Mengembalikan ID regu.

        Returns:
            int: ID unik regu.
        """
        return self.__idRegu

    def getNamaRegu(self) -> str:
        """
        Mengembalikan nama regu.

        Returns:
            str: Nama regu.
        """
        return self.__namaRegu

    def getAnggota(self) -> List[AbstractAnggota]:
        """
        Mengembalikan daftar anggota regu.

        Returns:
            List[AbstractAnggota]: Daftar objek anggota
                                   dalam regu.
        """
        return self.__anggota

    # SETTER
    def setNamaRegu(self, nama: str):
        """
        Mengubah nama regu.

        Args:
            nama (str): Nama baru regu.
        """
        self.__namaRegu = nama

    def setAnggota(self, anggota: List[AbstractAnggota]):
        """
        Mengubah daftar anggota regu.

        Args:
            anggota (List[AbstractAnggota]): Daftar anggota
                                             baru untuk regu.
        """
        self.__anggota = anggota