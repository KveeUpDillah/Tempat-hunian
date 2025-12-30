class Area:
    """
    Kelas untuk merepresentasikan sebuah area hunian atau fasilitas.

    Attributes:
        __idArea (int): ID unik dari area.
        __namaArea (str): Nama area.
        __kapasitas (int): Kapasitas orang di area.
        __status (str): Status ketersediaan area (misal: 'tersedia', 'penuh').

    Methods:
        getIdArea(): Mengambil ID area.
        getNamaArea(): Mengembalikan nama area.
        getKapasitas(): Mengembalikan kapasitas area.
        getStatus(): Mengembalikan status area.
        setNamaArea(nama): Mengubah nama area.
        setKapasitas(kapasitas): Mengubah kapasitas area (Nilai negatif akan memunculkan ValueError).
        setStatus(status): Mengubah status area.
    """

    def __init__(self, id_area: int, nama: str, kapasitas: int, status: str):
        """
        Inisialisasi objek Area dengan ID, nama, kapasitas, dan status.

        Args:
            id_area (int): ID unik dari area.
            nama (str): Nama area.
            kapasitas (int): Kapasitas area.
            status (str): Status ketersediaan area.
        """
        self.__idArea = id_area
        self.__namaArea = nama
        self.__kapasitas = kapasitas
        self.__status = status

    # Getter
    def getIdArea(self):
        """Mengembalikan ID area."""
        return self.__idArea

    def getNamaArea(self):
        """Mengembalikan nama area."""
        return self.__namaArea

    def getKapasitas(self):
        """Mengembalikan kapasitas area."""
        return self.__kapasitas

    def getStatus(self):
        """Mengembalikan status area."""
        return self.__status

    # Setter
    def setNamaArea(self, nama):
        """
        Mengubah nama area.

        Args:
            nama (str): Nama baru area.
        """
        self.__namaArea = nama

    def setKapasitas(self, kapasitas):
        """
        Mengubah kapasitas area.

        Args:
            kapasitas (int): Kapasitas baru area. Tidak boleh negatif.

        Raises:
            ValueError: Jika kapasitas bernilai negatif, program akan berhenti.
        """
        if kapasitas < 0:
            raise ValueError("Kapasitas tidak boleh negatif")
        self.__kapasitas = kapasitas

    def setStatus(self, status):
        """
        Mengubah status area.

        Args:
            status (str): Status baru area.
        """
        self.__status = status

