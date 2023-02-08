import ply.lex as lex
import ply.yacc as yacc



tokens = (
    'ROBOT_R',
    'VARS',
    'ID',
    'COMMA',
    'SEMICOLON',
    'PROCS',
    'PUT',
    'LBRACKET',
    'RBRACKET',
    'PLECA',
    'assignTo',
    'DOSPUNTOS',
    'INTEGER'
    
)

global_variables = {}

def t_ROBOT_R(t):
    r'ROBOT_R'
    return t

def t_VARS(t):
    r'VARS'
    return t

def t_PROCS(t):
    r'PROCS'
    return t

def t_PUT(t):
    r'PUT'
    return t

def t_assignTo(t):
    r'assignTo'
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
            | ROBOT_R var_def PROCS put_def'''
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

def p_put_def(p):
    '''put_def : PUT LBRACKET PLECA ID COMMA ID PLECA RBRACKET 
               | PUT LBRACKET PLECA ID COMMA ID PLECA assignTo_def RBRACKET '''
    if len(p) == 8:
        p[0] = (p[3], p[5])
    else:
        p[0] = (p[3], p[5], p[9])

def p_assignTo_def(p):
    'assignTo_def : assignTo DOSPUNTOS INTEGER COMMA ID SEMICOLON'
    global_variables[p[5]] = p[3]
    p[0] = (p[3], p[5])
    

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

data = "ROBOT_R\nVARS nam, y, z,arroz;\nPROCS\nPUT[|a,b| assignTo:51,arroz;]"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(data)
print(result)
print(global_variables)
