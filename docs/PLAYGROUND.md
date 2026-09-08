# PyKasi Playground

Playground adalah editor PyKasi yang berjalan langsung di browser, langsung di
[homepage PyKasi](index.html#playground). Jalankan server lokal:

```sh
python -m http.server 8000 --directory docs
```

Lalu buka `http://localhost:8000/#playground`.

## Cara pakai

1. Tulis atau ubah kode di panel kiri.
2. Tekan **Run code** atau `Ctrl/Cmd + Enter`.
3. Baca hasil atau pesan error di panel kanan.
4. Pakai **Reset** untuk kembali ke contoh awal.
5. Pilih template di bawah editor untuk memuat contoh baru.
6. Tekan **Bagikan kode** untuk menyalin URL berisi kode saat ini.

Kode dibaca dan dijalankan di perangkat pengunjung. Tidak ada backend dan kode
tidak dikirim ke server.

## Sintaks yang didukung

| Kelompok | Dukungan playground |
| --- | --- |
| Output & variabel | `bacot`, `spill`, `gas`, `duit`, `omongan`, `danta` |
| Boolean | `danta`, `kagadanta`, `valid`, `hoax` |
| Operator | simbol dan `tambah`, `kurang`, `kali`, `bagi`, `sisa`, `pangkat` |
| Kontrol alur | `kalo` / `kaga`, `puterin`, `terus`, `berhenti` |
| Fungsi | `fungsi`, `balikin`, pemanggilan fungsi |
| Data | list dan dictionary literal |
| Built-in | `panjang`, `jumlah`, `maks`, `min`, `urutkan`, `balik`, `rentang`, `bentuk`, `hitung`, `desimal`, `tipe` |

Playground menggunakan interpreter JavaScript kecil yang sengaja dibatasi untuk
belajar dan percobaan cepat. Referensi bahasa utama tetap [SINTAKS.md](../SINTAKS.md).

## Yang perlu dijalankan lokal

Fitur di bawah belum tersedia di playground karena membutuhkan runtime Python:

- `impor`, `dari ... impor`, dan akses modul Python
- Flask dan `flask_runner.py`
- `coba` / `tangkep`, `lamda`, akses indeks, assignment indeks, serta pemanggilan method

Untuk fitur tersebut, buat file `.bks` dan jalankan:

```sh
python main.py nama_file.bks
```

## Catatan link berbagi

Kode dibungkus dalam bagian `#` pada URL. Link cocok untuk contoh pendek sampai
menengah; untuk program yang lebih besar, simpan sebagai file `.bks` dan unggah ke
repository atau gist.
