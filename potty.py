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

stringStart = "#include <iostream>\nusing namespace std;\n\nint main( ){\n"

##### PARSER

def p_programa(p):
	'''programa : JUGAR instruccion DORMIR eof'''
	#p[0] = p[1] + " " + p[2] + " " + p[3]
	p[0] = stringStart + p[2] + "\n}"
	
def p_eof(p):
	'''eof : FINLINEA
			| empty'''

def p_finlinea(p):
	'''FINLINEA : FINDELINEA FINLINEA
				 | FINDELINEA'''
	
def p_instruccion(p):
	'''instruccion : instruccion asignacion
					| instruccion aritmetica
					| instruccion condicional
					| instruccion ESCRIBIR
					| empty'''
	if p[1] is None:
		p[0] = ""
	else:
		if p[1] is not None:
			p[0] = p[1] + " " + p[2]
		else:
			p[0] = p[2]
		
	
def p_asignacion(p):
	'''asignacion : VARIABLE ASIG dato'''
	p[0] = p[1] + " " + p[2] + " " + p[3] + ";\n"
	
def p_aritmetica(p):
	'''aritmetica : VARIABLE ASIG PRI dato aritExtra PRD'''
	p[0] = p[1] + " " + p[2] + " " + p[3] + p[4] + " " + p[5] + p[6] + ";\n"
	
def p_condicional(p):
	'''condicional : if
					| while
					| for'''
	p[0] = p[1]
					
def p_aritExtra(p):
	'''aritExtra : aritExtra operador dato 
				  | empty'''
	if p[1] is None:
		p[0] = ""
	else:
		p[0] = p[1] + " " + p[2] + " " + p[3]
				  
def p_operador(p):
	'''operador : SUMA
				   | RESTA
				   | MULT
				   | DIV''' 
	p[0] = p[1]
				   
def p_if(p):
	'''if : SI requisito ENTONCES PRI instruccion PRD'''
	#p[0] = p[1] + " " + p[2] + " " + p[3] + p[4] + p[5] + p[6]
	p[0] = "if(" + p[2] + "){\n" + p[5] + "\n}\n" 
	 
def p_requisito(p):
	'''requisito : VARIABLE condicion posibilidad'''
	p[0] = p[1] + " " + p[2] + " " + p[3]
	
def p_posibilidad(p):
	'''posibilidad : dato
					| VERDAD
					| MENTIRA'''
	p[0] = p[1]
					
def p_condicion(p):
	'''condicion : MAYQ
				  | MENQ
				  | IGUAL
				  | MAYIGUAL
				  | MENIGUAL
				  | DIFERENTE'''
	p[0] = p[1]
				  
def p_for(p):
	'''for : DAR dato VUELTAS PRI instruccion PRD'''
	#p[0] = p[1] + " " + p[2] + " " + p[3] + p[4] + p[5] + p[6]
	p[0] = "for( int i=1; i <=" + p[2] + "; i++){\n" + p[5] + "\n}"
	
def p_while(p):
	'''while : HAGA PRI instruccion PRD MIENTRAS requisito'''
	# p[0] = p[1] + " " + p[2] + p[3] + p[4] + " " + p[5] + " " + p[6]
	p[0] = "do{\n" + p[3] + "\n} while (" + p[6] + ");\n"
			
def p_dato(p):
	'''dato : LETRA
			 | NUM
			 | VARIABLE'''
	p[0] = p[1]

def p_error(p):
	print ("ERROR FATAL")

def p_empty(p): 
	'empty :'
	pass

# Build the parser
parser = yacc.yacc()

# PARSEAR EL ARCHIVO

text = ""

for line in file('myfirstpotty.pty'):
	text += line.replace("\n","")


result = parser.parse(text)
f = open('out.cpp', 'w')
f.write(result)
f.close()
print(result)
				  