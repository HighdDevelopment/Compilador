import ply.lex as lexer
import lexer1 as lex

# Give the lexer some input
lexer.input(open("test.txt","r").read())

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
