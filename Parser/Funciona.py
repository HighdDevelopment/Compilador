import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'ROBOT_R',
    'VARS',
    'ID',
    'COMMA',
    'SEMICOLON'
)

def t_ROBOT_R(t):
    r'ROBOT_R'
    return t

def t_VARS(t):
    r'VARS'
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_COMMA(t):
    r','
    return t

def t_SEMICOLON(t):
    r';'
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
    'prog : ROBOT_R var_def'
    p[0] = p[2]

def p_var_def(p):
    'var_def : VARS ID_list SEMICOLON'
    p[0] = p[2]

def p_ID_list(p):
    '''ID_list : ID
              | ID_list COMMA ID'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

data = "ROBOT_R\nVARS nam, y, z;\n"

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(data)
print(result)
