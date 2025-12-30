class Regu:
    """
    Kelas Regu merepresentasikan sebuah tim atau kelompok dengan anggota tertentu.

    Attributes:
        __idRegu (int): ID unik regu.
        __namaRegu (str): Nama regu.
        __anggota (list): Daftar anggota yang tergabung/bertambah dalam regu.
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
        """
        Mengembalikan ID regu.
        
        Returns:
            int: ID yang unik pada regu.
        """
        return self.__idRegu

    def getNamaRegu(self):
        """Mengembalikan nama regu.
        
        Returns:
            string: Nama regu.
        """
        return self.__namaRegu

    def getAnggota(self):
        """
        Mengembalikan daftar anggota regu.
        
        Returns:
            list: daftar anggota baru.
        """
        return self.__anggota

    # Setter
    def setNamaRegu(self, nama):
        """
        Mengubah nama regu.
        
        Args:
            nama(string): Nama baru untuk regu.
        """
        self.__namaRegu = nama

    def setAnggota(self, anggota: list):
        """
        Mengubah daftar anggota regu.
        
        Args:
            anggota(list): Daftar anggota baru untuk regu.
        """
        self.__anggota = anggota

