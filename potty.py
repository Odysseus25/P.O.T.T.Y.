import ply.lex as lex 
import ply.yacc as yacc

reservadas = {
	'jugar' : 'jugar'
	'dormir' : 'dormir'
	'dar' : 'dar'
	'vueltas' : 'vueltas'
	'si' : 'si'
	'entonces' : 'entonces'
	'haga' : 'haga'
	'mientras' : 'mientras'
	'escribir' : 'escrbir'
	'verdad' : 'verdad'
	'mentira' : 'mentira'
	'y' : 'y'
	'o' : 'o'
		
}

tokens = ['+', '-', '/'. '*', '(', ')', '{', '}', 'es', 'mayor_que', 'menor_que', 'igual_a', 'mayor_igual', 'menor_igual', 'no_igual', 'cadena', 'numero', 'letra'] + list(reservadas.values())

t_+ = r'\+'
t_- = r'-'
t_* = r'\*'
t_/ = r'/'
t_( = r'\('
t_) = r')'
t_{ = r'{'
t_} = r'}'
t_es = r'='
t_mayor_que = r'>'
t_menor_que = r'<'
t_mayor_igual = r'>='
t_menor_igual = r'<='
t_igual_a = r'=='
t_no_igual : r'!='
t_cadena 