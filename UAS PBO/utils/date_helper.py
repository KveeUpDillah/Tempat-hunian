def tanggal_valid(tgl_masuk, tgl_keluar):
    """
    Mengecek apakah rentang tanggal valid.
    
    Return:
        bool: True jika tanggal keluar >= tanggal masuk
    """
    return tgl_keluar >= tgl_masuk


def hitung_lama_tinggal(tgl_masuk, tgl_keluar):
    """
    Menghitung lama tinggal dalam satuan hari.

    Return:
        int: Jumlah hari tinggal
    """
    return (tgl_keluar - tgl_masuk).days
