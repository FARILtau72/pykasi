import ply.yacc as yacc
from .lexer import Lexer

class Node:
    pass

class Program(Node):
    def __init__(self, statements):
        self.statements = statements

class StatementList(Node):
    def __init__(self, statements):
        self.statements = statements

class Assign(Node):
    def __init__(self, name, expr, type_name=None):
        self.name = name
        self.expr = expr
        self.type_name = type_name

class Print(Node):
    def __init__(self, expr):
        self.expr = expr

class If(Node):
    def __init__(self, cond, then_block, else_block=None):
        self.cond = cond
        self.then_block = then_block
        self.else_block = else_block

class While(Node):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class Block(Node):
    def __init__(self, statements):
        self.statements = statements

class BinaryOp(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Number(Node):
    def __init__(self, value):
        self.value = value

class String(Node):
    def __init__(self, value):
        self.value = value

class Boolean(Node):
    def __init__(self, value):
        self.value = value

class Var(Node):
    def __init__(self, name):
        self.name = name

class FunctionDef(Node):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class Return(Node):
    def __init__(self, expr):
        self.expr = expr

class FunctionCall(Node):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class MethodCall(Node):
    def __init__(self, obj, method_name, args):
        self.obj = obj
        self.method_name = method_name
        self.args = args

class List(Node):
    def __init__(self, elements):
        self.elements = elements

class ListAccess(Node):
    def __init__(self, list_expr, index_expr):
        self.list_expr = list_expr
        self.index_expr = index_expr

class Dict(Node):
    def __init__(self, pairs):
        self.pairs = pairs

class Lambda(Node):
    def __init__(self, params, expr):
        self.params = params
        self.expr = expr

class TryCatch(Node):
    def __init__(self, try_block, catch_block):
        self.try_block = try_block
        self.catch_block = catch_block

class Continue(Node):
    pass

class Break(Node):
    pass

class ListAssign(Node):
    def __init__(self, list_expr, index_expr, value_expr):
        self.list_expr = list_expr
        self.index_expr = index_expr
        self.value_expr = value_expr

class Import(Node):
    def __init__(self, module_name, alias=None):
        self.module_name = module_name
        self.alias = alias

class ImportFrom(Node):
    def __init__(self, module_name, import_names):
        self.module_name = module_name
        self.import_names = import_names  # List of (name, alias) tuples

class AttributeAccess(Node):
    def __init__(self, obj, attr):
        self.obj = obj
        self.attr = attr

class Parser:
    def __init__(self):
        self.lexer = Lexer()
        self.lexer.build()
        self.tokens = self.lexer.tokens
        self.yacc = yacc.yacc(module=self, debug=False, write_tables=False)

    def parse(self, text):
        return self.yacc.parse(text, lexer=self.lexer.lexobj)

    precedence = (
        ('left', 'EQEQ', 'NEQ', 'GT', 'LT', 'GTE', 'LTE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE', 'MODULO'),
        ('right', 'POWER'),
        ('left', 'LBRACKET', 'DOT'),
    )

    def p_program(self, p):
        'program : statements'
        p[0] = Program(p[1])

    def p_statements_multiple(self, p):
        'statements : statements statement'
        p[0] = p[1]
        p[0].append(p[2])

    def p_statements_single(self, p):
        'statements : statement'
        p[0] = [p[1]]

    def p_statement_assign(self, p):
        'statement : NAME GAS expression SEMI'
        p[0] = Assign(p[1], p[3])

    def p_statement_list_assign(self, p):
        'statement : NAME LBRACKET expression RBRACKET GAS expression SEMI'
        p[0] = ListAssign(Var(p[1]), p[3], p[6])

    def p_statement_typed_duit(self, p):
        'statement : DUIT NAME GAS expression SEMI'
        p[0] = Assign(p[2], p[4], type_name='duit')

    def p_statement_typed_omongan(self, p):
        'statement : OMONGAN NAME GAS expression SEMI'
        p[0] = Assign(p[2], p[4], type_name='omongan')

    def p_statement_typed_validdecl(self, p):
        'statement : VALID NAME GAS expression SEMI'
        p[0] = Assign(p[2], p[4], type_name='valid')

    def p_statement_print(self, p):
        'statement : SPILL expression SEMI'
        p[0] = Print(p[2])

    def p_statement_if(self, p):
        'statement : KALO expression block optional_else'
        p[0] = If(p[2], p[3], p[4])

    def p_optional_else(self, p):
        'optional_else : KALO_KAGA block'
        p[0] = p[2]

    def p_optional_else_empty(self, p):
        'optional_else : '
        p[0] = None

    def p_statement_while(self, p):
        'statement : PUTERIN expression block'
        p[0] = While(p[2], p[3])

    def p_statement_function_def(self, p):
        'statement : FUNGSI NAME LPAREN param_list RPAREN block'
        p[0] = FunctionDef(p[2], p[4], p[6])

    def p_param_list_multiple(self, p):
        'param_list : param_list COMMA NAME'
        p[0] = p[1] + [p[3]]

    def p_param_list_single(self, p):
        'param_list : NAME'
        p[0] = [p[1]]

    def p_param_list_empty(self, p):
        'param_list : '
        p[0] = []

    def p_statement_return(self, p):
        'statement : BALIKIN expression SEMI'
        p[0] = Return(p[2])

    def p_statement_return_empty(self, p):
        'statement : BALIKIN SEMI'
        p[0] = Return(None)

    def p_statement_continue(self, p):
        'statement : TERUS SEMI'
        p[0] = Continue()

    def p_statement_break(self, p):
        'statement : BERHENTI SEMI'
        p[0] = Break()

    def p_statement_try_catch(self, p):
        'statement : COBA block TANGKEP block'
        p[0] = TryCatch(p[2], p[4])

    def p_statement_import(self, p):
        'statement : IMPOR NAME SEMI'
        p[0] = Import(p[2])

    def p_statement_import_as(self, p):
        'statement : IMPOR NAME SEBAGAI NAME SEMI'
        p[0] = Import(p[2], p[4])

    def p_statement_import_from(self, p):
        'statement : DARI NAME IMPOR import_names SEMI'
        p[0] = ImportFrom(p[2], p[4])

    def p_import_names_multiple(self, p):
        'import_names : import_names COMMA NAME'
        p[0] = p[1] + [(p[3], None)]

    def p_import_names_single(self, p):
        'import_names : NAME'
        p[0] = [(p[1], None)]

    def p_import_names_as(self, p):
        'import_names : NAME SEBAGAI NAME'
        p[0] = [(p[1], p[3])]

    def p_block(self, p):
        'block : LBRACE statements RBRACE'
        p[0] = Block(p[2])

    def p_expression_binop(self, p):
        '''expression : expression PLUS expression
                      | expression MINUS expression
                      | expression TIMES expression
                      | expression DIVIDE expression
                      | expression MODULO expression
                      | expression POWER expression
                      | expression EQEQ expression
                      | expression NEQ expression
                      | expression GT expression
                      | expression LT expression
                      | expression GTE expression
                      | expression LTE expression'''
        p[0] = BinaryOp(p[2], p[1], p[3])

    def p_expression_group(self, p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_number(self, p):
        'expression : NUMBER'
        p[0] = Number(p[1])

    def p_expression_string(self, p):
        'expression : STRING'
        p[0] = String(p[1])

    def p_expression_duit(self, p):
        'expression : DUIT NUMBER'
        p[0] = Number(p[2])

    def p_expression_omongan(self, p):
        'expression : OMONGAN STRING'
        p[0] = String(p[2])

    def p_expression_boolean_valid(self, p):
        'expression : VALID'
        p[0] = Boolean(True)

    def p_expression_boolean_hoax(self, p):
        'expression : HOAX'
        p[0] = Boolean(False)

    def p_expression_name(self, p):
        'expression : NAME'
        p[0] = Var(p[1])

    def p_expression_attribute(self, p):
        'expression : expression DOT NAME'
        p[0] = AttributeAccess(p[1], p[3])

    def p_expression_function_call(self, p):
        'expression : NAME LPAREN arg_list RPAREN'
        p[0] = FunctionCall(p[1], p[3])

    def p_expression_method_call(self, p):
        'expression : expression DOT NAME LPAREN arg_list RPAREN'
        p[0] = MethodCall(p[1], p[3], p[5])

    def p_arg_list_multiple(self, p):
        'arg_list : arg_list COMMA expression'
        p[0] = p[1] + [p[3]]

    def p_arg_list_single(self, p):
        'arg_list : expression'
        p[0] = [p[1]]

    def p_arg_list_empty(self, p):
        'arg_list : '
        p[0] = []

    def p_expression_list(self, p):
        'expression : LBRACKET arg_list RBRACKET'
        p[0] = List(p[2])

    def p_expression_list_access(self, p):
        'expression : expression LBRACKET expression RBRACKET'
        p[0] = ListAccess(p[1], p[3])

    def p_expression_dict(self, p):
        'expression : LBRACE dict_pairs RBRACE'
        p[0] = Dict(p[2])

    def p_dict_pairs_multiple(self, p):
        'dict_pairs : dict_pairs COMMA expression COLON expression'
        p[0] = p[1] + [(p[3], p[5])]

    def p_dict_pairs_single(self, p):
        'dict_pairs : expression COLON expression'
        p[0] = [(p[1], p[3])]

    def p_dict_pairs_empty(self, p):
        'dict_pairs : '
        p[0] = []

    def p_expression_lambda(self, p):
        'expression : LAMDA LPAREN param_list RPAREN ARROW expression'
        p[0] = Lambda(p[3], p[6])

    def p_error(self, p):
        if p:
            raise SyntaxError(f'Sintaks salah dekat token {p.value}')
        raise SyntaxError('Sintaks salah di akhir input')
