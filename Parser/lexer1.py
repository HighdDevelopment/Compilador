import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'do' : "DO",
    'repeat' : "REPEAT",
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
    "ITEMS",
    "ROBOT_R",
    'NEWLINE'

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

def t_ROBOT_R(t):
    r'ROBOT_R'
    return t


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
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    return 

# Función de error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

counter = 0

def p_check_first_line(p):
    'check_first_line : ROBOT_R'
    global counter
    counter += 1
    if counter == 1:
        print("The first line is correct")
    else:
        print("Error: 'ROBOT_R' can only appear once in the file")

def p_check_first_line_error(p):
    'check_first_line : TEXT'
    global counter
    if counter == 0:
        print("Error: The first line must be 'ROBOT_R'")

def p_error(p):
    print("Syntax error in input!")

if counter != 1:
    print("Error: 'ROBOT_R' must appear once in the file")
else:
    print("'ROBOT_R' appears only once in the file")
parser = yacc.yacc()

with open('test.txt', 'r') as file:
    first_line = file.readline()
    result = parser.parse(first_line)