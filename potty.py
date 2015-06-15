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

tokens = ['+', '-', '/'. '*', '(', ')', '{', '}', 'es', 'mayorque', 'menorque', 'iguala',  ]

#probando commit desde VS code

#commit julio