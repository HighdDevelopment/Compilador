numeros ={"1","2","3","4","5","6","7","8","9","0"}
procedure={
    "assignTo",
    "goto",
    "move",
    "turn", 
    "face",
    "put",
    "pick",
    "moveToThe",
    "moveInDir",
    "jumpToThe",
    "jumpInDir",
    "nop",
    "ROBOT_R"

}

vars = []
ltimo= ""
def VARS(tokens,ultimo):
    resultado = True
    if tokens[0] not in numeros:
        resultado = True
    ultimo = tokens

def analizador(tokens):
    indx = 0
    respuesta = True
    reservada = ""
    while respuesta and (indx!=len(tokens)-1):
        if tokens[0] != "ROBOT_R":
            respuesta = False 
        indx+=1

