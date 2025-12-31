import unittest
from models.pengelola import Pengelola


class TestPengelola(unittest.TestCase):

    def setUp(self):
        self.pengelola = Pengelola(
            id_petugas=101,
            nama="Budi Santoso",
            jabatan="Koordinator Lapangan"
        )

    # ===== Getter Test =====
    def test_get_id_petugas(self):
        self.assertEqual(self.pengelola.getIdPetugas(), 101)

    def test_get_nama(self):
        self.assertEqual(self.pengelola.getNama(), "Budi Santoso")

    def test_get_jabatan(self):
        self.assertEqual(self.pengelola.getJabatan(), "Koordinator Lapangan")

    # ===== Setter Test =====
    def test_set_nama(self):
        self.pengelola.setNama("Andi Wijaya")
        self.assertEqual(self.pengelola.getNama(), "Andi Wijaya")

    def test_set_jabatan(self):
        self.pengelola.setJabatan("Supervisor")
        self.assertEqual(self.pengelola.getJabatan(), "Supervisor")


if __name__ == "__main__":
    unittest.main()
