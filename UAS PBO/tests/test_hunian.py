import unittest
from models.area import Area
from models.hunian import Hunian


class TestHunian(unittest.TestCase):

    def setUp(self):
        # Membuat objek Area sebagai parent
        self.area = Area(
            id_area=1,
            nama="Area Utama",
            kapasitas=100,
            status="tersedia"
        )

        # Membuat objek Hunian
        self.hunian = Hunian(
            id_hunian=10,
            nama="Hunian A",
            lokasi="Zona 1",
            kapasitas=5,
            area=self.area
        )

    # ===== Test atribut Hunian =====
    def test_get_id_hunian(self):
        self.assertEqual(self.hunian.getIdHunian(), 10)

    def test_get_nama_hunian(self):
        self.assertEqual(self.hunian.getNamaHunian(), "Hunian A")

    def test_get_lokasi(self):
        self.assertEqual(self.hunian.getLokasi(), "Zona 1")

    def test_get_kapasitas_hunian(self):
        self.assertEqual(self.hunian.getKapasitas(), 5)

    # ===== Test setter Hunian =====
    def test_set_nama_hunian(self):
        self.hunian.setNamaHunian("Hunian B")
        self.assertEqual(self.hunian.getNamaHunian(), "Hunian B")

    def test_set_lokasi(self):
        self.hunian.setLokasi("Zona 2")
        self.assertEqual(self.hunian.getLokasi(), "Zona 2")

    def test_set_kapasitas_valid(self):
        self.hunian.setKapasitas(8)
        self.assertEqual(self.hunian.getKapasitas(), 8)

    def test_set_kapasitas_negatif(self):
        with self.assertRaises(ValueError):
            self.hunian.setKapasitas(-1)

    # ===== Test inheritance dari Area =====
    def test_inherit_id_area(self):
        self.assertEqual(self.hunian.getIdArea(), 1)

    def test_inherit_nama_area(self):
        self.assertEqual(self.hunian.getNamaArea(), "Area Utama")

    def test_inherit_status_area(self):
        self.assertEqual(self.hunian.getStatus(), "tersedia")


if __name__ == "__main__":
    unittest.main()
