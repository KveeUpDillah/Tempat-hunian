from models.area import Area

class Hunian(Area):
    """
    Kelas Hunian, turunan dari Area, merepresentasikan sebuah hunian dengan atribut tambahan.

    Attributes:
        __idHunian (int): ID unik hunian.
        __namaHunian (str): Nama hunian.
        __lokasi (str): Lokasi hunian.
        __kapasitas (int): Kapasitas hunian.
    
    Inherits:
        Area: ID, nama, kapasitas, dan status area.
    """

    def __init__(self, id_hunian, nama, lokasi, kapasitas, area: Area):
        """
        Inisialisasi objek Hunian.

        Args:
            id_hunian (int): ID unik hunian.
            nama (str): Nama hunian.
            lokasi (str): Lokasi hunian.
            kapasitas (int): Kapasitas hunian.
            area (Area): Objek Area yang menjadi basis hunian.
        """
        super().__init__(
            area.getIdArea(),
            area.getNamaArea(),
            area.getKapasitas(),
            area.getStatus()
        )
        self.__idHunian = id_hunian
        self.__namaHunian = nama
        self.__lokasi = lokasi
        self.__kapasitas = kapasitas

    # Getter
    def getIdHunian(self):
        """Mengembalikan ID hunian."""
        return self.__idHunian

    def getNamaHunian(self):
        """Mengembalikan nama hunian."""
        return self.__namaHunian

    def getLokasi(self):
        """Mengembalikan lokasi hunian."""
        return self.__lokasi

    def getKapasitas(self):
        """Mengembalikan kapasitas hunian."""
        return self.__kapasitas

    # Setter
    def setNamaHunian(self, nama):
        """Mengubah nama hunian."""
        self.__namaHunian = nama

    def setLokasi(self, lokasi):
        """Mengubah lokasi hunian."""
        self.__lokasi = lokasi

    def setKapasitas(self, kapasitas):
        """
        Mengubah kapasitas hunian.

        Args:
            kapasitas (int): Kapasitas baru hunian. Tidak boleh negatif.

        Raises:
            ValueError: Jika kapasitas bernilai negatif.
        """
        if kapasitas < 0:
            raise ValueError("Kapasitas hunian tidak boleh negatif")
        self.__kapasitas = kapasitas
