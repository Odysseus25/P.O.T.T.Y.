
# /Users/Julio/Desktop/P.O.T.T.Y./parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = '251DD52429ECD897AE906AF3A1E8A1DB'
    
_lr_action_items = {'DORMIR':([2,3,4,6,7,8,10,13,15,16,33,35,36,38,39,40,41,54,55,56,57,],[-35,5,-7,-10,-12,-6,-4,-5,-3,-11,-33,-8,-34,-22,-23,-24,-21,-20,-31,-32,-9,]),'JUGAR':([0,],[2,]),'ENTONCES':([18,33,36,38,39,40,41,],[23,-33,-34,-22,-23,-24,-21,]),'DIFERENTE':([19,],[27,]),'VERDAD':([24,25,26,27,28,29,30,],[-29,-26,-27,-30,39,-25,-28,]),'MENTIRA':([24,25,26,27,28,29,30,],[-29,-26,-27,-30,40,-25,-28,]),'RESTA':([33,36,44,58,59,],[-33,-34,51,51,51,]),'DIV':([33,36,44,58,59,],[-33,-34,52,52,52,]),'MULT':([33,36,44,58,59,],[-33,-34,50,50,50,]),'HAGA':([2,3,4,6,7,8,10,13,15,16,21,32,33,35,36,37,38,39,40,41,42,45,46,54,55,56,57,],[-35,12,-7,-10,-12,-6,-4,-5,-3,-11,-35,12,-33,-8,-34,-35,-22,-23,-24,-21,-35,12,12,-20,-31,-32,-9,]),'ASIG':([14,],[22,]),'MENIGUAL':([19,],[24,]),'ESCRIBIR':([2,3,4,6,7,8,10,13,15,16,21,32,33,35,36,37,38,39,40,41,42,45,46,54,55,56,57,],[-35,8,-7,-10,-12,-6,-4,-5,-3,-11,-35,8,-33,-8,-34,-35,-22,-23,-24,-21,-35,8,8,-20,-31,-32,-9,]),'PRI':([12,22,23,31,],[21,34,37,42,]),'NUM':([11,22,24,25,26,27,28,29,30,34,49,50,51,52,53,],[20,36,-29,-26,-27,-30,36,-25,-28,36,59,-18,-17,-19,-16,]),'SUMA':([33,36,44,58,59,],[-33,-34,53,53,53,]),'DAR':([2,3,4,6,7,8,10,13,15,16,21,32,33,35,36,37,38,39,40,41,42,45,46,54,55,56,57,],[-35,11,-7,-10,-12,-6,-4,-5,-3,-11,-35,11,-33,-8,-34,-35,-22,-23,-24,-21,-35,11,11,-20,-31,-32,-9,]),'$end':([1,5,17,],[0,-2,-1,]),'PRD':([4,6,7,8,10,13,15,16,21,32,33,35,36,37,38,39,40,41,42,44,45,46,48,54,55,56,57,58,59,60,61,],[-7,-10,-12,-6,-4,-5,-3,-11,-35,43,-33,-8,-34,-35,-22,-23,-24,-21,-35,-15,54,55,57,-20,-31,-32,-9,-15,-15,-13,-14,]),'MAYIGUAL':([19,],[30,]),'MIENTRAS':([43,],[47,]),'MAYQ':([19,],[29,]),'VARIABLE':([2,3,4,6,7,8,9,10,13,15,16,21,32,33,35,36,37,38,39,40,41,42,45,46,47,49,50,51,52,53,54,55,56,57,],[-35,14,-7,-10,-12,-6,19,-4,-5,-3,-11,-35,14,-33,-8,-34,-35,-22,-23,-24,-21,-35,14,14,19,58,-18,-17,-19,-16,-20,-31,-32,-9,]),'IGUAL':([19,],[26,]),'LETRA':([22,24,25,26,27,28,29,30,34,],[33,-29,-26,-27,-30,33,-25,-28,33,]),'VUELTAS':([20,],[31,]),'MENQ':([19,],[25,]),'SI':([2,3,4,6,7,8,10,13,15,16,21,32,33,35,36,37,38,39,40,41,42,45,46,54,55,56,57,],[-35,9,-7,-10,-12,-6,-4,-5,-3,-11,-35,9,-33,-8,-34,-35,-22,-23,-24,-21,-35,9,9,-20,-31,-32,-9,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'aritExtra':([44,58,59,],[48,60,61,]),'for':([3,32,45,46,],[7,7,7,7,]),'asignacion':([3,32,45,46,],[15,15,15,15,]),'posibilidad':([28,],[41,]),'instruccion':([2,21,37,42,],[3,32,45,46,]),'dato':([22,28,34,],[35,38,44,]),'requisito':([9,47,],[18,56,]),'operador':([44,58,59,],[49,49,49,]),'while':([3,32,45,46,],[16,16,16,16,]),'aritmetica':([3,32,45,46,],[10,10,10,10,]),'condicion':([19,],[28,]),'programa':([0,],[1,]),'eof':([5,],[17,]),'condicional':([3,32,45,46,],[13,13,13,13,]),'empty':([2,21,37,42,],[4,4,4,4,]),'if':([3,32,45,46,],[6,6,6,6,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> JUGAR instruccion DORMIR eof','programa',4,'p_programa','potty.py',78),
  ('eof -> <empty>','eof',0,'p_eof','potty.py',83),
  ('instruccion -> instruccion asignacion','instruccion',2,'p_instruccion','potty.py',86),
  ('instruccion -> instruccion aritmetica','instruccion',2,'p_instruccion','potty.py',87),
  ('instruccion -> instruccion condicional','instruccion',2,'p_instruccion','potty.py',88),
  ('instruccion -> instruccion ESCRIBIR','instruccion',2,'p_instruccion','potty.py',89),
  ('instruccion -> empty','instruccion',1,'p_instruccion','potty.py',90),
  ('asignacion -> VARIABLE ASIG dato','asignacion',3,'p_asignacion','potty.py',98),
  ('aritmetica -> VARIABLE ASIG PRI dato aritExtra PRD','aritmetica',6,'p_aritmetica','potty.py',102),
  ('condicional -> if','condicional',1,'p_condicional','potty.py',106),
  ('condicional -> while','condicional',1,'p_condicional','potty.py',107),
  ('condicional -> for','condicional',1,'p_condicional','potty.py',108),
  ('aritExtra -> operador VARIABLE aritExtra','aritExtra',3,'p_aritExtra','potty.py',112),
  ('aritExtra -> operador NUM aritExtra','aritExtra',3,'p_aritExtra','potty.py',113),
  ('aritExtra -> <empty>','aritExtra',0,'p_aritExtra','potty.py',114),
  ('operador -> SUMA','operador',1,'p_operador','potty.py',118),
  ('operador -> RESTA','operador',1,'p_operador','potty.py',119),
  ('operador -> MULT','operador',1,'p_operador','potty.py',120),
  ('operador -> DIV','operador',1,'p_operador','potty.py',121),
  ('if -> SI requisito ENTONCES PRI instruccion PRD','if',6,'p_if','potty.py',125),
  ('requisito -> VARIABLE condicion posibilidad','requisito',3,'p_requisito','potty.py',129),
  ('posibilidad -> dato','posibilidad',1,'p_posibilidad','potty.py',133),
  ('posibilidad -> VERDAD','posibilidad',1,'p_posibilidad','potty.py',134),
  ('posibilidad -> MENTIRA','posibilidad',1,'p_posibilidad','potty.py',135),
  ('condicion -> MAYQ','condicion',1,'p_condicion','potty.py',138),
  ('condicion -> MENQ','condicion',1,'p_condicion','potty.py',139),
  ('condicion -> IGUAL','condicion',1,'p_condicion','potty.py',140),
  ('condicion -> MAYIGUAL','condicion',1,'p_condicion','potty.py',141),
  ('condicion -> MENIGUAL','condicion',1,'p_condicion','potty.py',142),
  ('condicion -> DIFERENTE','condicion',1,'p_condicion','potty.py',143),
  ('for -> DAR NUM VUELTAS PRI instruccion PRD','for',6,'p_for','potty.py',146),
  ('while -> HAGA PRI instruccion PRD MIENTRAS requisito','while',6,'p_while','potty.py',150),
  ('dato -> LETRA','dato',1,'p_dato','potty.py',154),
  ('dato -> NUM','dato',1,'p_dato','potty.py',155),
  ('empty -> <empty>','empty',0,'p_empty','potty.py',162),
]
