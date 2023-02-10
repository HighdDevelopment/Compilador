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
    'nop',
    'if',
    'then',
    'else',
    'while',
    'do'
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

def t_if(t):
    r'(?i)if\b'
    return t

def t_then(t):
    r'(?i)then\b'
    return t

def t_else(t):
    r'(?i)else\b'
    return t

def t_while(t):
    r'(?i)while\b'
    return t

def t_do(t):
    r'(?i)do\b'
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
            | ROBOT_R var_def PROCS bloque_def'''
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

def p_bloque_def(p):
    """bloque_def : id_def
                  | bloque_def id_def"""

def p_id_def(p):
    '''id_def : ID LBRACKET PLECA id_func PLECA func_def RBRACKET'''
    if len(p) == 8:
        p[0] = (p[3], p[5])
    else:
        p[0] = (p[3], p[5], p[9])

def p_id_func(p):
    '''id_func : ID
               | ID COMMA id_func
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = [p[1]] + p[3]

def p_func_def(p):
    """
    func_def : function_def
             | func_def SEMICOLON function_def
             | if_else_def
             | while_def
    """

def p_if_else_def(t):
    '''if_else_def : if DOSPUNTOS function_def then DOSPUNTOS LBRACKET function_def RBRACKET else DOSPUNTOS LBRACKET function_def RBRACKET
                   | if DOSPUNTOS function_def then DOSPUNTOS LBRACKET if_else_def RBRACKET else DOSPUNTOS LBRACKET function_def RBRACKET
                   | if DOSPUNTOS function_def then DOSPUNTOS LBRACKET function_def RBRACKET else DOSPUNTOS LBRACKET if_else_def RBRACKET
                   | if DOSPUNTOS function_def then DOSPUNTOS LBRACKET if_else_def RBRACKET else DOSPUNTOS LBRACKET if_else_def RBRACKET'''

def p_while_def(t):
    '''while_def : while DOSPUNTOS function_def do DOSPUNTOS LBRACKET function_def RBRACKET
                 | while DOSPUNTOS function_def do DOSPUNTOS LBRACKET if_else_def RBRACKET
                 | while DOSPUNTOS function_def do DOSPUNTOS LBRACKET while_def RBRACKET'''

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
    'assignTo_def : assignTo DOSPUNTOS INTEGER COMMA ID'
    if p[5] in global_variables:
        global_variables[p[5]] = p[3]
        p[0] = (p[3], p[5])
    else:
        p_error(p)  

def p_put_def(p):
    """put_def : put DOSPUNTOS ID COMMA ITEMS 
               | put DOSPUNTOS INTEGER COMMA ITEMS 
               | pick DOSPUNTOS INTEGER COMMA ITEMS 
               | pick DOSPUNTOS ID COMMA ITEMS """

def p_moveandjumptothe_def(p):
    """moveandjumptothe_def : movetothe DOSPUNTOS ID COMMA DIRECTION 
               | movetothe DOSPUNTOS INTEGER COMMA DIRECTION 
               | jumptothe DOSPUNTOS INTEGER COMMA DIRECTION 
               | jumptothe DOSPUNTOS ID COMMA DIRECTION 
               | movetothe DOSPUNTOS ID COMMA LEFTANDRIGHT 
               | movetothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT 
               | jumptothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT 
               | jumptothe DOSPUNTOS ID COMMA LEFTANDRIGHT """    

def p_moveandjumpindir_def(p):
    """moveandjumpindir_def : moveindir DOSPUNTOS ID COMMA CARDINAL 
               | moveindir DOSPUNTOS INTEGER COMMA CARDINAL 
               | jumpindir DOSPUNTOS INTEGER COMMA CARDINAL 
               | jumpindir DOSPUNTOS ID COMMA CARDINAL """
    
def p_move_def(p):
    """move_def : move DOSPUNTOS ID 
                | move DOSPUNTOS INTEGER """

def p_goto_def(p):
    """goto_def : goto DOSPUNTOS ID COMMA ID 
                | goto DOSPUNTOS INTEGER COMMA INTEGER 
                | goto DOSPUNTOS ID COMMA INTEGER 
                | goto DOSPUNTOS INTEGER COMMA ID """

def p_turn_def(p):
    """turn_def : turn DOSPUNTOS DIRECTION_TURN 
                | turn DOSPUNTOS LEFTANDRIGHT """
    
def p_face_def(p):
    """face_def : face DOSPUNTOS CARDINAL """

def p_nop_def(p):
    """nop_def : nop DOSPUNTOS """
    

success = True

def p_error(p):
    global success
    success = False

parser = yacc.yacc()

data = "ROBOT_R\nVARS nAm, y, z,arroz;\nPROCS\ngoWest [ |a,b| assignTo : 1 , y ; put : c , chips ; put : b , balloons] gaWest [ |a,b|if: nop: then: [if: nop: then: [nop:] else: [nop:]] else: [if: nop: then: [nop:] else: [nop:]]] mama[ |ab,sz| while: nop: do:[while: nop: do:[nop:]]]"

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
