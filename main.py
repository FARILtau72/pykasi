#!/usr/bin/env python3
"""
PyKasi - Main entry point
"""

import sys
import os
from pykasi import run_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.bks>")
        print("Example: python main.py contoh.bks")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not file_path.endswith('.bks'):
        print("Error: File harus berekstensi .bks")
        sys.exit(1)
    
    try:
        abs_path = os.path.abspath(file_path)
        if not os.path.isfile(abs_path):
            print(f"Error: File '{file_path}' tidak ditemukan")
            sys.exit(1)
        
        run_file(abs_path)
    except OSError:
        print(f"Error: Tidak dapat mengakses file '{file_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
