# Sintaks PyKasi 0.2

PyKasi pakai kosakata tongkrongan Bekasi: `bacot` buat menampilkan teks,
`danta` buat benar, `kagadanta` buat salah, dan `tambah` buat penjumlahan.
Semua contoh di sini dijalankan oleh interpreter Python yang ada di repository.

## Kamus utama

| PyKasi | Makna | Bentuk lama yang tetap didukung |
| --- | --- | --- |
| `bacot` | Menampilkan nilai ke layar | `spill` |
| `gas` | Memberi nilai ke variabel | `gas` |
| `danta` | Boolean benar (`True`) | `valid` |
| `kagadanta` | Boolean salah (`False`) | `hoax` |
| `kalo` | Percabangan `if` | `kalo` |
| `kaga` | Cabang `else` | `kalo_kaga` |
| `puterin` | Perulangan `while` | `puterin` |
| `fungsi` / `balikin` | Membuat fungsi / mengembalikan nilai | Tetap sama |
| `terus` / `berhenti` | `continue` / `break` di dalam loop | Tetap sama |

Boolean baru menerima kapitalisasi apa pun: `danta`, `Danta`, `DANTA`,
`kagadanta`, dan `Kagadanta` dikenali. Kata kunci lain ditulis huruf kecil;
nama variabel tetap peka huruf besar/kecil. Output boolean masih menggunakan
representasi Python, yaitu `True` dan `False`.

## Ngomong dan hitung

```pykasi
omongan asal gas "Bekasi";
bacot "Woy, " tambah asal tambah "!";
duit patungan gas 10000 tambah 5000;
bacot patungan;
```

Output:

```text
Woy, Bekasi!
15000
```

| Operator kata | Simbol | Contoh | Hasil |
| --- | --- | --- | --- |
| `tambah` | `+` | `10 tambah 5` | `15` |
| `kurang` | `-` | `10 kurang 3` | `7` |
| `kali` | `*` | `4 kali 3` | `12` |
| `bagi` | `/` | `12 bagi 4` | `3.0` |
| `sisa` | `%` | `17 sisa 5` | `2` |
| `pangkat` | `**` | `2 pangkat 3` | `8` |

Urutan operasi sama dengan versi simbol: pangkat lebih dulu, lalu kali/bagi/sisa,
lalu tambah/kurang. Pangkat mengelompok dari kanan. Gunakan tanda kurung untuk
mengubah urutan. Operator kata dan simbol boleh dicampur.

`tambah` juga menggabungkan dua string atau dua list; `kali` bisa mengulang
string/list dengan angka bulat di sebelah kanan. Dua jenis yang tidak cocok
(misalnya string ditambah angka) menghasilkan error, sama seperti operator lama.

## Danta atau kagadanta?

```pykasi
danta paham gas danta;
kalo paham {
    bacot "Danta, bre. Gas lanjut!";
} kaga {
    bacot "Kagadanta? Tanya dulu, bre.";
}

paham gas Kagadanta;
kalo paham {
    bacot "Udah paham.";
} kaga {
    bacot "Santai, belajar lagi.";
}
```

`danta paham gas danta;` mendeklarasikan variabel bertipe boolean. Deklarasi
`paham gas danta;` tanpa tipe juga bisa. Deklarasi bertipe menolak penugasan
ulang yang bukan boolean. `kaga` adalah `else`, bukan operator negasi.

## Fungsi dan nama lama

```pykasi
fungsi tambah(a, b) {
    balikin a tambah b;
}
bacot tambah(2, 3);

duit sisa gas 17 sisa 5;
bacot sisa;
```

Outputnya `5`, lalu `2`. Operator kata bersifat kontekstual: `tambah` pada posisi
operator berarti `+`, tetapi masih bisa menjadi nama fungsi, parameter, variabel,
atau atribut. Contoh lama yang memakai nama `tambah`, `kali`, atau `sisa` tetap
dapat dijalankan. Kata baru `bacot`, `kaga`, `danta`, dan `kagadanta` menjadi kata
kunci; ganti namanya jika sebelumnya dipakai sebagai identifier.

## Perulangan

```pykasi
duit putaran gas 1;
puterin putaran <= 3 {
    bacot putaran;
    putaran gas putaran tambah 1;
}
```

Pakai `;` untuk menutup pernyataan sederhana, `{ ... }` untuk blok, dan `#` untuk
komentar. Blok harus berisi setidaknya satu pernyataan. Simpan kode sebagai `.bks`.

## Jalankan contoh lengkap

```sh
python main.py bekasi.bks
```

Sintaks lama seperti `spill`, `valid`, `hoax`, `kalo_kaga`, dan operator simbol
tetap tersedia. Tidak perlu mengubah program lama kecuali program itu memakai
empat kata kunci baru sebagai nama. Fitur import, list, dictionary, fungsi,
lambda, dan error handling mengikuti [dokumentasi utama](README.md).
