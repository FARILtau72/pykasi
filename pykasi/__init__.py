"""PyKasi package initializer

Expose package-level helpers for running PyKasi code programmatically.
"""

__version__ = '0.1.0'

from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter, RuntimeErrorWithMessage, ReturnValue, BreakLoop, ContinueLoop
from pathlib import Path

def _ngegas_message_for(exception):
    if isinstance(exception, ZeroDivisionError):
        return 'Woy, error nih! Lu bagi nol ya? Ngadi-ngadi lu!'
    if isinstance(exception, NameError):
        return f'Woy, variabel ga ada: {exception}'
    if isinstance(exception, TypeError):
        return f'Woy, tipe data salah: {exception}'
    if isinstance(exception, SyntaxError):
        return f'Woy, salah sintaks: {exception}'
    return f'Woy, error aneh: {exception}'

def run_text(text):
    try:
        parser = Parser()
        ast = parser.parse(text)
        interp = Interpreter()
        interp.run(ast)
    except Exception as e:
        message = _ngegas_message_for(e)
        raise RuntimeErrorWithMessage(message)

def run_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return run_text(f.read())

def logo_path():
    root = Path(__file__).resolve().parent
    p = root.parent / 'assets' / 'logo.svg'
    if p.exists():
        return str(p)
    raise FileNotFoundError('assets/logo.svg tidak ditemukan')

def logo_svg():
    p = Path(logo_path())
    return p.read_text(encoding='utf-8')

__all__ = ['Lexer', 'Parser', 'Interpreter', 'run_text', 'run_file', 'logo_path', 'logo_svg', 'RuntimeErrorWithMessage']
