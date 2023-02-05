
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
            lexico.append(token)
            token = ""
            
        elif valor == "\n":
            lexico.append(token)
            token = ""
    
    if valor != " ":
        lexico.append(valor)
    
    return lexico




