import unittest
from datetime import date
from models.registrasi import Registrasi


class TestRegistrasi(unittest.TestCase):

    def setUp(self):
        self.registrasi = Registrasi(
            id_registrasi=1001,
            tgl_masuk=date(2025, 1, 1),
            tgl_keluar=date(2025, 1, 10),
            status="aktif"
        )

    # ===== Getter Test =====
    def test_get_id_registrasi(self):
        self.assertEqual(self.registrasi.getIdRegistrasi(), 1001)

    def test_get_tgl_masuk(self):
        self.assertEqual(self.registrasi.getTglMasuk(), date(2025, 1, 1))

    def test_get_tgl_keluar(self):
        self.assertEqual(self.registrasi.getTglKeluar(), date(2025, 1, 10))

    def test_get_status(self):
        self.assertEqual(self.registrasi.getStatus(), "aktif")

    # ===== Setter Test =====
    def test_set_tgl_masuk(self):
        tgl_baru = date(2025, 2, 1)
        self.registrasi.setTglMasuk(tgl_baru)
        self.assertEqual(self.registrasi.getTglMasuk(), tgl_baru)

    def test_set_tgl_keluar(self):
        tgl_baru = date(2025, 2, 15)
        self.registrasi.setTglKeluar(tgl_baru)
        self.assertEqual(self.registrasi.getTglKeluar(), tgl_baru)

    def test_set_status(self):
        self.registrasi.setStatus("selesai")
        self.assertEqual(self.registrasi.getStatus(), "selesai")


if __name__ == "__main__":
    unittest.main()
