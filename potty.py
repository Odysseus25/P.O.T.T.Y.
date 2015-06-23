import ply.lex as lex 
import ply.yacc as yacc

reservadas = {
	'JUGAR' : 'JUGAR'
	'DORMIR' : 'DORMIR'
	'DAR' : 'DAR'
	'VUELTAS' : 'VUELTAS'
	'SI' : 'SI'
	'ENTONCES' : 'ENTONCES'
	'HAGA' : 'HAGA'
	'MIENTRAS' : 'MIENTRAS'
	'ESCRIBIR' : 'ESCRIBIR'
	'VERDAD' : 'VERDAD'
	'MENTIRA' : 'MENTIRA'

}

tokens = ['SUMA', 'RESTA', 'DIV', 'MULT', 'PRI', 'PRD', 'ASIG', 'MAYQ', 'MENQ', 'IGUAL', 'MAYIGUAL', 'MENIGUAL', 'DIFERENTE', 'VARIABLE', 'NUM', 'LETRA', 'FINDELINEA', 'ID'] + list(reservadas.values())

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PRI = r'\('
t_PRD = r'\)'
#t_LI = r'{'
#t_LD = r'}'
t_ASIG = r'='
t_MAYQ = r'>'
t_MENQ = r'<'
t_MAYIGUAL = r'>='
t_MENIGUAL = r'<='
t_IGUAL= r'=='
t_DIFERENTE = r'!='
t_VARIABLE = r'([a-z]+[A-Z]*[0-9]*)+'
t_letra = r'[a-zA-Z]'
	
def t_NUM(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t
	
def t_FINDELINEA(t):
    r'(\n)+'
    t.lexer.lineno += t.value.count("\n")
    return t

#función que determina el número de línea 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    t.type = reservadas.get(t.value, 'ID')    # Check for reserved words
    return t
	
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0] + " en la linea " + str(t.lexer.lineno))
    t.lexer.skip(1)

lexer = ply.lex.lex()
#lexer.input("JUGAR SI 6 > 7")

while True:
    tok = lexer.token()
    if not tok:
        break
    print tok

t_ignore = " \t"	

##### PARSER

def p_programa(p):
	'programa : JUGAR instruccion DORMIR eof'
	
def p_eof(p):
	'''eof : '''
	
def p_instruccion(p):
	'''instruccion : instruccion asignacion
					| instruccion aritmetica
					| instruccion condicional
					| instruccion ESCRIBIR
					| '''

def p_asignacion(p):
	'''asignacion : variable es dato'''
	
def p_aritmetica(p):
	'''aritmetica : variable es PRI dato aritExtra PRD'''
	
def p_condicional(p):
	'''condicional : if
					| while
					| for'''
					
def p_aritExtra(p):
	'''aritExtra : operador variable aritExtra 
				  | operador num aritExtra
				  | '''
				  
def p_operador(p):
	'''p_operador : SUMA
				   | RESTA
				   | MULT
				   | DIV'''
				   
def p_if(p):
	'''p_if : si requisito entonces PRI instruccion PDR'''
	
def p_requisito(p):
	'''requisito : variable condicion posibilidad'''
	
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
	'''for : DAR num VUELTAS PRI instruccion PRD'''
	
def p_while(p):
	'''while : HAGA PRI instruccion PRD MIENTRAS requisito'''
				  
				  