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
	'Y' : 'Y'
	'O' : 'O'

}

tokens = ['SUMA', 'RESTA', 'DIV', 'MULT', 'PRI', 'PRD', 'LI', 'LD', 'ASIG', 'MAYQ', 'MENQ', 'IGUAL', 'MAYIGUAL', 'MENIGUAL', 'DIFERENTE', 'VARIABLE', 'NUM', 'LETRA', 'FINDELINEA', 'ID'] + list(reservadas.values())

<<<<<<< HEAD
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PRI = r'\('
t_PRD = r'\)'
t_LI = r'{'
t_LD = r'}'
t_ASIG = r'='
t_MAYQ = r'>'
t_MENQ = r'<'
t_MAYIGUAL = r'>='
t_MENIGUAL = r'<='
t_IGUAL= r'=='
t_DIFERENTE = r'!='
t_VARIABLE = r'([a-z]+[A-Z]*[0-9]*)+'
=======
t_+ = r'\+'
t_- = r'-'
t_* = r'\*'
t_/ = r'/'
t_( = r'\('
t_) = r'\)'
t_{ = r'{'
t_} = r'}'
t_es = r'='
t_mayor_que = r'>'
t_menor_que = r'<'
t_mayor_igual = r'>='
t_menor_igual = r'<='
t_igual_a = r'=='
t_diferente_a = r'!='
t_variable = r'([a-z]+[A-Z]*[0-9]*)+'
t_letra = r'[a-zA-Z]'
>>>>>>> origin/master
	
def t_NUM(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t
	
def t_FINDELINEA(t):
    r'(\n)+'
    t.lexer.lineno += t.value.count("\n")
    return t

<<<<<<< HEAD
#función que determina el número de línea 
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
=======
def t_IDENTIFICADOR(t):
>>>>>>> origin/master
    r'[A-Z][A-Z0-9]*'
    t.type = reservadas.get(t.value, 'ID')    # Check for reserved words
    return t
<<<<<<< HEAD
	
def t_error(t):
    print 'Caracter ilegal'
    t.lexer.skip(1)
	
t_ignore = " \t"

lexer = ply.lex.lex()
lexer.input("JUGAR SI 6 > 7")
while True:
    tok = lexer.token()
    if not tok:
        break
    print tok
=======

t_ignore = " \t"	
>>>>>>> origin/master
