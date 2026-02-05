# 🎉 PyKasi - Update Lengkap!

## Apa yang Baru?

PyKasi sekarang punya fitur **IMPORT LIBRARIES**, **FLASK WEB FRAMEWORK**, dan **SECURITY IMPROVEMENTS**! 🚀🔒

---

## 🆕 Fitur Baru

### 1. Python Library Imports 📦

Sekarang lu bisa import library Python yang AMAN!

**PENTING:** Untuk keamanan, hanya module tertentu yang diizinkan. Lihat `SECURITY.md` untuk daftar lengkap.

**Syntax:**
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

**Supported:**
- ✅ Access module attributes: `math.pi`
- ✅ Call module functions: `math.sqrt(16)`
- ✅ Method calls: `json.dumps(data)`
- ✅ Semua Python standard libraries!

### 2. Flask Web Framework 🌐

Bikin web app pake PyKasi!

**Example:**
```pykasi
# Import Flask
dari flask impor Flask, jsonify;

# Create app
app gas Flask("pykasi_web");

# Use Flask methods
data gas {"status": "Gas terus!"};
response gas jsonify(data);
```

**File Examples:**
- `flask_demo.bks` - Integration demo
- `flask_runner.py` - Working web server

### 3. Dictionary Access 📋

Sekarang bisa akses dictionary dengan syntax Python:

```pykasi
data gas {"nama": "PyKasi", "kota": "Bekasi"};
nama gas data["nama"];  # Works!
```

---

## 📂 File-File Penting

### Examples (.bks)
1. **contoh.bks** - Basic PyKasi
2. **kalkulator.bks** - Math operations
3. **fitur_lengkap.bks** - All PyKasi features
4. **fibonacci.bks** - Recursive functions
5. **sorting.bks** - Bubble sort algorithm
6. **python_libs.bks** - 8+ Python libraries demo (NEW!)
7. **flask_demo.bks** - Flask integration (NEW!)

### Web Server
- **flask_runner.py** - Flask web server (NEW!)

---

## 🚀 Quick Start

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Examples
```bash
# Test Python libraries
python main.py python_libs.bks

# Test Flask integration
python main.py flask_demo.bks

# Run web server
python flask_runner.py
# Open: http://localhost:5000
```

---

## 💡 Examples

### Import Math Library
```pykasi
impor math;

spill "π = ";
spill math.pi;

spill "√144 = ";
spill math.sqrt(144);
```

### Import Multiple Items
```pykasi
dari random impor randint, choice;

angka gas randint(1, 100);
spill angka;

pilihan gas ["A", "B", "C"];
hasil gas choice(pilihan);
spill hasil;
```

### Flask Web App
```pykasi
dari flask impor Flask;

app gas Flask("my_app");
spill "Flask app created!";
spill app.name;
```

### JSON Operations
```pykasi
impor json;

data gas {"nama": "PyKasi", "versi": "1.0"};
json_str gas json.dumps(data);
spill json_str;

parsed gas json.loads(json_str);
spill parsed["nama"];
```

---

## 🎯 Yang Berubah

### Syntax Baru
- `impor module` - Import module
- `impor module sebagai alias` - Import with alias
- `dari module impor item1, item2` - Import specific items
- `module.attribute` - Access attributes
- `object.method()` - Call methods
- `dict[key]` - Dictionary access

### Operator Precedence
- DOT (`.`) has highest precedence
- `2 * math.pi` parses correctly as `2 * (math.pi)`

### Error Messages
- Better error messages for imports
- Clear messages for missing modules/attributes

---

## 📖 Documentation

Lihat file-file ini untuk detail lebih lanjut:
- **README.md** - Complete guide
- **FITUR_BARU.md** - Feature documentation  
- **SECURITY.md** - Security guide (BARU! 🔒)
- **This file (UPDATE.md)** - Quick reference

---

## 🔥 Cool Things You Can Do

1. **Use Safe Python Libraries**
   ```pykasi
   impor math;
   impor json;
   dari datetime impor datetime;
   # Lihat SECURITY.md untuk daftar lengkap
   ```

2. **Build Web APIs**
   ```pykasi
   dari flask impor Flask, jsonify;
   app gas Flask("api");
   ```

3. **Math & Statistics**
   ```pykasi
   impor numpy sebagai np;
   impor matplotlib.pyplot sebagai plt;
   ```

4. **Secure Development**
   ```pykasi
   # PyKasi melindungi dari module berbahaya
   # impor os;  # ERROR: Tidak diizinkan!
   # impor subprocess;  # ERROR: Tidak diizinkan!
   ```

---

## 🔒 Keamanan (BARU!)

### Pembatasan Import Module

PyKasi sekarang membatasi module yang dapat di-import untuk keamanan:

**Module Aman:**
- ✅ math, random, datetime, json
- ✅ string, collections, itertools
- ✅ time, re, urllib.parse
- ✅ base64, hashlib, uuid
- ✅ flask, pathlib
- ✅ Dan lainnya... (lihat SECURITY.md)

**Module Berbahaya (Dilarang):**
- ❌ os - System commands
- ❌ subprocess - Process execution
- ❌ sys - System modification
- ❌ pickle - Code execution
- ❌ importlib - Bypass restrictions

### File Extension Validation

Hanya file `.bks` yang dapat dijalankan untuk keamanan.

Untuk detail lengkap, baca **SECURITY.md**!

---

## ⚠️ Notes

### Flask Debug Mode
`flask_runner.py` uses `debug=True` for development only.
For production, use a WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 flask_runner:app
```

### Backward Compatibility
100% backward compatible! All existing PyKasi code still works.

---

## 🎉 Summary

PyKasi sekarang bisa:
- ✅ Import semua Python libraries
- ✅ Bikin web app dengan Flask
- ✅ Akses dictionary dengan syntax Python
- ✅ Call methods pada Python objects
- ✅ Integrate dengan ekosistem Python

**Gas lah! PyKasi makin powerful! 🚀🔥**

---

*Dibuat dengan Python, Kopi, dan Semangat Bekasi! ☕*
