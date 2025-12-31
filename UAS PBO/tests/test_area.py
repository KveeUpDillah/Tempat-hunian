import unittest
from models.area import Area


class TestArea(unittest.TestCase):

    def setUp(self):
        # Dipanggil sebelum setiap test
        self.area = Area(
            id_area=1,
            nama="Blok A",
            kapasitas=10,
            status="tersedia"
        )

    # ===== Getter Test =====
    def test_get_id_area(self):
        self.assertEqual(self.area.getIdArea(), 1)

    def test_get_nama_area(self):
        self.assertEqual(self.area.getNamaArea(), "Blok A")

    def test_get_kapasitas(self):
        self.assertEqual(self.area.getKapasitas(), 10)

    def test_get_status(self):
        self.assertEqual(self.area.getStatus(), "tersedia")

    # ===== Setter Test =====
    def test_set_nama_area(self):
        self.area.setNamaArea("Blok B")
        self.assertEqual(self.area.getNamaArea(), "Blok B")

    def test_set_kapasitas_valid(self):
        self.area.setKapasitas(20)
        self.assertEqual(self.area.getKapasitas(), 20)

    def test_set_kapasitas_negatif(self):
        with self.assertRaises(ValueError):
            self.area.setKapasitas(-5)

    def test_set_status(self):
        self.area.setStatus("penuh")
        self.assertEqual(self.area.getStatus(), "penuh")


if __name__ == "__main__":
    unittest.main()
