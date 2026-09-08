# 🪐 PyKasi 0.2 — Python Bekasi

> *Coding rasa nongkrong di Kalimalang.*

PyKasi adalah bahasa pemrograman esoterik berbasis Python yang memakai kosakata
Bekasi untuk belajar konsep pemrograman. Tulis `bacot`, `danta`, `kagadanta`, dan
`tambah`; interpreter akan menjalankannya lewat Python + PLY.

## Mulai dari sini

- **Coba langsung di browser:** [Homepage PyKasi → Playground](docs/index.html#playground)
- **Kamus sintaks lengkap:** [SINTAKS.md](SINTAKS.md)
- **Panduan playground:** [docs/PLAYGROUND.md](docs/PLAYGROUND.md)

```pykasi
omongan asal gas "Bekasi";
duit patungan gas 10000 tambah 5000;

bacot "Woy, " tambah asal tambah "!";
bacot patungan;
```

```text
Woy, Bekasi!
15000
```

## Fitur

- Variabel bertipe: `duit`, `omongan`, dan `danta`
- Output dengan `bacot` (alias lama: `spill`)
- Percabangan `kalo` / `kaga`, perulangan `puterin`
- Fungsi, `balikin`, `terus`, dan `berhenti`
- List, dictionary, index, serta assignment index
- Lambda (`lamda`), `coba` / `tangkep`, dan built-in bahasa Bekasi
- Import Python dengan allowlist aman, termasuk Flask untuk demo lokal
- Operator Bekasi: `tambah`, `kurang`, `kali`, `bagi`, `sisa`, `pangkat`

## Instalasi

PyKasi memerlukan Python 3.8 atau lebih baru.

```sh
git clone https://github.com/FARILtau72/pykasi.git
cd pykasi
python -m venv .venv
```

Aktifkan virtual environment:

```sh
# Windows PowerShell
.venv\Scripts\Activate.ps1

# Windows CMD
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

Lalu pasang dependency dan jalankan contoh:

```sh
python -m pip install -r requirements.txt
python main.py bekasi.bks
```

Alternatif untuk memasang command `pykasi`:

```sh
python -m pip install -e .
pykasi bekasi.bks
pykasi --eval 'bacot 2 tambah 3;'
```

## Cara menjalankan kode

Simpan program dengan ekstensi `.bks`, kemudian jalankan dari root repository:

```sh
python main.py nama_file.bks
```

Kalau memakai package CLI:

```sh
pykasi nama_file.bks
pykasi -e 'bacot "Woy, Bekasi!";'
```

Contoh yang tersedia:

| File | Isi |
| --- | --- |
| `bekasi.bks` | Sintaks Bekasi 0.2 yang paling baru |
| `contoh.bks` | Dasar PyKasi |
| `fitur_lengkap.bks` | Ringkasan fitur utama |
| `fibonacci.bks` | Rekursi dan fungsi |
| `sorting.bks` | Bubble sort |
| `kalkulator.bks` | Aritmatika |
| `python_libs.bks` | Import library Python yang diizinkan |
| `flask_demo.bks` | Integrasi Flask lokal |

## Sintaks cepat

| Tujuan | Tulis di PyKasi |
| --- | --- |
| Cetak nilai | `bacot "Woy!";` |
| Angka | `duit umur gas 16;` |
| Teks | `omongan kota gas "Bekasi";` |
| Boolean | `danta paham gas danta;` |
| Kondisi | `kalo paham { ... } kaga { ... }` |
| Loop | `puterin umur < 18 { ... }` |
| Fungsi | `fungsi sapa(nama) { balikin nama; }` |
| List | `angka gas [1, 2, 3];` |
| Dictionary | `data gas {"kota": "Bekasi"};` |

`danta` berarti `True`; `kagadanta` berarti `False`. Boolean itu tidak peka huruf
besar/kecil, jadi `Kagadanta` tetap valid. Referensi lengkap beserta aturan,
built-in, dan contoh lanjutan ada di [SINTAKS.md](SINTAKS.md).

## Playground browser

Playground ada langsung di homepage (`docs/index.html#playground`) dan bisa di-host sebagai static site.
Ia berjalan seluruhnya di browser, tanpa mengirim kode ke server. Gunakan untuk
mencoba sintaks inti, template contoh, shortcut **Ctrl/Cmd + Enter**, atau membuat
link berbagi kode. Import Python dan Flask harus dijalankan lewat interpreter
lokal. Detail fitur dan batasannya ada di [docs/PLAYGROUND.md](docs/PLAYGROUND.md).

Untuk membuka homepage + playground secara lokal:

```sh
python -m http.server 8000 --directory docs
```

Buka `http://localhost:8000`, lalu pilih **Playground**.

## Struktur proyek

| Lokasi | Peran |
| --- | --- |
| `pykasi/lexer.py` | Mengubah teks `.bks` menjadi token |
| `pykasi/parser.py` | Membentuk struktur program dan memeriksa tata bahasa |
| `pykasi/interpreter.py` | Mengeksekusi program, built-in, tipe, dan import aman |
| `pykasi/cli.py` | Command `pykasi` |
| `main.py` | Titik masuk sederhana untuk `python main.py file.bks` |
| `tests/` | Uji regresi syntax dan program contoh |
| `docs/` | Homepage statis, playground, dan dokumentasi web |
| `vscode-extension/` | Grammar dan snippet VS Code |

## Import dan keamanan

`impor` hanya menerima nama modul Python yang valid dan dibatasi allowlist.
Modul seperti `os`, `sys`, `subprocess`, `eval`, dan `exec` ditolak. Ini membantu
menjaga demo PyKasi tetap aman; lihat daftar modul yang diizinkan di
`pykasi/interpreter.py` sebelum menambahkan ketergantungan baru.

## Pengembangan dan kontribusi

Jalankan test setelah mengubah lexer, parser, atau interpreter:

```sh
python -m unittest discover -s tests
```

Alur kontribusi:

1. Fork repository lalu buat branch dari `main`.
2. Tambahkan atau perbarui test yang relevan.
3. Jalankan test dan contoh `.bks` terkait.
4. Perbarui [SINTAKS.md](SINTAKS.md) jika perilaku bahasa berubah.
5. Buka pull request dengan ringkasan perubahan dan contoh output.

## Lisensi

MIT. Dibuat oleh [FARILtau72](https://github.com/FARILtau72).
