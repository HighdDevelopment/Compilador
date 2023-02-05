tokens = {
    "ID","NUMBERS"
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
    "nop",
    "ROBOT_R"

}

vars = []

indx = 0
def analizador(tokens):
    if tokens[indx] in procedure:
        indx+=1
        analizador(tokens[indx])
    else: 
        return ""
            