class Pengelola:
    """
    Kelas Pengelola merepresentasikan petugas atau pengelola suatu area atau hunian.

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
        """Mengembalikan ID petugas."""
        return self.__idPetugas

    def getNama(self):
        """Mengembalikan nama petugas."""
        return self.__nama

    def getJabatan(self):
        """Mengembalikan jabatan petugas."""
        return self.__jabatan

    # Setter
    def setNama(self, nama):
        """Mengubah nama petugas."""
        self.__nama = nama

    def setJabatan(self, jabatan):
        """Mengubah jabatan petugas."""
        self.__jabatan = jabatan
