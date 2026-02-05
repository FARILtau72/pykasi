#!/usr/bin/env python3
"""
Flask Web App Runner for PyKasi
Demonstrates how to use Flask with PyKasi
"""

from flask import Flask, jsonify

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><title>PyKasi Web App</title></head>
    <body style="font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px;">
        <h1>🪐 Halo dari PyKasi!</h1>
        <p>Ini web server yang dibuat pake bahasa Bekasi! Gas lah! 🚀</p>
        <h2>Fitur PyKasi:</h2>
        <ul>
            <li>Fungsi (fungsi)</li>
            <li>Lists dan dictionaries</li>
            <li>Built-in functions Bekasi</li>
            <li>Try-catch error handling</li>
            <li>Python library imports</li>
            <li><strong>Flask web framework!</strong></li>
        </ul>
        <h3>Routes:</h3>
        <ul>
            <li><a href="/">/ - Homepage (you are here)</a></li>
            <li><a href="/about">/about - About PyKasi</a></li>
            <li><a href="/api/data">/api/data - JSON API</a></li>
            <li><a href="/api/hitung/5/3">/api/hitung/5/3 - Calculator API</a></li>
        </ul>
    </body>
    </html>
    """

@app.route('/about')
def about():
    return """
    <html>
    <head><title>About PyKasi</title></head>
    <body style="font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px;">
        <h1>About PyKasi</h1>
        <p><strong>PyKasi</strong> adalah bahasa pemrograman esoterik dengan syntax bahasa Bekasi!</p>
        <h2>Kenapa PyKasi?</h2>
        <ul>
            <li>Coding rasa nongkrong di Kalimalang</li>
            <li>Syntax yang fun tapi powerful</li>
            <li>Akses ke Python libraries</li>
            <li>Bisa bikin web app pake Flask!</li>
        </ul>
        <p><a href="/">← Back to Home</a></p>
    </body>
    </html>
    """

@app.route('/api/data')
def api_data():
    return jsonify({
        'nama': 'PyKasi',
        'versi': '1.0',
        'lokasi': 'Bekasi',
        'fitur': [
            'Functions',
            'Lists & Dictionaries',
            'Python Imports',
            'Flask Web Framework'
        ],
        'status': 'Gas terus! 🚀'
    })

@app.route('/api/hitung/<int:a>/<int:b>')
def api_hitung(a, b):
    """API untuk kalkulasi sederhana"""
    return jsonify({
        'a': a,
        'b': b,
        'tambah': a + b,
        'kurang': a - b,
        'kali': a * b,
        'bagi': a / b if b != 0 else 'Error: Pembagian dengan nol!',
        'message': 'Hitung pake PyKasi!'
    })

if __name__ == '__main__':
    print("=" * 50)
    print("🪐 PyKasi Flask Web Server")
    print("=" * 50)
    print("\nServer running on:")
    print("  • http://127.0.0.1:5000")
    print("  • http://localhost:5000")
    print("\nPress Ctrl+C to stop the server\n")
    
    # WARNING: debug=True is for development only!
    # For production, use a WSGI server like gunicorn or waitress
    # Example: gunicorn -w 4 -b 127.0.0.1:5000 flask_runner:app
    app.run(debug=True, host='127.0.0.1', port=5000)
