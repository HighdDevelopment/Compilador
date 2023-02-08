import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'ROBOT_R',
    'VARS',
    'COMMA',
    'NAME',
    'SEMICOLON',
    "NEWLINE"
]

def t_ROBOT_R(t):
    r'ROBOT_R'
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1

def t_VARS(t):
    r'VARS'
    return t

def t_COMMA(t):
    r','
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_SEMICOLON(t):
    r';'
    return t


t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_program(p):
    '''program : ROBOT_R NEWLINE vars'''
    p[0] = (p[1], p[3])

def p_vars(p):
    '''vars : VARS instances SEMICOLON'''
    p[0] = (p[1], p[2])

def p_instances(p):
    '''instances : NAME
                 | instances COMMA NAME'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

parser = yacc.yacc()

input_str = '''ROBOT_R\nVARS nom, x, y, one;'''

result = parser.parse(input_str)

print(result)


