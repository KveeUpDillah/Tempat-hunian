import unittest
from models.regu import Regu

class TestRegu(unittest.TestCase):

    def setUp(self):
        self.regu = Regu(1, "Regu A", [])

    def test_get_id_regu(self):
        self.assertEqual(self.regu.getIdRegu(), 1)

    def test_get_nama_regu(self):
        self.assertEqual(self.regu.getNamaRegu(), "Regu A")

    def test_set_nama_regu(self):
        self.regu.setNamaRegu("Regu Baru")
        self.assertEqual(self.regu.getNamaRegu(), "Regu Baru")

    def test_set_anggota(self):
        anggota = ["Andi", "Budi"]
        self.regu.setAnggota(anggota)
        self.assertEqual(self.regu.getAnggota(), anggota)

if __name__ == "__main__":
    unittest.main()
