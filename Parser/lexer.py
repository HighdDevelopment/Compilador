numeros = {
    "1","2","3","4","5","6","7","8","9","0"
}


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
    "VARS",
    "facing",
    "canPut",
    "canPick",
    "canMoveInDir",
    "canJumpInDir",
    "canMoveToThe",
    "canJumpToThe",
    "nop",
    ",",
    ";"
}
"""
La siguiente funcion se encarga de registrar en una lista nativa de python los tokens
que posteriormente se deben ingresar al parser
"""

def abrir_archivo(filename):

    lexico = []
    """
    Se inicia una lista donde se guardaran los tokens
    """
    
    data = open(filename,"r").read()
    """
    Se abre el archivo .txt
    """

    token =""
    """
    En esta variable se guardara las cadenas que se formen durante el ciclo
    """

    filecontents = list(data)
    """
    Se convierte el archivo txt en una lista y se guarda en filecontents
    """

    for valor in filecontents:
        token+=valor.replace("\n","").replace(" ","")
        """
        Las condiciones para guardar el token en la lista se dan cuando valor tome un espacio en blanco
        o un salto de linea, paso seguido a guardar la informacion y reiniciando el token
        """
        if valor == " ":
            if token in numeros:
                lexico.append(f"NUMBER({token})")
                token = ""
            elif token not in procedure:
                lexico.append(f"ID({token})")
                token = ""
            else:
                lexico.append(token)
                token = ""
    
    if valor != " ":
        lexico.append(valor)
    
    return lexico




