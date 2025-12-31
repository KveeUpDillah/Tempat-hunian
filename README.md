# [INF2153] Praktikum Pemrograman Web Berorientasi Objek
## Pertemuan 16: Proyek UAS Manajemen Hunian Sementara (Huntara)

### Deskripsi Proyek
Sistem Manajemen Huntara adalah aplikasi berbasis Python yang dirancang untuk membantu pengelolaan hunian sementara (huntara) secara terstruktur dan terintegrasi. Sistem ini bertujuan mempermudah proses pendataan regu, registrasi penghuni, konfirmasi kelayakan, serta pengelolaan area dan hunian dalam satu alur kerja yang jelas.

### Struktur File
UAS_PBO/
- models/
  - __init__.py            : Menandai folder models sebagai package Python
  - regu.py                : Class Regu (data kelompok/anggota)
  - registrasi.py          : Class Registrasi pengajuan hunian
  - konfirmasi.py          : Class Konfirmasi status pendaftaran
  - area.py                : Class Area lokasi hunian
  - hunian.py              : Class Hunian/unit tempat tinggal
  - pengelola.py           : Class Pengelola hunian

- repositories/
  - __init__.py            : Menandai folder repositories sebagai package
  - regu_repo.py           : Penyimpanan & akses data Regu
  - registrasi_repo.py     : Penyimpanan & akses data Registrasi
  - konfirmasi_repo.py     : Penyimpanan & akses data Konfirmasi
  - area_repo.py           : Penyimpanan & akses data Area
  - hunian_repo.py         : Penyimpanan & akses data Hunian

- services/
  - __init__.py            : Menandai folder services sebagai package
  - registrasi_service.py  : Logika bisnis proses pendaftaran
  - konfirmasi_service.py  : Logika bisnis konfirmasi & validasi
  - hunian_service.py      : Logika bisnis pengelolaan hunian

- utils/
  - __init__.py            : Menandai folder utils sebagai package
  - date_helper.py         : Fungsi bantu pengolahan tanggal
  - status_helper.py       : Fungsi bantu status & konstanta

- main.py                  : Entry point aplikasi & penghubung antar layer
- README.md                : Dokumentasi proyek

### Cara menjalankan
1. Pastikan Python 3.x terinstal.
2. Jalankan file utama dari terminal.
    

    ```bash
    python main.py
    ```
