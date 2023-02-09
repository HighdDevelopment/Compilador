import ply.lex as lex
import ply.yacc as yacc

tokens = [
    'ID',
    'INTEGER',
    'PLECA',
    'DOSPUNTOS',
    'COMMA',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'assignTo'
]

t_PLECA = r'\|'
t_DOSPUNTOS = r':'
t_COMMA = r','
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_assignTo(t):
    r'assingTo'
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def p_assignTo_def(p):
    'assignTo_def : assignTo DOSPUNTOS INTEGER COMMA ID SEMICOLON'
    if p[5] in global_variables:
        global_variables[p[5]] = p[3]
        p[0] = (p[3], p[5])
    else:
        raise ValueError(f"Variable {p[5]} no se encuentra en global_variables")

def p_id_def(p):
    '''id_def : ID LBRACKET PLECA ID COMMA ID PLECA RBRACKET 
              | ID LBRACKET PLECA ID COMMA ID PLECA TEXT RBRACKET '''
    if len(p) == 8:
        p[0] = (p[3], p[5])
    else:
        p[0] = (p[3], p[5], p[9])


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()



global_variables = {}

text = 'assignTo : 1 , one ;\n5 put : c , chips ; put : b , balloons ]'
lexer.input(text)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)

result = parser.parse(text)
print(result)
print(global_variables)