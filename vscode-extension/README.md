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
- `valid` / `hoax` - boolean type
- `gudang` - list
- `catetan` - dictionary

### I/O & Import
- `spill` - print
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
   - Pilih file `pykasi-language-1.0.0.vsix`

## Cara Pakai

1. Buat file baru dengan ekstensi `.bks` (contoh: `program.bks`)
2. VS Code akan otomatis mendeteksi sebagai PyKasi
3. Mulai coding dengan syntax PyKasi!

### Contoh Program

```pykasi
# Ini adalah komentar
spill "Halo dari PyKasi!";

duit angka GAS 10;
omongan nama GAS "Bekasi";

kalo angka > 5 {
    spill "Angka lebih besar dari 5";
} kalo_kaga {
    spill "Angka kecil atau sama dengan 5";
}

puterin angka > 0 {
    spill angka;
    angka GAS angka - 1;
}

fungsi tambah(a, b) {
    balikin a + b;
}

spill tambah(5, 3);
```

## Snippets Cepat

Ketik prefix berikut lalu tekan Tab:

| Prefix | Deskripsi |
|--------|-----------|
| `spill` | Print statement |
| `gas` | Variable assignment |
| `kalo` | If statement |
| `kaloelse` | If-else statement |
| `puterin` | While loop |
| `fungsi` | Function definition |
| `coba` | Try-catch block |
| `duit` | Numeric variable |
| `omongan` | String variable |
| `valid` | Boolean variable |

## License

MIT License

## Repository

[https://github.com/pykasi/pykasi](https://github.com/pykasi/pykasi)
