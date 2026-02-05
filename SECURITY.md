# 🔒 PyKasi Security Guide

## Keamanan PyKasi

PyKasi dirancang dengan keamanan yang dipertimbangkan untuk melindungi pengguna dari kode berbahaya.

## Fitur Keamanan

### 1. Pembatasan Import Module

PyKasi membatasi module Python yang dapat di-import untuk mencegah eksekusi kode berbahaya.

**Module yang DIIZINKAN:**
- `math` - Operasi matematika
- `random` - Angka acak
- `datetime` - Tanggal dan waktu
- `json` - Parsing JSON
- `string` - Manipulasi string
- `collections` - Tipe data koleksi
- `itertools`, `functools` - Functional programming
- `time` - Waktu
- `re` - Regular expressions
- `urllib.parse`, `urllib.request` - URL parsing
- `base64`, `hashlib`, `hmac` - Encoding & hashing
- `uuid` - UUID generation
- `decimal`, `fractions`, `statistics` - Matematika lanjutan
- `flask` - Web framework
- `pathlib` - Path operations

**Module yang DILARANG:**
- `os` - Dapat menjalankan system commands
- `subprocess` - Dapat menjalankan system commands
- `sys` - Dapat memodifikasi sistem
- `__builtin__`, `__builtins__` - Akses internal Python
- `importlib` - Dapat bypass import restrictions
- `pickle`, `shelve`, `marshal` - Dapat execute arbitrary code
- `code` - Dapat compile dan execute code

### 2. Validasi Input

**File Path:**
- Hanya file dengan ekstensi `.bks` yang dapat dijalankan
- Path divalidasi dan di-resolve ke absolute path
- Dicek keberadaan file sebelum execution

**Module Names:**
- Nama module harus alphanumeric (dengan underscore dan dot)
- Dicek terhadap whitelist module yang aman

### 3. Flask Debug Mode

**Warning:** `flask_runner.py` menggunakan `debug=True` hanya untuk development!

Untuk production, gunakan WSGI server:
```bash
pip install gunicorn
gunicorn -w 4 flask_runner:app
```

## Best Practices

### Untuk Developer

1. **Jangan Import Module Berbahaya**
   ```pykasi
   # JANGAN LAKUKAN INI:
   # impor os;  # ERROR: Tidak diizinkan!
   # impor subprocess;  # ERROR: Tidak diizinkan!
   
   # LAKUKAN INI:
   impor math;  # OK
   impor json;  # OK
   ```

2. **Validasi User Input**
   Jika aplikasi Anda menerima input user, validasi dengan hati-hati:
   ```pykasi
   fungsi process_input(input_str) {
       # Validasi input
       kalo panjang(input_str) > 1000 {
           balikin "Input terlalu panjang";
       }
       # Process safely
       balikin input_str;
   }
   ```

3. **Hindari Dynamic Code Execution**
   PyKasi tidak mendukung `eval()` atau `exec()` untuk keamanan.

### Untuk Production

1. **Gunakan WSGI Server** - Jangan gunakan Flask development server
2. **Set Environment Variables** - Jangan hardcode credentials
3. **Enable HTTPS** - Gunakan SSL/TLS untuk komunikasi
4. **Rate Limiting** - Batasi request per user
5. **Input Validation** - Selalu validasi input dari user

## Melaporkan Security Issues

Jika Anda menemukan security vulnerability:
1. **JANGAN** buat public issue
2. Email ke maintainer secara private
3. Berikan detail yang jelas tentang vulnerability
4. Tunggu response sebelum disclosure

## Changelog Keamanan

### Version 1.0
- ✅ Implementasi module import whitelist
- ✅ Validasi file path
- ✅ Validasi module names
- ✅ Warning untuk Flask debug mode
- ✅ Dokumentasi keamanan

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Flask Security](https://flask.palletsprojects.com/en/2.0.x/security/)

---

**Ingat: Keamanan adalah tanggung jawab bersama! 🔒**
