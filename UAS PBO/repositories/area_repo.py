from models.area import Area


class AreaRepository:
    """
    Repository Area untuk menyimpan dan mengelola data Area
    menggunakan struktur data List.

    Attributes:
        __list_area (list of Area): List yang menyimpan seluruh
                                    objek Area dalam sistem.
    """

    def __init__(self):
        """
        Konstruktor AreaRepository.

        Menginisialisasi repository dengan list kosong
        sebagai media penyimpanan data Area.
        """
        self.__list_area = []

    def tambah_area(self, area: Area):
        """
        Menambahkan data area baru ke dalam repository.

        Args:
            area (Area): Objek Area yang akan disimpan.
        """
        self.__list_area.append(area)

    def get_semua_area(self):
        """
        Mengambil seluruh data area.

        Returns:
            list: Daftar objek Area.
        """
        return self.__list_area

    def get_area_by_id(self, id_area):
        """
        Mencari area berdasarkan ID.

        Args:
            id_area (int): ID area.

        Returns:
            Area | None: Objek Area jika ditemukan,
                         None jika tidak ditemukan.
        """
        for area in self.__list_area:
            if area.getIdArea() == id_area:
                return area
        return None

    def update_area(self, id_area, nama_area=None, kapasitas=None, status=None):
        """
        Memperbarui data area berdasarkan ID.

        Args:
            id_area (int): ID area.
            nama_area (str, optional): Nama baru area.
            kapasitas (int, optional): Kapasitas baru area.
            status (str, optional): Status baru area.
        """
        area = self.get_area_by_id(id_area)
        if area:
            if nama_area is not None:
                area.setNamaArea(nama_area)
            if kapasitas is not None:
                area.setKapasitas(kapasitas)
            if status is not None:
                area.setStatus(status)

    def hapus_area(self, id_area):
        """
        Menghapus data area berdasarkan ID.

        Args:
            id_area (int): ID area.
        """
        area = self.get_area_by_id(id_area)
        if area:
            self.__list_area.remove(area)
