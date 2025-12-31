import unittest
from datetime import datetime, timedelta
from models.area import Area
from models.konfirmasi import Konfirmasi


class TestKonfirmasi(unittest.TestCase):

    def setUp(self):
        # Objek Area dummy untuk testing
        self.area = Area(
            id_area=1,
            nama="Area Hunian A",
            kapasitas=20,
            status="tersedia"
        )

        # Catat waktu sebelum membuat konfirmasi
        self.waktu_sebelum = datetime.now()

        # Objek Konfirmasi
        self.konfirmasi = Konfirmasi(
            lama_tinggal=7,
            area=self.area,
            keterangan="Hunian sementara untuk regu A"
        )

        # Catat waktu setelah membuat konfirmasi
        self.waktu_setelah = datetime.now()

    # ===== Getter Test =====
    def test_get_lama_tinggal(self):
        self.assertEqual(self.konfirmasi.getLamaTinggal(), 7)

    def test_get_area_hunian(self):
        self.assertEqual(self.konfirmasi.getAreaHunian(), self.area)

    def test_get_keterangan(self):
        self.assertEqual(
            self.konfirmasi.getKeterangan(),
            "Hunian sementara untuk regu A"
        )

    def test_get_waktu_konfirmasi(self):
        waktu_konfirmasi = self.konfirmasi.getWaktuKonfirmasi()

        # Pastikan waktu konfirmasi berada di antara sebelum & sesudah
        self.assertTrue(
            self.waktu_sebelum <= waktu_konfirmasi <= self.waktu_setelah
        )

    # ===== Setter Test =====
    def test_set_lama_tinggal(self):
        self.konfirmasi.setLamaTinggal(14)
        self.assertEqual(self.konfirmasi.getLamaTinggal(), 14)

    def test_set_area_hunian(self):
        area_baru = Area(
            id_area=2,
            nama="Area Hunian B",
            kapasitas=30,
            status="tersedia"
        )
        self.konfirmasi.setAreaHunian(area_baru)
        self.assertEqual(self.konfirmasi.getAreaHunian(), area_baru)

    def test_set_keterangan(self):
        self.konfirmasi.setKeterangan("Perpanjangan hunian")
        self.assertEqual(
            self.konfirmasi.getKeterangan(),
            "Perpanjangan hunian"
        )


if __name__ == "__main__":
    unittest.main()
