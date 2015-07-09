import ply.lex as lex 
import ply.yacc as yacc
import sys

reservadas = {
	'JUGAR' : 'JUGAR',
	'DORMIR' : 'DORMIR',
	'DAR' : 'DAR',
	'VUELTAS' : 'VUELTAS',
	'SI' : 'SI',
	'ENTONCES' : 'ENTONCES',
	'HAGA' : 'HAGA',
	'MIENTRAS' : 'MIENTRAS',
	'ESCRIBIR' : 'ESCRIBIR',
	'VERDAD' : 'VERDAD',
	'MENTIRA' : 'MENTIRA'

}

tokens = ['SUMA', 'RESTA', 'DIV', 'MULT', 'PRI', 'PRD', 'ASIG', 'MAYQ', 'MENQ', 'IGUAL', 'MAYIGUAL', 'MENIGUAL', 'DIFERENTE', 'VARIABLE', 'NUM', 'LETRA', 'FINDELINEA', 'ID'] + list(reservadas.values())

t_SUMA = r'\+'
t_RESTA = r'-'
t_DIV = r'/'
t_MULT = r'\*'
t_PRI = r'\('
t_PRD = r'\)'
t_ASIG = r'='
t_MAYQ = r'>'
t_MENQ = r'<'
t_IGUAL= r'=='
t_MAYIGUAL = r'>='
t_MENIGUAL = r'<='
t_DIFERENTE = r'!='
t_VARIABLE = r'([a-z]+[A-Z]*[0-9]*)+'
t_LETRA = r'[a-zA-Z]'
	
def t_NUM(t):
	r'[0-9]+'
	return t
	
def t_FINDELINEA(t):
    r'(\n)+'
    t.lexer.lineno += t.value.count("\n")
    return t

#funcion que determina el numero de linea 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    t.type = reservadas.get(t.value, 'ID')    # Chequea palabras reservadas
    return t
	
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0] + " en la linea " + str(t.lexer.lineno))
    t.lexer.skip(1)

t_ignore = " \t"	

import ply.lex as lex
lex.lex()
#lexer.input("JUGAR SI 6 > 7")

# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print tok



##### PARSER

def p_programa(p):
	'''programa : JUGAR instruccion DORMIR eof'''
	p[0] = p[1] + " " + p[2] + " " + p[3]
	#print(p[0])
	
def p_eof(p):
	'''eof : '''
	
def p_instruccion(p):
	'''instruccion : instruccion asignacion
					| instruccion aritmetica
					| instruccion condicional
					| instruccion ESCRIBIR
					| empty'''
	if p[1] is None:
		p[0] = ""
	else:
		if [1] is not None:
			p[0] = p[1] + " " + p[2]
		else:
			p[0] = p[2]
		
	
def p_asignacion(p):
	'''asignacion : VARIABLE ASIG dato'''
	p[0] = p[1] + " " + p[2] + " " + p[3]
	
def p_aritmetica(p):
	'''aritmetica : VARIABLE ASIG PRI dato aritExtra PRD'''
	#p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
	
def p_condicional(p):
	'''condicional : if
					| while
					| for'''
	#p[0] = p[1]
					
def p_aritExtra(p):
	'''aritExtra : operador VARIABLE aritExtra 
				  | operador NUM aritExtra
				  | '''
	#condicional
				  
def p_operador(p):
	'''operador : SUMA
				   | RESTA
				   | MULT
				   | DIV'''
	# if p[2] == '+': p[0] = 
				   
def p_if(p):
	'''if : SI requisito ENTONCES PRI instruccion PRD'''
	#p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
	 
def p_requisito(p):
	'''requisito : VARIABLE condicion posibilidad'''
	#p[0] = p[1] + p[2] + p[3]
	
def p_posibilidad(p):
	'''posibilidad : dato
				    | VERDAD
					| MENTIRA'''
					
def p_condicion(p):
	'''condicion : MAYQ
				  | MENQ
				  | IGUAL
				  | MAYIGUAL
				  | MENIGUAL
				  | DIFERENTE'''
				  
def p_for(p):
	'''for : DAR NUM VUELTAS PRI instruccion PRD'''
	#p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
	
def p_while(p):
	'''while : HAGA PRI instruccion PRD MIENTRAS requisito'''
	#p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
			
def p_dato(p):
	'''dato : LETRA
			 | NUM'''
	p[0] = p[1]

def p_error(p):
    print ("ERROR FATAL")

def p_empty(p): 
	'empty :'
	pass

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('potty> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)	  

# try:
#     file = open(filename,'r')
# except FileNotFoundError:
#     print("Archivo no encontrado: ",filename)
# continue
				  