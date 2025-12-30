class Regu:
    """
    Kelas Regu merepresentasikan sebuah tim atau kelompok dengan anggota tertentu.

    Attributes:
        __idRegu (int): ID unik regu.
        __namaRegu (str): Nama regu.
        __anggota (list): Daftar anggota regu.
    """

    def __init__(self, id_regu, nama_regu, anggota: list):
        """
        Inisialisasi objek Regu.

        Args:
            id_regu (int): ID unik regu.
            nama_regu (str): Nama regu.
            anggota (list): Daftar anggota regu.
        """
        self.__idRegu = id_regu
        self.__namaRegu = nama_regu
        self.__anggota = anggota

    # Getter
    def getIdRegu(self):
        """Mengembalikan ID regu."""
        return self.__idRegu

    def getNamaRegu(self):
        """Mengembalikan nama regu."""
        return self.__namaRegu

    def getAnggota(self):
        """Mengembalikan daftar anggota regu."""
        return self.__anggota

    # Setter
    def setNamaRegu(self, nama):
        """Mengubah nama regu."""
        self.__namaRegu = nama

    def setAnggota(self, anggota: list):
        """Mengubah daftar anggota regu."""
        self.__anggota = anggota
