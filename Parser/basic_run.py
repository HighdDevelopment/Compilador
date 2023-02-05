import lexer as lx
import parser as pr



def run():
    info = lx.abrir_archivo("test.lang")
    print(pr.Analizador(info))
run()