import ply.lex as lex
import ply.yacc as yacc
import re 


tokens = (
    'ROBOT_R',
    'VARS',
    'ID',
    'COMMA',
    'SEMICOLON',
    'PROCS',
    'LBRACKET',
    'RBRACKET',
    'PLECA',
    'assignTo',
    'DOSPUNTOS',
    'INTEGER',
    'put',
    'ITEMS',
    'pick',
    'DIRECTION',
    'LEFTANDRIGHT',
    'DIRECTION_TURN',
    'movetothe',
    'jumptothe',
    'moveindir',
    'jumpindir',
    'CARDINAL',
    'move',
    'goto',
    'turn',
    'face',
    'nop'
)

global_variables = {}




def t_ROBOT_R(t):
    r'(?i)ROBOT_R'
    return t

def t_VARS(t):
    r'(?i)VARS'
    return t

def t_PROCS(t):
    r'(?i)PROCS'
    return t


def t_assignTo(t):
    r'(?i)assignTo\b'
    return t

def t_ITEMS(t):
    r'(?i)chips\b|balloons\b'
    return t

def t_put(t):
    r'(?i)put\b'
    return t

def t_pick(t):
    r'(?i)pick\b'
    return t

def t_movetothe(t):
    r'(?i)movetothe\b'
    return t

def t_jumptothe(t):
    r'(?i)jumptothe\b'
    return t

def t_DIRECTION(t):
    r'(?i)front\b|back\b'
    return t

def t_moveindir(t):
    r'(?i)moveindir\b'
    return t

def t_jumpindir(t):
    r'(?i)jumpindir\b'
    return t

def t_CARDINAL(t):
    r'(?i)north\b|south\b|west\b|east\b'
    return t

def t_move(t):
    r'(?i)move\b'
    return t

def t_goto(t):
    r'(?i)goto\b'
    return t

def t_turn(t):
    r'(?i)turn\b'
    return t

def t_DIRECTION_TURN(t):
    r'(?i)around\b'
    return t

def t_LEFTANDRIGHT(t):
    r'(?i)left\b|right\b'
    return t

def t_face(t):
    r'(?i)face\b'
    return t

def t_nop(t):
    r'(?i)nop\b'
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    if t.value not in tokens:
        t.value = t.value.lower()
        return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMA(t):
    r','
    return t

def t_SEMICOLON(t):
    r';'
    return t

def t_LBRACKET(t):
    r'\['
    return t

def t_RBRACKET(t):
    r'\]'
    return t

def t_PLECA(t):
    r'\|'
    return t

def t_DOSPUNTOS(t):
    r':'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

t_ignore = ' \t'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()


def p_prog(p):
    '''prog : ROBOT_R var_def PROCS
            | ROBOT_R var_def PROCS id_def'''
    p[0] = p[2]

def p_var_def(p):
    'var_def : VARS ID_list SEMICOLON'
    for id in p[2]:
        global_variables[id] = None
    p[0] = p[2]

def p_ID_list(p):
    '''ID_list : ID
              | ID_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_id_def(p):
    '''id_def : ID LBRACKET PLECA ID COMMA ID PLECA RBRACKET 
              | ID LBRACKET PLECA ID COMMA ID PLECA function_def RBRACKET 
              | ID LBRACKET PLECA ID COMMA ID PLECA function_def function_def RBRACKET 
              | ID LBRACKET PLECA ID COMMA ID PLECA function_def function_def function_def RBRACKET
              | ID LBRACKET PLECA ID COMMA ID PLECA function_def function_def function_def function_def RBRACKET
              | ID LBRACKET PLECA ID COMMA ID PLECA function_def function_def function_def function_def function_def RBRACKET'''
    if len(p) == 8:
        p[0] = (p[3], p[5])
    else:
        p[0] = (p[3], p[5], p[9])

def p_functions_def(p):
    """function_def : assignTo_def
                    | put_def
                    | moveandjumptothe_def
                    | moveandjumpindir_def
                    | move_def
                    | goto_def
                    | turn_def
                    | face_def
                    | nop_def"""

def p_assignTo_def(p):
    'assignTo_def : assignTo DOSPUNTOS INTEGER COMMA ID SEMICOLON'
    if p[5] in global_variables:
        global_variables[p[5]] = p[3]
        p[0] = (p[3], p[5])
    else:
        p_error(p)  

def p_put_def(p):
    """put_def : put DOSPUNTOS ID COMMA ITEMS SEMICOLON
               | put DOSPUNTOS INTEGER COMMA ITEMS SEMICOLON
               | pick DOSPUNTOS INTEGER COMMA ITEMS SEMICOLON
               | pick DOSPUNTOS ID COMMA ITEMS SEMICOLON"""

def p_moveandjumptothe_def(p):
    """moveandjumptothe_def : movetothe DOSPUNTOS ID COMMA DIRECTION SEMICOLON
               | movetothe DOSPUNTOS INTEGER COMMA DIRECTION SEMICOLON
               | jumptothe DOSPUNTOS INTEGER COMMA DIRECTION SEMICOLON
               | jumptothe DOSPUNTOS ID COMMA DIRECTION SEMICOLON
               | movetothe DOSPUNTOS ID COMMA LEFTANDRIGHT SEMICOLON
               | movetothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT SEMICOLON
               | jumptothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT SEMICOLON
               | jumptothe DOSPUNTOS ID COMMA LEFTANDRIGHT SEMICOLON"""    

def p_moveandjumpindir_def(p):
    """moveandjumpindir_def : moveindir DOSPUNTOS ID COMMA CARDINAL SEMICOLON
               | moveindir DOSPUNTOS INTEGER COMMA CARDINAL SEMICOLON
               | jumpindir DOSPUNTOS INTEGER COMMA CARDINAL SEMICOLON
               | jumpindir DOSPUNTOS ID COMMA CARDINAL SEMICOLON"""
    
def p_move_def(p):
    """move_def : move DOSPUNTOS ID SEMICOLON
                | move DOSPUNTOS INTEGER SEMICOLON"""

def p_goto_def(p):
    """goto_def : goto DOSPUNTOS ID COMMA ID SEMICOLON
                | goto DOSPUNTOS INTEGER COMMA INTEGER SEMICOLON
                | goto DOSPUNTOS ID COMMA INTEGER SEMICOLON
                | goto DOSPUNTOS INTEGER COMMA ID SEMICOLON"""

def p_turn_def(p):
    """turn_def : turn DOSPUNTOS DIRECTION_TURN SEMICOLON
                | turn DOSPUNTOS LEFTANDRIGHT SEMICOLON"""
    
def p_face_def(p):
    """face_def : face DOSPUNTOS CARDINAL SEMICOLON"""

def p_nop_def(p):
    """nop_def : nop DOSPUNTOS """
    

success = True

def p_error(p):
    global success
    success = False

parser = yacc.yacc()

data = "ROBOT_R\nVARS nAm, y, z,arroz;\nPROCS\nassigntoCB[|c,b| move: 1; face: west; jumptothe: 20, left;]"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)


result = parser.parse(data)
print(result)
print(global_variables)

if success:
    print("True")
else:
    print("False")
