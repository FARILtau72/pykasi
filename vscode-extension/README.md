# PyKasi VS Code Extension

Ekstensi VS Code untuk bahasa pemrograman **PyKasi** - bahasa pemrograman dengan syntax yang mudah dipahami orang Indonesia.

## Fitur

- 🎨 **Syntax Highlighting** - Pewarnaan syntax untuk semua keyword PyKasi
- 📝 **Code Snippets** - Snippets cepat untuk keyword umum (spill, gas, kalo, puterin, dll)
- 🌙 **Dark Theme** - Tema khusus PyKasi Dark dengan warna yang nyaman di mata
- 🔧 **Auto Closing** - Otomatis menutup bracket, parentheses, dan quotes
- 📋 **Language Configuration** - Konfigurasi lengkap untuk file `.bks`

## Keyword yang Didukung

### Control Flow
- `kalo` / `kalo_kaga` - if / else
- `puterin` - while loop
- `terus` - continue
- `berhenti` - break

### Functions
- `fungsi` - function definition
- `balikin` - return
- `lamda` - lambda function

### Variables & Types
- `gas` - assignment
- `duit` - numeric type
- `omongan` - string type
- `danta` / `kagadanta` - True / False; `valid` / `hoax` tetap didukung
- List: `angka gas [1, 2, 3];`
- Dictionary: `data gas {"asal": "Bekasi"};`

### I/O & Import
- `bacot` / `spill` - print
- `tambah`, `kurang`, `kali`, `bagi`, `sisa`, `pangkat` - operator aritmatika
- `impor` / `dari` / `sebagai` - import statements

### Error Handling
- `coba` / `tangkep` - try / catch

## Cara Install

### Development Mode

1. Buka folder `vscode-extension` di VS Code
2. Tekan `F5` untuk menjalankan extension development host
3. Atau jalankan:
   ```bash
   cd vscode-extension
   npm install
   code .
   ```

### Packaged Extension (.vsix)

1. Install dependencies:
   ```bash
   npm install -g @vscode/vsce
   ```

2. Package extension:
   ```bash
   vsce package
   ```

3. Install the .vsix file:
   - Buka VS Code
   - Extensions panel (Ctrl+Shift+X)
   - Klik menu (...) → "Install from VSIX..."
   - Pilih file `pykasi-language-1.1.0.vsix`

## Cara Pakai

1. Buat file baru dengan ekstensi `.bks` (contoh: `program.bks`)
2. VS Code akan otomatis mendeteksi sebagai PyKasi
3. Mulai coding dengan syntax PyKasi!

### Contoh Program

```pykasi
# Ini adalah komentar
bacot "Woy, Bekasi!";

duit angka gas 10;
omongan nama gas "Bekasi";

kalo angka > 5 {
    spill "Angka lebih besar dari 5";
} kaga {
    spill "Angka kecil atau sama dengan 5";
}

puterin angka > 0 {
    spill angka;
    angka gas angka - 1;
}

fungsi tambah(a, b) {
    balikin a tambah b;
}

spill tambah(5, 3);
```

## Snippets Cepat

Ketik prefix berikut lalu tekan Tab:

| Prefix | Deskripsi |
|--------|-----------|
| `bacot` / `spill` | Print statement |
| `gas` | Variable assignment |
| `kalo` | If statement |
| `kaloelse` | If-else statement |
| `puterin` | While loop |
| `fungsi` | Function definition |
| `coba` | Try-catch block |
| `duit` | Numeric variable |
| `omongan` | String variable |
| `danta` / `valid` | Boolean variable |
| `kagadanta` | Nilai False |
| `tambah` | Penjumlahan |

## License

MIT License

## Repository

[https://github.com/FARILtau72/pykasi](https://github.com/FARILtau72/pykasi)

## Sintaks 0.2

Lihat [kamus PyKasi](../SINTAKS.md). `danta` dan `kagadanta` menerima kapitalisasi
seperti `Danta` atau `Kagadanta`; kata kunci lain memakai huruf kecil.
Snippet menghasilkan `gas` huruf kecil dan komentar `#`. List/dictionary
menggunakan assignment biasa; sintaks for-in dan komentar blok belum didukung
interpreter sehingga tidak ditawarkan sebagai snippet.

Operator kata juga tetap bisa menjadi nama fungsi/variabel, misalnya
`fungsi tambah(a, b) { balikin a tambah b; }`.
