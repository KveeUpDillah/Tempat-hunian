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
        """
        Mengembalikan lama tinggal atau penggunaan area (dalam hari).
        
        Returns:
            int: Lama tinggal dalam hari.
        """
        return self.__lamaTinggal

    def getArea(self):
        """
        Mengembalikan objek Area yang dikonfirmasi.
        
        Returns:
            Area: Objek area terkait.
        """
        return self.__area

    def getKeterangan(self):
        """
        Mengembalikan keterangan tambahan terkait konfirmasi.
        
        Returns:
            str: Keterangan konfirmasi.
        """
        return self.__keterangan

    # Setter
    def setLamaTinggal(self):
        """
        Mengubah lama tinggal.

        Args:
            hari(int): Lama tinggal baru.
        """
        return self.__lamaTinggal
        
    def setArea(self):
        """
        Mengubah area yang akan ditempati.

        Args:
            area(Area): Area baru.
        """
        return self.__area
    
    def setKeterangan(self):
        """
        Mengubah keterangan atau catatan tambahan.
        
        Args:
            ket(str): Keterangan baru.
        """
        return self.__keterangan
