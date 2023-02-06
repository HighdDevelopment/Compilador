numeros = {"1","2","3","4","5","6","7","8","9","0"}


commands = {"M", "R", "C", "B", "c", "b", "P", "J", "G"}

cardinals = {"north", "south", "west", "east"}

objects = {"balloons", "chips"}

direction ={"front", "right", "left", "back", "around"}

conditional = {"if", "then", "else"}

loop = {"while", "do"}

repeat = {"repeat"}

signs = {":;,()][|"}

procedure={
    "assignTo",
    "goTo",
    "move",
    "turn", 
    "face",
    "put",
    "pick",
    "moveToThe",
    "moveInDir",
    "jumpToThe",
    "jumpInDir",
    "nop"}

condition ={
    "facing",
    "canPut",
    "canPick",
    "canMoveInDir",
    "canJumpInDir",
    "canMoveToThe",
    "canJumpToThe",
    "not"}
    

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
    contenido = data.replace("\n", " ")

    """
    Se abre el archivo .txt
    """

    token =""
    """
    En esta variable se guardara las cadenas que se formen durante el ciclo
    """

    """
    Se convierte el archivo txt en una lista y se guarda en filecontents
    """

    for valor in contenido:
        token+=valor.replace(" ","").replace("\t", "")
        """
        Las condiciones para guardar el token en la lista se dan cuando valor tome un espacio en blanco
        o un salto de linea, paso seguido a guardar la informacion y reiniciando el token
        """
        if valor == " ":
            if token in numeros:
                lexico.append(f"NUMBER({token})")
                token = ""
            elif token in commands:
                lexico.append(f"COMMANDS({token})")
                token = ""

            elif token in loop:
                lexico.append(f"LOOP({token})")
                token = ""            

            elif token in cardinals:
                lexico.append(f"CARDINALS({token})")
                token = ""                
            elif token in objects:
                lexico.append(f"OBJECTS({token})")
                token = ""
            elif token in direction:
                lexico.append(f"DIRECTION({token})")
                token = ""
            elif token in conditional:
                lexico.append(f"CONDITIONAL({token})")
                token = ""
            elif token in repeat:
                lexico.append(f"REPEAT({token})")
                token = ""
            elif token in signs:
                lexico.append(f"SIGNS({token})")
                token = ""
            elif token in condition:  
                lexico.append(f"CONDITION({token})")
                token = ""
            elif token in procedure:
                lexico.append(f"PROCEDURE({token})")
                token = ""      
            else:
                lexico.append(token)
                token = ""
    
    if valor != " ":
        lexico.append(valor)
    
    return lexico




