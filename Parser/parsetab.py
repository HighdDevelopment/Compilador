
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CARDINAL COMMA DIRECTION DIRECTION_TURN DOSPUNTOS ID INTEGER ITEMS LBRACKET LEFTANDRIGHT PLECA PROCS RBRACKET ROBOT_R SEMICOLON VARS assignTo canjumpindir canjumptothe canmoveindir canmovetothe canpick canput do else face facing goto if jumpindir jumptothe move moveindir movetothe nop not pick put repeat then turn whileprog : ROBOT_R var_def PROCS\n            | ROBOT_R var_def PROCS bloque_def\n            | ROBOT_R var_def PROCS bloque_def LBRACKET final_def RBRACKETvar_def : VARS ID_list SEMICOLONID_list : ID\n              | ID_list COMMA IDbloque_def : id_def\n                  | bloque_def id_defid_def : ID LBRACKET PLECA id_func PLECA func_def RBRACKETid_func : ID\n               | ID COMMA id_func\n               | \n    estructura_def : ID DOSPUNTOS INTEGER COMMA INTEGER final_def : estructura_def\n                 | final_def estructura_def \n    func_def : bloques_def\n             | if_else_def\n             | while_def\n             | repeat_def\n    bloques_def : function_def\n                   | bloques_def SEMICOLON function_defrepeat_def : repeat DOSPUNTOS conditions_def LBRACKET bloques_def RBRACKET\n                  | repeat DOSPUNTOS conditions_def LBRACKET if_else_def RBRACKET\n                  | repeat DOSPUNTOS conditions_def LBRACKET while_def RBRACKET\n                  | repeat DOSPUNTOS conditions_def LBRACKET repeat_def RBRACKETif_else_def : if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET bloques_def RBRACKET else DOSPUNTOS LBRACKET bloques_def RBRACKET\n                   | if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET if_else_def RBRACKET else DOSPUNTOS LBRACKET bloques_def RBRACKET\n                   | if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET bloques_def RBRACKET else DOSPUNTOS LBRACKET if_else_def RBRACKET\n                   | if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET if_else_def RBRACKET else DOSPUNTOS LBRACKET if_else_def RBRACKETwhile_def : while DOSPUNTOS conditions_def do DOSPUNTOS LBRACKET bloques_def RBRACKET\n                 | while DOSPUNTOS conditions_def do DOSPUNTOS LBRACKET if_else_def RBRACKET\n                 | while DOSPUNTOS conditions_def do DOSPUNTOS LBRACKET while_def RBRACKETfunction_def : assignTo_def\n                    | put_def\n                    | moveandjumptothe_def\n                    | moveandjumpindir_def\n                    | move_def\n                    | goto_def\n                    | turn_def\n                    | face_def\n                    | nop_defassignTo_def : assignTo DOSPUNTOS INTEGER COMMA IDput_def : put DOSPUNTOS ID COMMA ITEMS \n               | put DOSPUNTOS INTEGER COMMA ITEMS \n               | pick DOSPUNTOS INTEGER COMMA ITEMS \n               | pick DOSPUNTOS ID COMMA ITEMS moveandjumptothe_def : movetothe DOSPUNTOS ID COMMA DIRECTION \n               | movetothe DOSPUNTOS INTEGER COMMA DIRECTION \n               | jumptothe DOSPUNTOS INTEGER COMMA DIRECTION \n               | jumptothe DOSPUNTOS ID COMMA DIRECTION \n               | movetothe DOSPUNTOS ID COMMA LEFTANDRIGHT \n               | movetothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT \n               | jumptothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT \n               | jumptothe DOSPUNTOS ID COMMA LEFTANDRIGHT moveandjumpindir_def : moveindir DOSPUNTOS ID COMMA CARDINAL \n               | moveindir DOSPUNTOS INTEGER COMMA CARDINAL \n               | jumpindir DOSPUNTOS INTEGER COMMA CARDINAL \n               | jumpindir DOSPUNTOS ID COMMA CARDINAL move_def : move DOSPUNTOS ID \n                | move DOSPUNTOS INTEGER goto_def : goto DOSPUNTOS ID COMMA ID \n                | goto DOSPUNTOS INTEGER COMMA INTEGER \n                | goto DOSPUNTOS ID COMMA INTEGER \n                | goto DOSPUNTOS INTEGER COMMA ID turn_def : turn DOSPUNTOS DIRECTION_TURN \n                | turn DOSPUNTOS LEFTANDRIGHT face_def : face DOSPUNTOS CARDINAL nop_def : nop DOSPUNTOS conditions_def : facing_def\n                    | canputpick_def\n                    | canmoveandjumptothe_def\n                    | canmoveandjumpindir_def\n                    | not_deffacing_def : facing DOSPUNTOS CARDINAL canputpick_def : canput DOSPUNTOS ID COMMA ITEMS \n               | canput DOSPUNTOS INTEGER COMMA ITEMS \n               | canpick DOSPUNTOS INTEGER COMMA ITEMS \n               | canpick DOSPUNTOS ID COMMA ITEMS canmoveandjumpindir_def : canmoveindir DOSPUNTOS ID COMMA CARDINAL \n               | canmoveindir DOSPUNTOS INTEGER COMMA CARDINAL \n               | canjumpindir DOSPUNTOS INTEGER COMMA CARDINAL \n               | canjumpindir DOSPUNTOS ID COMMA CARDINAL canmoveandjumptothe_def : canmovetothe DOSPUNTOS ID COMMA DIRECTION \n               | canmovetothe DOSPUNTOS INTEGER COMMA DIRECTION \n               | canjumptothe DOSPUNTOS INTEGER COMMA DIRECTION \n               | canjumptothe DOSPUNTOS ID COMMA DIRECTION \n               | canmovetothe DOSPUNTOS ID COMMA LEFTANDRIGHT \n               | canmovetothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT \n               | canjumptothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT \n               | canjumptothe DOSPUNTOS ID COMMA LEFTANDRIGHT not_def : not DOSPUNTOS conditions_def'
    
_lr_action_items = {'ROBOT_R':([0,],[2,]),'$end':([1,5,8,9,14,21,62,],[0,-1,-2,-7,-8,-3,-9,]),'VARS':([2,],[4,]),'PROCS':([3,11,],[5,-4,]),'ID':([4,5,8,9,12,13,14,17,18,20,22,27,61,62,68,69,70,71,72,73,74,75,118,119,120,121,122,123,127,140,141,],[7,10,10,-7,16,19,-8,19,-14,24,-15,24,-13,-9,97,100,101,104,105,108,109,111,144,147,148,151,152,155,162,179,182,]),'SEMICOLON':([6,7,16,32,36,40,41,42,43,44,45,46,47,48,78,79,109,110,113,114,115,158,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,201,219,233,236,],[11,-5,-6,63,-20,-33,-34,-35,-36,-37,-38,-39,-40,-41,-68,-21,-59,-60,-65,-66,-67,63,-42,-43,-44,-45,-46,-47,-51,-48,-52,-49,-53,-50,-54,-55,-56,-57,-58,-61,-63,-62,-64,63,63,63,63,]),'COMMA':([6,7,16,24,26,96,97,98,99,100,101,102,103,104,105,106,107,108,111,112,144,145,146,147,148,149,150,151,152,153,154,155,],[12,-5,-6,27,29,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,184,185,186,187,188,189,190,191,192,193,194,195,]),'LBRACKET':([8,9,10,14,62,81,82,83,84,85,95,142,143,156,157,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,229,230,],[13,-7,15,-8,-9,-69,-70,-71,-72,-73,126,183,-74,-91,196,-75,-76,-77,-78,-83,-87,-84,-88,-85,-89,-86,-90,-79,-80,-81,-82,231,232,]),'PLECA':([15,20,24,25,27,30,],[20,-12,-10,28,-12,-11,]),'RBRACKET':([17,18,22,31,32,33,34,35,36,40,41,42,43,44,45,46,47,48,61,78,79,109,110,113,114,115,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,197,198,199,200,201,202,219,220,221,224,225,226,233,234,235,236,237,238,239,240,],[21,-14,-15,62,-16,-17,-18,-19,-20,-33,-34,-35,-36,-37,-38,-39,-40,-41,-13,-68,-21,-59,-60,-65,-66,-67,197,198,199,200,-42,-43,-44,-45,-46,-47,-51,-48,-52,-49,-53,-50,-54,-55,-56,-57,-58,-61,-63,-62,-64,-22,-23,-24,-25,222,223,224,225,226,-30,-31,-32,237,238,239,240,-26,-28,-29,-27,]),'DOSPUNTOS':([19,37,38,39,49,50,51,52,53,54,55,56,57,58,59,60,86,87,88,89,90,91,92,93,116,125,227,228,],[23,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,117,118,119,120,121,122,123,124,142,157,229,230,]),'INTEGER':([23,29,67,68,69,70,71,72,73,74,75,118,119,120,121,122,123,140,141,],[26,61,96,98,99,102,103,106,107,110,112,145,146,149,150,153,154,180,181,]),'if':([28,126,183,196,231,232,],[37,37,37,37,37,37,]),'while':([28,126,196,],[38,38,38,]),'repeat':([28,126,],[39,39,]),'assignTo':([28,63,126,183,196,231,232,],[49,49,49,49,49,49,49,]),'put':([28,63,126,183,196,231,232,],[50,50,50,50,50,50,50,]),'pick':([28,63,126,183,196,231,232,],[51,51,51,51,51,51,51,]),'movetothe':([28,63,126,183,196,231,232,],[52,52,52,52,52,52,52,]),'jumptothe':([28,63,126,183,196,231,232,],[53,53,53,53,53,53,53,]),'moveindir':([28,63,126,183,196,231,232,],[54,54,54,54,54,54,54,]),'jumpindir':([28,63,126,183,196,231,232,],[55,55,55,55,55,55,55,]),'move':([28,63,126,183,196,231,232,],[56,56,56,56,56,56,56,]),'goto':([28,63,126,183,196,231,232,],[57,57,57,57,57,57,57,]),'turn':([28,63,126,183,196,231,232,],[58,58,58,58,58,58,58,]),'face':([28,63,126,183,196,231,232,],[59,59,59,59,59,59,59,]),'nop':([28,63,126,183,196,231,232,],[60,60,60,60,60,60,60,]),'facing':([64,65,66,124,],[86,86,86,86,]),'canput':([64,65,66,124,],[87,87,87,87,]),'canpick':([64,65,66,124,],[88,88,88,88,]),'canmovetothe':([64,65,66,124,],[89,89,89,89,]),'canjumptothe':([64,65,66,124,],[90,90,90,90,]),'canmoveindir':([64,65,66,124,],[91,91,91,91,]),'canjumpindir':([64,65,66,124,],[92,92,92,92,]),'not':([64,65,66,124,],[93,93,93,93,]),'DIRECTION_TURN':([76,],[113,]),'LEFTANDRIGHT':([76,132,133,134,135,188,189,190,191,],[114,168,170,172,174,208,210,212,214,]),'CARDINAL':([77,117,136,137,138,139,192,193,194,195,],[115,143,175,176,177,178,215,216,217,218,]),'then':([80,81,82,83,84,85,143,156,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,],[116,-69,-70,-71,-72,-73,-74,-91,-75,-76,-77,-78,-83,-87,-84,-88,-85,-89,-86,-90,-79,-80,-81,-82,]),'do':([81,82,83,84,85,94,143,156,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,],[-69,-70,-71,-72,-73,125,-74,-91,-75,-76,-77,-78,-83,-87,-84,-88,-85,-89,-86,-90,-79,-80,-81,-82,]),'ITEMS':([128,129,130,131,184,185,186,187,],[163,164,165,166,203,204,205,206,]),'DIRECTION':([132,133,134,135,188,189,190,191,],[167,169,171,173,207,209,211,213,]),'else':([222,223,],[227,228,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'var_def':([2,],[3,]),'ID_list':([4,],[6,]),'bloque_def':([5,],[8,]),'id_def':([5,8,],[9,14,]),'final_def':([13,],[17,]),'estructura_def':([13,17,],[18,22,]),'id_func':([20,27,],[25,30,]),'func_def':([28,],[31,]),'bloques_def':([28,126,183,196,231,232,],[32,158,201,219,233,236,]),'if_else_def':([28,126,183,196,231,232,],[33,159,202,220,234,235,]),'while_def':([28,126,196,],[34,160,221,]),'repeat_def':([28,126,],[35,161,]),'function_def':([28,63,126,183,196,231,232,],[36,79,36,36,36,36,36,]),'assignTo_def':([28,63,126,183,196,231,232,],[40,40,40,40,40,40,40,]),'put_def':([28,63,126,183,196,231,232,],[41,41,41,41,41,41,41,]),'moveandjumptothe_def':([28,63,126,183,196,231,232,],[42,42,42,42,42,42,42,]),'moveandjumpindir_def':([28,63,126,183,196,231,232,],[43,43,43,43,43,43,43,]),'move_def':([28,63,126,183,196,231,232,],[44,44,44,44,44,44,44,]),'goto_def':([28,63,126,183,196,231,232,],[45,45,45,45,45,45,45,]),'turn_def':([28,63,126,183,196,231,232,],[46,46,46,46,46,46,46,]),'face_def':([28,63,126,183,196,231,232,],[47,47,47,47,47,47,47,]),'nop_def':([28,63,126,183,196,231,232,],[48,48,48,48,48,48,48,]),'conditions_def':([64,65,66,124,],[80,94,95,156,]),'facing_def':([64,65,66,124,],[81,81,81,81,]),'canputpick_def':([64,65,66,124,],[82,82,82,82,]),'canmoveandjumptothe_def':([64,65,66,124,],[83,83,83,83,]),'canmoveandjumpindir_def':([64,65,66,124,],[84,84,84,84,]),'not_def':([64,65,66,124,],[85,85,85,85,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> ROBOT_R var_def PROCS','prog',3,'p_prog','parser.py',244),
  ('prog -> ROBOT_R var_def PROCS bloque_def','prog',4,'p_prog','parser.py',245),
  ('prog -> ROBOT_R var_def PROCS bloque_def LBRACKET final_def RBRACKET','prog',7,'p_prog','parser.py',246),
  ('var_def -> VARS ID_list SEMICOLON','var_def',3,'p_var_def','parser.py',250),
  ('ID_list -> ID','ID_list',1,'p_ID_list','parser.py',256),
  ('ID_list -> ID_list COMMA ID','ID_list',3,'p_ID_list','parser.py',257),
  ('bloque_def -> id_def','bloque_def',1,'p_bloque_def','parser.py',264),
  ('bloque_def -> bloque_def id_def','bloque_def',2,'p_bloque_def','parser.py',265),
  ('id_def -> ID LBRACKET PLECA id_func PLECA func_def RBRACKET','id_def',7,'p_id_def','parser.py',268),
  ('id_func -> ID','id_func',1,'p_id_func','parser.py',271),
  ('id_func -> ID COMMA id_func','id_func',3,'p_id_func','parser.py',272),
  ('id_func -> <empty>','id_func',0,'p_id_func','parser.py',273),
  ('estructura_def -> ID DOSPUNTOS INTEGER COMMA INTEGER','estructura_def',5,'p_estructura_def','parser.py',281),
  ('final_def -> estructura_def','final_def',1,'p_final_def','parser.py',288),
  ('final_def -> final_def estructura_def','final_def',2,'p_final_def','parser.py',289),
  ('func_def -> bloques_def','func_def',1,'p_func_def','parser.py',295),
  ('func_def -> if_else_def','func_def',1,'p_func_def','parser.py',296),
  ('func_def -> while_def','func_def',1,'p_func_def','parser.py',297),
  ('func_def -> repeat_def','func_def',1,'p_func_def','parser.py',298),
  ('bloques_def -> function_def','bloques_def',1,'p_bloques_def','parser.py',302),
  ('bloques_def -> bloques_def SEMICOLON function_def','bloques_def',3,'p_bloques_def','parser.py',303),
  ('repeat_def -> repeat DOSPUNTOS conditions_def LBRACKET bloques_def RBRACKET','repeat_def',6,'p_repeat_def','parser.py',306),
  ('repeat_def -> repeat DOSPUNTOS conditions_def LBRACKET if_else_def RBRACKET','repeat_def',6,'p_repeat_def','parser.py',307),
  ('repeat_def -> repeat DOSPUNTOS conditions_def LBRACKET while_def RBRACKET','repeat_def',6,'p_repeat_def','parser.py',308),
  ('repeat_def -> repeat DOSPUNTOS conditions_def LBRACKET repeat_def RBRACKET','repeat_def',6,'p_repeat_def','parser.py',309),
  ('if_else_def -> if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET bloques_def RBRACKET else DOSPUNTOS LBRACKET bloques_def RBRACKET','if_else_def',13,'p_if_else_def','parser.py',312),
  ('if_else_def -> if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET if_else_def RBRACKET else DOSPUNTOS LBRACKET bloques_def RBRACKET','if_else_def',13,'p_if_else_def','parser.py',313),
  ('if_else_def -> if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET bloques_def RBRACKET else DOSPUNTOS LBRACKET if_else_def RBRACKET','if_else_def',13,'p_if_else_def','parser.py',314),
  ('if_else_def -> if DOSPUNTOS conditions_def then DOSPUNTOS LBRACKET if_else_def RBRACKET else DOSPUNTOS LBRACKET if_else_def RBRACKET','if_else_def',13,'p_if_else_def','parser.py',315),
  ('while_def -> while DOSPUNTOS conditions_def do DOSPUNTOS LBRACKET bloques_def RBRACKET','while_def',8,'p_while_def','parser.py',318),
  ('while_def -> while DOSPUNTOS conditions_def do DOSPUNTOS LBRACKET if_else_def RBRACKET','while_def',8,'p_while_def','parser.py',319),
  ('while_def -> while DOSPUNTOS conditions_def do DOSPUNTOS LBRACKET while_def RBRACKET','while_def',8,'p_while_def','parser.py',320),
  ('function_def -> assignTo_def','function_def',1,'p_function_def','parser.py',323),
  ('function_def -> put_def','function_def',1,'p_function_def','parser.py',324),
  ('function_def -> moveandjumptothe_def','function_def',1,'p_function_def','parser.py',325),
  ('function_def -> moveandjumpindir_def','function_def',1,'p_function_def','parser.py',326),
  ('function_def -> move_def','function_def',1,'p_function_def','parser.py',327),
  ('function_def -> goto_def','function_def',1,'p_function_def','parser.py',328),
  ('function_def -> turn_def','function_def',1,'p_function_def','parser.py',329),
  ('function_def -> face_def','function_def',1,'p_function_def','parser.py',330),
  ('function_def -> nop_def','function_def',1,'p_function_def','parser.py',331),
  ('assignTo_def -> assignTo DOSPUNTOS INTEGER COMMA ID','assignTo_def',5,'p_assignTo_def','parser.py',335),
  ('put_def -> put DOSPUNTOS ID COMMA ITEMS','put_def',5,'p_put_def','parser.py',343),
  ('put_def -> put DOSPUNTOS INTEGER COMMA ITEMS','put_def',5,'p_put_def','parser.py',344),
  ('put_def -> pick DOSPUNTOS INTEGER COMMA ITEMS','put_def',5,'p_put_def','parser.py',345),
  ('put_def -> pick DOSPUNTOS ID COMMA ITEMS','put_def',5,'p_put_def','parser.py',346),
  ('moveandjumptothe_def -> movetothe DOSPUNTOS ID COMMA DIRECTION','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',349),
  ('moveandjumptothe_def -> movetothe DOSPUNTOS INTEGER COMMA DIRECTION','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',350),
  ('moveandjumptothe_def -> jumptothe DOSPUNTOS INTEGER COMMA DIRECTION','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',351),
  ('moveandjumptothe_def -> jumptothe DOSPUNTOS ID COMMA DIRECTION','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',352),
  ('moveandjumptothe_def -> movetothe DOSPUNTOS ID COMMA LEFTANDRIGHT','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',353),
  ('moveandjumptothe_def -> movetothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',354),
  ('moveandjumptothe_def -> jumptothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',355),
  ('moveandjumptothe_def -> jumptothe DOSPUNTOS ID COMMA LEFTANDRIGHT','moveandjumptothe_def',5,'p_moveandjumptothe_def','parser.py',356),
  ('moveandjumpindir_def -> moveindir DOSPUNTOS ID COMMA CARDINAL','moveandjumpindir_def',5,'p_moveandjumpindir_def','parser.py',359),
  ('moveandjumpindir_def -> moveindir DOSPUNTOS INTEGER COMMA CARDINAL','moveandjumpindir_def',5,'p_moveandjumpindir_def','parser.py',360),
  ('moveandjumpindir_def -> jumpindir DOSPUNTOS INTEGER COMMA CARDINAL','moveandjumpindir_def',5,'p_moveandjumpindir_def','parser.py',361),
  ('moveandjumpindir_def -> jumpindir DOSPUNTOS ID COMMA CARDINAL','moveandjumpindir_def',5,'p_moveandjumpindir_def','parser.py',362),
  ('move_def -> move DOSPUNTOS ID','move_def',3,'p_move_def','parser.py',365),
  ('move_def -> move DOSPUNTOS INTEGER','move_def',3,'p_move_def','parser.py',366),
  ('goto_def -> goto DOSPUNTOS ID COMMA ID','goto_def',5,'p_goto_def','parser.py',369),
  ('goto_def -> goto DOSPUNTOS INTEGER COMMA INTEGER','goto_def',5,'p_goto_def','parser.py',370),
  ('goto_def -> goto DOSPUNTOS ID COMMA INTEGER','goto_def',5,'p_goto_def','parser.py',371),
  ('goto_def -> goto DOSPUNTOS INTEGER COMMA ID','goto_def',5,'p_goto_def','parser.py',372),
  ('turn_def -> turn DOSPUNTOS DIRECTION_TURN','turn_def',3,'p_turn_def','parser.py',375),
  ('turn_def -> turn DOSPUNTOS LEFTANDRIGHT','turn_def',3,'p_turn_def','parser.py',376),
  ('face_def -> face DOSPUNTOS CARDINAL','face_def',3,'p_face_def','parser.py',379),
  ('nop_def -> nop DOSPUNTOS','nop_def',2,'p_nop_def','parser.py',382),
  ('conditions_def -> facing_def','conditions_def',1,'p_conditions_def','parser.py',388),
  ('conditions_def -> canputpick_def','conditions_def',1,'p_conditions_def','parser.py',389),
  ('conditions_def -> canmoveandjumptothe_def','conditions_def',1,'p_conditions_def','parser.py',390),
  ('conditions_def -> canmoveandjumpindir_def','conditions_def',1,'p_conditions_def','parser.py',391),
  ('conditions_def -> not_def','conditions_def',1,'p_conditions_def','parser.py',392),
  ('facing_def -> facing DOSPUNTOS CARDINAL','facing_def',3,'p_facing_def','parser.py',396),
  ('canputpick_def -> canput DOSPUNTOS ID COMMA ITEMS','canputpick_def',5,'p_canputpick_def','parser.py',399),
  ('canputpick_def -> canput DOSPUNTOS INTEGER COMMA ITEMS','canputpick_def',5,'p_canputpick_def','parser.py',400),
  ('canputpick_def -> canpick DOSPUNTOS INTEGER COMMA ITEMS','canputpick_def',5,'p_canputpick_def','parser.py',401),
  ('canputpick_def -> canpick DOSPUNTOS ID COMMA ITEMS','canputpick_def',5,'p_canputpick_def','parser.py',402),
  ('canmoveandjumpindir_def -> canmoveindir DOSPUNTOS ID COMMA CARDINAL','canmoveandjumpindir_def',5,'p_canmoveandjumpindir_def','parser.py',405),
  ('canmoveandjumpindir_def -> canmoveindir DOSPUNTOS INTEGER COMMA CARDINAL','canmoveandjumpindir_def',5,'p_canmoveandjumpindir_def','parser.py',406),
  ('canmoveandjumpindir_def -> canjumpindir DOSPUNTOS INTEGER COMMA CARDINAL','canmoveandjumpindir_def',5,'p_canmoveandjumpindir_def','parser.py',407),
  ('canmoveandjumpindir_def -> canjumpindir DOSPUNTOS ID COMMA CARDINAL','canmoveandjumpindir_def',5,'p_canmoveandjumpindir_def','parser.py',408),
  ('canmoveandjumptothe_def -> canmovetothe DOSPUNTOS ID COMMA DIRECTION','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',411),
  ('canmoveandjumptothe_def -> canmovetothe DOSPUNTOS INTEGER COMMA DIRECTION','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',412),
  ('canmoveandjumptothe_def -> canjumptothe DOSPUNTOS INTEGER COMMA DIRECTION','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',413),
  ('canmoveandjumptothe_def -> canjumptothe DOSPUNTOS ID COMMA DIRECTION','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',414),
  ('canmoveandjumptothe_def -> canmovetothe DOSPUNTOS ID COMMA LEFTANDRIGHT','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',415),
  ('canmoveandjumptothe_def -> canmovetothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',416),
  ('canmoveandjumptothe_def -> canjumptothe DOSPUNTOS INTEGER COMMA LEFTANDRIGHT','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',417),
  ('canmoveandjumptothe_def -> canjumptothe DOSPUNTOS ID COMMA LEFTANDRIGHT','canmoveandjumptothe_def',5,'p_canmoveandjumptothe_def','parser.py',418),
  ('not_def -> not DOSPUNTOS conditions_def','not_def',3,'p_not_def','parser.py',421),
]
