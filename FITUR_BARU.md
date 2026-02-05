# 🎉 PyKasi - Fitur Baru (Versi Bekasi)

## Ringkasan Perubahan

PyKasi sekarang punya fitur-fitur modern dengan gaya bahasa Bekasi yang khas!

## ✨ Fitur Baru yang Ditambahkan

### 1. **Function Definitions** 🔧
```pykasi
fungsi tambah(a, b) {
    balikin a + b;
}

hasil gas tambah(5, 3);  # 8
```

### 2. **Return Statements** 🔄
```pykasi
fungsi faktorial(n) {
    kalo n <= 1 {
        balikin 1;
    }
    balikin n * faktorial(n - 1);
}
```

### 3. **Lists/Arrays** 📋
```pykasi
angka gas [1, 2, 3, 4, 5];
spill angka[0];  # 1

# Modifikasi elemen
angka[0] gas 99;
spill angka;  # [99, 2, 3, 4, 5]
```

### 4. **Dictionaries** 📖
```pykasi
data gas {"nama": "Bekasi", "populasi": 2500000};
```

### 5. **Built-in Functions** 🛠️
- `panjang()` - len()
- `maks()` - max()
- `min()` - min()
- `jumlah()` - sum()
- `urutkan()` - sorted()
- `balik()` - reversed()
- `rentang()` - range()
- `bentuk()` - str()
- `hitung()` - int()
- `desimal()` - float()
- `tipe()` - type()

### 6. **Loop Control** 🔁
```pykasi
puterin i < 10 {
    kalo i == 5 {
        berhenti;  # break
    }
    kalo i == 3 {
        terus;     # continue
    }
    spill i;
}
```

### 7. **Try-Catch Error Handling** 🛡️
```pykasi
coba {
    hasil gas 10 / 2;
    spill hasil;
} tangkep {
    spill "Error terjadi!";
}
```

### 8. **Enhanced Operators** ➕➖✖️➗
- Aritmatika: `+`, `-`, `*`, `/`, `%`, `**`
- Perbandingan: `==`, `!=`, `>`, `<`, `>=`, `<=`
- String/List concatenation dan repetition

### 9. **Lambda Functions** λ
```pykasi
# Lambda untuk functional programming
f gas lamda(x, y) => x + y;
```

### 10. **Python Library Imports** 📦
```pykasi
# Import module
impor math;
pi gas math.pi;

# Import dengan alias
impor datetime sebagai dt;

# Import specific items
dari math impor sqrt, pi;
hasil gas sqrt(25);
```

### 11. **Flask Web Framework** 🌐
```pykasi
# Import Flask
dari flask impor Flask, jsonify;

# Create app
app gas Flask("pykasi_web");

# Use Flask methods
data gas {"status": "success"};
json_response gas jsonify(data);
```

## 📂 File Contoh

1. **contoh.bks** - Contoh singkat PyKasi
2. **kalkulator.bks** - Demo operasi matematika
3. **fitur_lengkap.bks** - Demo SEMUA fitur baru (RECOMMENDED!)
4. **fibonacci.bks** - Deret Fibonacci dengan rekursif
5. **sorting.bks** - Implementasi bubble sort
6. **flask_demo.bks** - Demo Flask web framework integration (NEW!)
7. **flask_runner.py** - Flask web server siap pakai (NEW!)

## 🚀 Cara Pakai

```bash
# Install dependencies
pip install -r requirements.txt

# Jalankan contoh
python main.py fitur_lengkap.bks
python main.py fibonacci.bks
python main.py sorting.bks

# Test Flask integration
python main.py flask_demo.bks

# Run Flask web server
python flask_runner.py
# Buka browser: http://localhost:5000
```

## 🏗️ Arsitektur Perubahan

### Lexer (`lexer.py`)
- Tambah tokens: `FUNGSI`, `BALIKIN`, `LAMDA`, `COBA`, `TANGKEP`, `TERUS`, `BERHENTI`
- Tambah tokens: `LBRACKET`, `RBRACKET`, `COMMA`, `COLON`, `ARROW`
- Tambah operators: `!=`, `>=`, `<=`

### Parser (`parser.py`)
- Tambah node types: `FunctionDef`, `Return`, `FunctionCall`, `List`, `ListAccess`, `ListAssign`, `Dict`, `Lambda`, `TryCatch`, `Continue`, `Break`
- Fix operator precedence untuk evaluasi yang benar
- Tambah grammar rules untuk semua fitur baru

### Interpreter (`interpreter.py`)
- Implementasi execution untuk semua node types baru
- Tambah built-in functions dengan nama Bekasi
- Implementasi function call dengan environment management
- Support list/dict operations
- Exception handling untuk ReturnValue, BreakLoop, ContinueLoop

## 🎯 Kenapa Versi Bekasi?

Terinspirasi dari RenzmcLang yang menggunakan Bahasa Indonesia, PyKasi fokus ke:
- **Bahasa gaul Bekasi** yang authentic
- **Error messages yang ngegas** tapi helpful
- **Syntax yang fun** tapi tetap powerful
- **Modern features** dengan naming lokal

## 🤝 Kompatibilitas

Semua kode PyKasi lama masih jalan! Fitur baru 100% backward compatible.

## 📈 Next Steps (Future Ideas)

- [ ] For loops dengan syntax: `untuk i dalam rentang(10)`
- [ ] List comprehensions: `[x * 2 untuk x dalam [1,2,3]]`
- [ ] String formatting yang lebih advanced
- [ ] File I/O operations
- [ ] Class dan OOP support
- [ ] More Flask features (decorators, templates)
- [ ] Async/await untuk concurrent programming
- [ ] Package manager untuk PyKasi libraries

---

**Dibuat dengan Python, Kopi, dan Semangat Bekasi! ☕🚀**

**Sekarang dengan Flask Web Framework! 🌐**
