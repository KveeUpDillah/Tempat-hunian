from models.regu import Regu


class ReguRepository:
    """
    Repository Regu untuk menyimpan dan mengelola data Regu
    menggunakan struktur data List.

    Attributes:
        __list_regu (list): List yang menyimpan kumpulan objek Regu
                            sebagai media penyimpanan data regu.
    """

    def __init__(self):
        """
        Konstruktor kelas ReguRepository.

        Atribut:
            __list_regu (list): Menyimpan kumpulan objek Regu
                               yang telah ditambahkan ke repository.
        """
        self.__list_regu = []

    def tambah_regu(self, regu: Regu):
        """
        Menambahkan regu baru ke dalam list.

        Args:
            regu (Regu): Objek Regu
        """
        self.__list_regu.append(regu)

    def get_semua_regu(self):
        """
        Mengambil semua data regu.

        Returns:
            list: Daftar objek Regu
        """
        return self.__list_regu

    def get_regu_by_id(self, id_regu):
        """
        Mencari regu berdasarkan ID.

        Args:
            id_regu (int): ID regu

        Returns:
            Regu | None: Objek Regu jika ditemukan, None jika tidak
        """
        for regu in self.__list_regu:
            if regu.getIdRegu() == id_regu:
                return regu
        return None

    def update_regu(self, id_regu, nama_regu=None, anggota=None):
        """
        Mengubah data regu berdasarkan ID.

        Args:
            id_regu (int): ID regu
            nama_regu (str, optional): Nama regu baru
            anggota (list, optional): Daftar anggota baru
        """
        regu = self.get_regu_by_id(id_regu)
        if regu:
            if nama_regu is not None:
                regu.setNamaRegu(nama_regu)
            if anggota is not None:
                regu.setAnggota(anggota)

    def hapus_regu(self, id_regu):
        """
        Menghapus regu berdasarkan ID.

        Args:
            id_regu (int): ID regu
        """
        regu = self.get_regu_by_id(id_regu)
        if regu:
            self.__list_regu.remove(regu)
