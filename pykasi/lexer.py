import re
import ply.lex as lex

class Lexer:
    tokens = [
        'NAME', 'NUMBER', 'STRING',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO', 'POWER',
        'EQEQ', 'GT', 'LT', 'GTE', 'LTE', 'NEQ',
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
        'SEMI', 'COMMA', 'COLON', 'ARROW', 'DOT'
    ]

    literals = []

    reserved = {
        'spill': 'SPILL',
        'gas': 'GAS',
        'kalo': 'KALO',
        'kalo_kaga': 'KALO_KAGA',
        'valid': 'VALID',
        'hoax': 'HOAX',
        'puterin': 'PUTERIN',
        'duit': 'DUIT',
        'omongan': 'OMONGAN',
        'fungsi': 'FUNGSI',
        'balikin': 'BALIKIN',
        'gudang': 'GUDANG',
        'catetan': 'CATETAN',
        'coba': 'COBA',
        'tangkep': 'TANGKEP',
        'lamda': 'LAMDA',
        'dalam': 'DALAM',
        'terus': 'TERUS',
        'berhenti': 'BERHENTI',
        'impor': 'IMPOR',
        'dari': 'DARI',
        'sebagai': 'SEBAGAI'
    }

    tokens = tokens + list(reserved.values())

    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_POWER = r'\*\*'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MODULO = r'%'
    t_NEQ = r'!='
    t_EQEQ = r'=='
    t_GTE = r'>='
    t_LTE = r'<='
    t_GT = r'>'
    t_LT = r'<'
    t_ARROW = r'=>'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_SEMI = r';'
    t_COMMA = r','
    t_COLON = r':'
    t_DOT = r'\.'

    t_ignore = ' \t'

    def t_comment(self, t):
        r'\#.*'
        pass

    def t_NAME(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value in self.reserved:
            t.type = self.reserved[t.value]
        return t

    def t_NUMBER(self, t):
        r'\d+\.\d+|\d+'
        if '.' in t.value:
            t.value = float(t.value)
        else:
            t.value = int(t.value)
        return t

    def t_STRING(self, t):
        r'"([^\\\n"]|\\.)*"'
        t.value = t.value[1:-1]
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        raise SyntaxError(f'Tidak ngerti token: {t.value[0]}')

    def build(self, **kwargs):
        self.lexobj = lex.lex(module=self, **kwargs)
        return self.lexobj
