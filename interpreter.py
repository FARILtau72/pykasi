import importlib
import os
import re

# Security: Dangerous modules that should be restricted
DANGEROUS_MODULES = {
    'os',
    'subprocess',
    'sys',
    '__builtin__',
    '__builtins__',
    'importlib',
    'pickle',
    'shelve',
    'marshal',
    'code',
    'eval',
    'exec',
}

# Modules that are safe to use
SAFE_MODULES = {
    'math',
    'random',
    'datetime',
    'json',
    'string',
    'collections',
    'itertools',
    'functools',
    'time',
    're',
    'urllib.parse',
    'urllib.request',
    'base64',
    'hashlib',
    'hmac',
    'uuid',
    'decimal',
    'fractions',
    'statistics',
    'flask',
    'pathlib',
}

def is_module_name_valid(module_name):
    """Validate module name format"""
    return bool(re.match(r'^[a-zA-Z0-9_.]+$', module_name))

def is_module_safe(module_name):
    """Check if a module is safe to import"""
    base_module = module_name.split('.')[0]
    
    if base_module in DANGEROUS_MODULES:
        return False
    
    if base_module in SAFE_MODULES:
        return True
    
    return False

class ReturnValue(Exception):
    def __init__(self, value):
        self.value = value

class BreakLoop(Exception):
    pass

class ContinueLoop(Exception):
    pass

class RuntimeErrorWithMessage(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Interpreter:
    def __init__(self):
        self.env = {}
        self.types = {}
        self.functions = {}
        self.modules = {}  # Store imported modules
        self._init_builtins()

    def _init_builtins(self):
        """Initialize built-in functions dengan nama Bekasi"""
        self.builtins = {
            'panjang': len,
            'tipe': type,
            'bentuk': str,
            'hitung': int,
            'desimal': float,
            'maks': max,
            'min': min,
            'jumlah': sum,
            'urutkan': sorted,
            'balik': reversed,
            'rentang': range,
        }

    def run(self, program):
        for stmt in program.statements:
            try:
                self.execute(stmt)
            except ReturnValue:
                raise RuntimeErrorWithMessage('Woy, balikin cuma boleh di dalam fungsi!')

    def execute(self, node):
        node_type = type(node)
        if node_type.__name__ == 'Assign':
            value = self.eval_expr(node.expr)
            if getattr(node, 'type_name', None):
                declared = node.type_name
                if declared == 'duit' and not isinstance(value, (int, float)):
                    raise TypeError(f"Variabel '{node.name}' di-declare sebagai duit tapi nilainya bukan angka")
                if declared == 'omongan' and not isinstance(value, str):
                    raise TypeError(f"Variabel '{node.name}' di-declare sebagai omongan tapi nilainya bukan string")
                if declared == 'valid' and not isinstance(value, bool):
                    raise TypeError(f"Variabel '{node.name}' di-declare sebagai valid tapi nilainya bukan boolean")
                self.types[node.name] = declared
            else:
                if node.name in self.types:
                    expected = self.types[node.name]
                    if expected == 'duit' and not isinstance(value, (int, float)):
                        raise TypeError(f"Variabel '{node.name}' kudu duit (angka)")
                    if expected == 'omongan' and not isinstance(value, str):
                        raise TypeError(f"Variabel '{node.name}' kudu omongan (string)")
                    if expected == 'valid' and not isinstance(value, bool):
                        raise TypeError(f"Variabel '{node.name}' kudu valid (boolean)")
            self.env[node.name] = value
            return None
        if node_type.__name__ == 'Print':
            value = self.eval_expr(node.expr)
            print(value)
            return None
        if node_type.__name__ == 'If':
            cond = self.eval_expr(node.cond)
            if cond:
                self.execute_block(node.then_block)
            elif node.else_block:
                self.execute_block(node.else_block)
            return None
        if node_type.__name__ == 'While':
            while self.eval_expr(node.cond):
                try:
                    self.execute_block(node.body)
                except BreakLoop:
                    break
                except ContinueLoop:
                    continue
            return None
        if node_type.__name__ == 'FunctionDef':
            self.functions[node.name] = node
            return None
        if node_type.__name__ == 'Return':
            value = self.eval_expr(node.expr) if node.expr else None
            raise ReturnValue(value)
        if node_type.__name__ == 'Break':
            raise BreakLoop()
        if node_type.__name__ == 'Continue':
            raise ContinueLoop()
        if node_type.__name__ == 'TryCatch':
            try:
                self.execute_block(node.try_block)
            except Exception:
                self.execute_block(node.catch_block)
            return None
        if node_type.__name__ == 'ListAssign':
            lst = self.eval_expr(node.list_expr)
            idx = self.eval_expr(node.index_expr)
            value = self.eval_expr(node.value_expr)
            if not isinstance(lst, list):
                raise TypeError('Yang di-assign harus gudang (list)')
            if not isinstance(idx, int):
                raise TypeError('Index harus duit (angka)')
            if idx < 0 or idx >= len(lst):
                raise IndexError(f'Index {idx} di luar jangkauan')
            lst[idx] = value
            return None
        if node_type.__name__ == 'Import':
            if not is_module_name_valid(node.module_name):
                raise RuntimeErrorWithMessage(f"Woy, nama module '{node.module_name}' ga valid!")
            
            if not is_module_safe(node.module_name):
                raise RuntimeErrorWithMessage(f"Woy, module '{node.module_name}' ga boleh di-import karena alasan keamanan!")
            
            try:
                module = importlib.import_module(node.module_name)
                if node.alias:
                    self.env[node.alias] = module
                else:
                    self.env[node.module_name] = module
            except ImportError as e:
                raise RuntimeErrorWithMessage(f"Woy, module '{node.module_name}' ga ketemu: {e}")
            return None
        if node_type.__name__ == 'ImportFrom':
            if not is_module_name_valid(node.module_name):
                raise RuntimeErrorWithMessage(f"Woy, nama module '{node.module_name}' ga valid!")
            
            if not is_module_safe(node.module_name):
                raise RuntimeErrorWithMessage(f"Woy, module '{node.module_name}' ga boleh di-import karena alasan keamanan!")
            
            try:
                module = importlib.import_module(node.module_name)
                for name, alias in node.import_names:
                    if not hasattr(module, name):
                        raise RuntimeErrorWithMessage(f"Woy, '{name}' ga ada di module '{node.module_name}'")
                    attr = getattr(module, name)
                    self.env[alias if alias else name] = attr
            except ImportError as e:
                raise RuntimeErrorWithMessage(f"Woy, module '{node.module_name}' ga ketemu: {e}")
            return None
        raise RuntimeErrorWithMessage('Node tidak dikenali')

    def execute_block(self, block):
        for stmt in block.statements:
            self.execute(stmt)

    def eval_expr(self, node):
        node_type = type(node)
        if node_type.__name__ == 'Number':
            return node.value
        if node_type.__name__ == 'String':
            return node.value
        if node_type.__name__ == 'Boolean':
            return node.value
        if node_type.__name__ == 'Var':
            if node.name in self.env:
                return self.env[node.name]
            raise NameError(f"Variabel '{node.name}' belum ada")
        if node_type.__name__ == 'AttributeAccess':
            obj = self.eval_expr(node.obj)
            if not hasattr(obj, node.attr):
                raise AttributeError(f"Woy, objek ga punya atribut '{node.attr}'")
            return getattr(obj, node.attr)
        if node_type.__name__ == 'List':
            return [self.eval_expr(elem) for elem in node.elements]
        if node_type.__name__ == 'ListAccess':
            container = self.eval_expr(node.list_expr)
            key = self.eval_expr(node.index_expr)
            
            # Handle dictionary access
            if isinstance(container, dict):
                if key not in container:
                    raise KeyError(f"Key '{key}' ga ada di dictionary")
                return container[key]
            
            # Handle list/string access
            if not isinstance(container, (list, str)):
                raise TypeError('Yang di-akses harus gudang (list), catetan (dict), atau omongan (string)')
            if not isinstance(key, int):
                raise TypeError('Index harus duit (angka)')
            if key < 0 or key >= len(container):
                raise IndexError(f'Index {key} di luar jangkauan')
            return container[key]
        if node_type.__name__ == 'Dict':
            result = {}
            for key_node, val_node in node.pairs:
                key = self.eval_expr(key_node)
                val = self.eval_expr(val_node)
                result[key] = val
            return result
        if node_type.__name__ == 'Lambda':
            return ('lambda', node.params, node.expr, dict(self.env))
        if node_type.__name__ == 'MethodCall':
            obj = self.eval_expr(node.obj)
            if not hasattr(obj, node.method_name):
                raise AttributeError(f"Woy, objek ga punya method '{node.method_name}'")
            method = getattr(obj, node.method_name)
            args = [self.eval_expr(arg) for arg in node.args]
            return method(*args)
        if node_type.__name__ == 'FunctionCall':
            func_name = node.name
            
            # Check built-in functions first
            if func_name in self.builtins:
                args = [self.eval_expr(arg) for arg in node.args]
                return self.builtins[func_name](*args)
            
            # Check if it's a callable in environment (imported function)
            if func_name in self.env:
                func_obj = self.env[func_name]
                if callable(func_obj):
                    args = [self.eval_expr(arg) for arg in node.args]
                    return func_obj(*args)
            
            # Check user-defined functions
            if func_name not in self.functions:
                raise NameError(f"Fungsi '{func_name}' belum ada")
            
            func = self.functions[func_name]
            args = [self.eval_expr(arg) for arg in node.args]
            
            if len(args) != len(func.params):
                raise TypeError(f"Fungsi '{func_name}' butuh {len(func.params)} parameter, lu kasih {len(args)}")
            
            # Save current environment
            old_env = dict(self.env)
            
            # Create new environment with parameters
            for param, arg in zip(func.params, args):
                self.env[param] = arg
            
            # Execute function body
            try:
                self.execute_block(func.body)
                result = None
            except ReturnValue as ret:
                result = ret.value
            finally:
                # Restore environment
                self.env = old_env
            
            return result
        if node_type.__name__ == 'BinaryOp':
            left = self.eval_expr(node.left)
            right = self.eval_expr(node.right)
            op = node.op
            if op == '+':
                if isinstance(left, str) and isinstance(right, str):
                    return left + right
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left + right
                if isinstance(left, list) and isinstance(right, list):
                    return left + right
                raise TypeError('Operator + butuh dua angka, dua string, atau dua list')
            if op == '-':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left - right
                raise TypeError('Operator - butuh dua angka')
            if op == '*':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left * right
                if isinstance(left, str) and isinstance(right, int):
                    return left * right
                if isinstance(left, list) and isinstance(right, int):
                    return left * right
                raise TypeError('Operator * butuh dua angka atau string/list * angka')
            if op == '/':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left / right
                raise TypeError('Operator / butuh dua angka')
            if op == '%':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    if right == 0:
                        raise ZeroDivisionError('Modulo dengan nol? Ngadi-ngadi lu!')
                    return left % right
                raise TypeError('Operator % butuh dua angka')
            if op == '**':
                if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left ** right
                raise TypeError('Operator ** butuh dua angka')
            if op == '==':
                return left == right
            if op == '!=':
                return left != right
            if op == '>':
                return left > right
            if op == '<':
                return left < right
            if op == '>=':
                return left >= right
            if op == '<=':
                return left <= right
        raise RuntimeErrorWithMessage('Ekspresi tidak dikenali')
