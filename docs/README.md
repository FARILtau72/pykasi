# Homepage PyKasi

Homepage statis berbahasa Indonesia untuk mengenalkan PyKasi, menampilkan contoh
sintaks beserta output, dan memandu instalasi dari repository. Tidak membutuhkan
Node.js, proses build, CDN, atau backend. Logo disalin dari `assets/logo.svg` di
root repository supaya folder ini dapat di-host secara mandiri.

## Buka lokal

Buka `docs/index.html` langsung di browser. Untuk memakai server lokal dari root
repository:

```sh
python -m http.server 8000 --directory docs
```

Lalu buka `http://localhost:8000`. Hanya folder `docs/` yang perlu disajikan.

## Interaksi

- Pilih salah satu dari empat tab contoh: kenalan, danta/kagadanta, perulangan, atau fungsi.
- Navigasi tab memakai klik, panah kiri/kanan, Home, atau End. Kode dan output
  berdampingan di layar lebar dan bertumpuk di layar kecil.
- Tombol salin menyalin contoh yang aktif atau perintah instalasi.
- Jika Clipboard API tidak tersedia atau izin ditolak, teks dipilih dan panduan
  menyalin manual ditampilkan.
- Tanpa JavaScript, keempat contoh, output, tabel sintaks, panduan instalasi, dan
  navigasi tetap tersedia. Kontrol yang membutuhkan JavaScript disembunyikan.
- Output adalah hasil contoh yang sudah ditentukan, bukan eksekusi interpreter
  di browser. Untuk menjalankan atau mengubah kode, gunakan interpreter Python.

## Hosting

Folder `docs/` siap untuk hosting statis, termasuk GitHub Pages. Ada dua pilihan
sumber GitHub Pages dari branch `main`:

- `/docs`: langsung menyajikan homepage.
- `/ (root)`: `index.html` di root mengarahkan pengunjung ke `docs/index.html`.
  File `.nojekyll` di root memastikan file statis disajikan apa adanya, sehingga
  halaman utama tidak lagi dibuat dari README oleh Jekyll.

Pengalihan dari root mempertahankan query string dan anchor (misalnya `#mulai`)
ketika JavaScript aktif. Tanpa JavaScript, meta refresh menuju homepage; tombol
tautan tetap tersedia jika browser memblokir pengalihan otomatis. Tampilan utama
tetap dipelihara di satu tempat, yaitu `docs/index.html`.

Perubahan ini tidak mengaktifkan hosting atau mengubah pengaturan repository
secara otomatis. Jika Pages sudah menyajikan root, pengalihan berlaku setelah
commit yang memuatnya selesai dipublikasikan oleh Pages.

Seluruh URL aset bersifat relatif sehingga homepage bisa disajikan di root domain
maupun subpath seperti `/pykasi/`.

## Playground

Playground pada `index.html#playground` adalah editor PyKasi di browser untuk mencoba sintaks inti tanpa
install Python. Ia mendukung output, variabel, kondisi, perulangan, fungsi, list,
dictionary, serta operator Bekasi seperti `tambah`, `kali`, dan `bagi`.

Import dan Flask tetap perlu interpreter Python lokal. Playground sengaja berjalan
sepenuhnya di perangkat pengunjung.

Panduan penggunaan, sintaks yang didukung, dan batasan browser ada di
[PLAYGROUND.md](PLAYGROUND.md).

## Struktur

- `index.html`: konten, contoh kode, output, dan metadata halaman.
- `assets/style.css`: tema, layout responsif, fokus keyboard, dan reduced motion.
- `assets/main.js`: pemilihan contoh serta penyalinan teks.
- `assets/playground.*`: editor, output, dan interpreter browser yang dipakai homepage.
- `assets/logo.svg`: logo PyKasi yang sudah ada.
- `.nojekyll`: menyajikan file statis apa adanya di GitHub Pages.

Saat mengganti contoh, jalankan teks di dalam `[data-source]` dengan
`pykasi.run_text` dan cocokkan stdout dengan `[data-output]` pada panel yang sama.
Periksa sintaks JavaScript dengan `node --check docs/assets/main.js`.

Homepage memakai sintaks PyKasi 0.2 dari [SINTAKS.md](../SINTAKS.md). Langkah
instalasi terakhir menjalankan `bekasi.bks`. Uji contoh dan snippet tersedia pada
`tests/test_bekasi_syntax.py`.
