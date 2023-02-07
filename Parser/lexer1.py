import ply.lex as lex

# Lista de tokens
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : "DO",
    'repeat' : "REPEAT",
    'ROBOT_R': "ROBOT_R",
    "facing": "FACING",
    "canPut": "CANPUT",
    "canPick": "CANPICK",
    "canMoveInDir":"CANMOVEINDIR",
    "canJumpInDir":"CANJUMPINDIR",
    "canMovetoThe":"CANMOVETOTHE",
    "canJumptoThe":"CANJUMPTOTHE",
    "not":"NOT",
    "assignTo":"ASSIGNTO",
    "goTo":"GOTO",
    "move":"MOVE",
    "turn":"TURN", 
    "face":"FACE",
    "put":"PUT",
    "pick":"PICK",
    "moveToThe":"MOVETOTHE",
    "moveInDir":"MOVEINDIR",
    "jumpToThe":"JUMPTOTHE",
    "jumpInDir":"JUMPINDIR",
    "nop":"NOP",
    "VARS":"VARS",
    "PROCS":"PROCS",
 }

tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',
    "CORDER",    
    "CORIZQ",
    "PLECA",
    "COMA",
    "DOSPUNTOS",
    "PUNTOCOMA",
    "DIRECTION",
    "ORIENTATION",
    "ITEMS"

] + list(reserved.values())

# Reglas de expresiones regulares para los tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_CORDER = r"\["
t_CORIZQ = r"\]"
t_PLECA = r"\|"
t_COMA = r","
t_DOSPUNTOS = r":"
t_PUNTOCOMA = r";"

# Un token NUMBER representa un número decimal
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DIRECTION(t):
    r'(north|south|east|west)'
    return t

def t_ORIENTATION(t):
    r'(front|right|left|back)'
    return t

def t_ITEMS(t):
    r'(chips|balloons)'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t



# Reglas de ignorar
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Función de error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()



