# 🪐 PyKasi 0.2 — Python Bekasi

> **"Coding rasa nongkrong di kalimalang."**
> 👨‍💻 **Lead Developer:** [FARILtau72](https://github.com/FARILtau72)

**PyKasi** adalah interpreter bahasa pemrograman esoterik yang dibangun di atas Python. Tujuannya simpel: Mengganti syntax Python yang kaku jadi bahasa tongkrongan Bekasi yang *valid*. Dibangun dengan arsitektur modular menggunakan **PLY (Python Lex-Yacc)**, bikin code ini enak dibaca developer tapi bikin sakit kepala user kalau sampe error (karena error message-nya ngegas).

## 🗣️ Ngomong Bekasi, ngoding PyKasi

Sintaks utama sekarang pakai `bacot`, `danta`, `kagadanta`, `kaga`, dan operator
kata seperti `tambah`. Lihat [kamus sintaks 0.2](SINTAKS.md) untuk seluruh aturan.

```pykasi
omongan asal gas "Bekasi";
bacot "Woy, " tambah asal tambah "!";
danta paham gas danta;
kalo paham {
    bacot 10000 tambah 5000;
} kaga {
    bacot "Kagadanta? Tanya dulu, bre.";
}
```

`danta` = `True`, `kagadanta` = `False`; kapitalisasi seperti `Kagadanta` juga
boleh. `bacot` = `spill`, `kaga` = `kalo_kaga`. Operator kata: `tambah`, `kurang`,
`kali`, `bagi`, `sisa`, `pangkat`. Sintaks lama tetap didukung; operator kata juga
masih bisa dipakai sebagai nama fungsi/variabel. Empat kata baru `bacot`, `kaga`,
`danta`, dan `kagadanta` kini menjadi kata kunci. Jalankan demo terbaru:
`python main.py bekasi.bks`.

**Fitur-fitur modern PyKasi:**
- ✅ **Function definitions** (`fungsi`) dengan return values
- ✅ **Lists dan dictionaries** untuk data structures
- ✅ **Built-in functions** dengan nama Bekasi (panjang, maks, min, dll)
- ✅ **Loop control** (break/continue atau berhenti/terus)
- ✅ **Try-catch error handling** (coba/tangkep)
- ✅ **Enhanced operators** (==, !=, >=, <=, dll)
- ✅ **Lambda functions** (lamda) untuk functional programming
- ✅ **Python library imports** (impor) untuk akses ekosistem Python
- ✅ **Flask web framework** support untuk bikin web app

## 🌐 Homepage

Homepage PyKasi ada di [`docs/index.html`](docs/index.html), lengkap dengan contoh
sintaks, output, dan panduan mulai. Buka file itu langsung di browser, atau
jalankan `python -m http.server 8000 --directory docs` dari root repository lalu
buka `http://localhost:8000`.

Lihat [panduan homepage](docs/README.md) untuk struktur file dan hosting statis.

---

## 🚀 Tutorial Instalasi (Wajib Baca!)

Ikutin langkah ini biar lu bisa langsung ngoding tanpa drama.

### Syarat Dulu Bre:

1. Pastiin laptop lu udah ada **Python 3.8** ke atas. (Cek pake `python --version`).
2. Pastiin lu punya koneksi internet (buat download library).

### Langkah 1: Clone Repository

Ambil kodingannya dari GitHub Bang Faril. Buka terminal/CMD/Git Bash:

```bash
git clone https://github.com/FARILtau72/pykasi.git
cd pykasi

```

### Langkah 2: Bikin Virtual Environment (Biar Rapi)

*Optional sih, tapi disaranin biar library-nya gak nyampur sama project lain.*

**Buat Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**Buat Mac/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### Langkah 3: Install Jantungnya (Dependencies)

PyKasi butuh library `ply` buat jalan. Ketik ini:

```bash
pip install ply

```

### Langkah 4: Tes Jalan (Running)

Kalo installasi sukses, coba jalanin file contoh yang udah disediain:

```bash
python main.py contoh.bks

```

*Kalau muncul tulisan output, berarti lu udah resmi jadi warga PyKasi!* 🎉

---

## 📂 Bedah Jeroan (Architecture)

Buat lu yang mau kontribusi atau kepo isinya, ini peta strukturnya. Kita pake konsep **Clean Code** & **Modular**.

| File / Folder | Fungsi & Tanggung Jawab |
| --- | --- |
| **`pykasi/`** | **Folder Inti.** Semua otak program ada di sini. |
| ├── `lexer.py` | **Si Pemecah Kata.** Tugasnya baca kode `.bks` lu dan misahin jadi token (Misal: `spill` diubah jadi token `PRINT`). |
| ├── `parser.py` | **Si Polisi Tata Bahasa.** Tugasnya ngecek urutan kode. Kalau abis `kalo` gak ada kondisi, dia yang teriak error. |
| ├── `interpreter.py` | **Si Eksekutor.** Mesin utama yang ngejalanin logika program. Di sini juga tempat nyimpen variabel & error handling "ngegas". |
| **`main.py`** | **Gerbang Utama.** File yang lu panggil di terminal. Dia nyambungin file `.bks` user ke folder `src`. |
| `contoh.bks` | File demo buat pamer syntax. |

---

## 📖 Kamus Gaul (Cheatsheet Syntax)

Jangan sampe salah panggil, nanti dimarahin interpreter.

### Dasar

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `bacot` / `spill` | `print()` | Buat nampilin teks ke layar. |
| `gas` | `=` | Buat masukin nilai ke variabel. |
| `duit` | `int` | Tipe data angka bulat. |
| `omongan` | `string` | Tipe data tulisan/teks. |

### Logika & Loop

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `kalo` | `if` | Kondisi awal. |
| `kaga` / `kalo_kaga` | `else` | Kondisi terakhir (kalau semua salah). |
| `puterin` | `while` | Perulangan selama kondisi valid. |
| `danta` / `valid` | `True` | Benar. |
| `kagadanta` / `hoax` | `False` | Salah. |
| `terus` | `continue` | Lanjut ke iterasi berikutnya. |
| `berhenti` | `break` | Berhenti dari loop. |

### Fungsi (Fitur Baru!)

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `fungsi` | `def` | Buat fungsi. |
| `balikin` | `return` | Kembalikan nilai dari fungsi. |
| `lamda` | `lambda` | Buat fungsi anonim. |

### Data Structures (Fitur Baru!)

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `[1, 2, 3]` | `[1, 2, 3]` | List/Array. |
| `{"key": "val"}` | `{"key": "val"}` | Dictionary/Map. |
| `list[0]` | `list[0]` | Akses elemen list. |

### Error Handling (Fitur Baru!)

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `coba` | `try` | Coba eksekusi kode. |
| `tangkep` | `except` | Tangkap error. |

### Built-in Functions (Fitur Baru!)

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `panjang()` | `len()` | Hitung panjang list/string. |
| `maks()` | `max()` | Cari nilai maksimum. |
| `min()` | `min()` | Cari nilai minimum. |
| `jumlah()` | `sum()` | Jumlahkan semua nilai. |
| `urutkan()` | `sorted()` | Urutkan list. |
| `balik()` | `reversed()` | Balik urutan list. |
| `rentang()` | `range()` | Buat rentang angka. |
| `bentuk()` | `str()` | Konversi ke string. |
| `hitung()` | `int()` | Konversi ke integer. |
| `desimal()` | `float()` | Konversi ke float. |
| `tipe()` | `type()` | Cek tipe data. |

### Operators Lengkap

| Operator | Deskripsi |
| --- | --- |
| `tambah` / `+` | Tambah (angka/string/list). |
| `kurang` / `-` | Kurang (angka). |
| `kali` / `*` | Kali (angka), atau repeat (string/list). |
| `bagi` / `/` | Bagi (angka). |
| `sisa` / `%` | Modulo/sisa bagi (angka). |
| `pangkat` / `**` | Pangkat (angka). |
| `==` | Sama dengan. |
| `!=` | Tidak sama dengan. |
| `>` | Lebih besar. |
| `<` | Lebih kecil. |
| `>=` | Lebih besar atau sama dengan. |
| `<=` | Lebih kecil atau sama dengan. |

### Import Libraries (Fitur Baru!)

| PyKasi | Python Asli | Deskripsi |
| --- | --- | --- |
| `impor module` | `import module` | Import Python module. |
| `impor module sebagai alias` | `import module as alias` | Import dengan alias. |
| `dari module impor func` | `from module import func` | Import function dari module. |
| `module.attribute` | `module.attribute` | Akses attribute/method. |

### Flask Web Framework (Fitur Baru!)

PyKasi sekarang bisa bikin web app pake Flask! Lihat `flask_demo.bks` dan `flask_runner.py` untuk contoh lengkap.

---

## 🧪 Contoh Kodingan

### Contoh Sederhana

Copy kode ini ke file baru, misal `gaji.bks`:

```text
# Hitung sisa duit bulanan

duit gaji gas 5000000;
duit hutang gas 2000000;

kalo gaji > hutang {
    spill "Alhamdulillah, masih bisa napas.";
    sisa gas gaji - hutang;
    spill sisa;
} kalo_kaga {
    spill "Waduh, nyari talangan dulu bre.";
}

```

Jalanin deh:
`python main.py gaji.bks`

### Contoh dengan Fungsi

```text
# Fungsi untuk hitung luas persegi panjang
fungsi hitung_luas(panjang, lebar) {
    balikin panjang * lebar;
}

duit p gas 10;
duit l gas 5;
duit luas gas hitung_luas(p, l);

spill "Luas persegi panjang: ";
spill luas;
```

### Contoh dengan List

```text
# Main-main dengan list
angka gas [1, 2, 3, 4, 5];
spill "List angka: ";
spill angka;

spill "Elemen pertama: ";
spill angka[0];

spill "Panjang list: ";
spill panjang(angka);

spill "Nilai maksimum: ";
spill maks(1, 2, 3, 4, 5);
```

### Contoh Lengkap

Lihat file-file contoh:
- **`fitur_lengkap.bks`** - Demo semua fitur PyKasi (RECOMMENDED!)
- **`fibonacci.bks`** - Deret Fibonacci dengan rekursif
- **`sorting.bks`** - Implementasi bubble sort
- **`flask_demo.bks`** - Demo Flask web framework integration
- **`flask_runner.py`** - Flask web server yang bisa dijalankan

### Contoh Flask Web Development

```bash
# Test Flask integration
python main.py flask_demo.bks

# Run Flask web server
python flask_runner.py
# Buka browser: http://localhost:5000
```

File `flask_demo.bks` mendemonstrasikan:
- Import Flask modules
- Create Flask application
- Use Python libraries (json, datetime)
- Integrate PyKasi functions with Flask

---

## 🤝 Kontribusi

Mau nambahin fitur? Mau bikin error message-nya makin pedes? Gas aja!

1. Fork repo ini.
2. Bikin branch baru (`git checkout -b fitur-gokil`).
3. Commit (`git commit -m 'Nambahin fitur X'`).
4. Push (`git push origin fitur-gokil`).
5. Open Pull Request.

---

**Original Project by [FARILtau72**](https://github.com/FARILtau72)
*Dibuat dengan Python, Kopi, dan Emosi.*
