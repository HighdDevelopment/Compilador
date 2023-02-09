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
    'INTEGER'
    
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
    r'(?i)assignTo'
    return t

def t_ID(t):
    r'[a-zA-Z]+'
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
              | ID LBRACKET PLECA ID COMMA ID PLECA assignTo_def RBRACKET '''
    if len(p) == 8:
        p[0] = (p[3], p[5])
    else:
        p[0] = (p[3], p[5], p[9])


def p_assignTo_def(p):
    'assignTo_def : assignTo DOSPUNTOS INTEGER COMMA ID SEMICOLON'
    if p[5] in global_variables:
        global_variables[p[5]] = p[3]
        p[0] = (p[3], p[5])
    else:
        raise ValueError(f"Variable {p[5]} no se encuentra en global_variables")      
def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

data = "ROBOT_R\nVARS nam, y, z,arroz;\nPROCS\nPutCB[|c,b| ASsiGnTo:51,nam;]"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(data)
print(result)
print(global_variables)
