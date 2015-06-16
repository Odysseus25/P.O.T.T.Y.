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

tokens = ['+', '-', '/', '*', '(', ')', '{', '}', 'es', 'mayor_que', 'menor_que', 'igual_a', 'mayor_igual', 'menor_igual', 'diferente_a', 'variable', 'numero', 'letra', 'FINDELINEA', 'IDENTIFICADOR'] + list(reservadas.values())

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
	
def t_numero(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t
	
def t_FINDELINEA(t):
    r'(\n)+'
    t.lexer.lineno += t.value.count("\n")
    return t

def t_IDENTIFICADOR(t):
    r'[A-Z][A-Z0-9]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')    # Check for reserved words
    return t

t_ignore = " \t"	