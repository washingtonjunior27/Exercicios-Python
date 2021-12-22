# -*- coding: utf-8 -*-
"""Faça um programa que lê as duas notas parciais obtidas 
por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos 
obedece à tabela abaixo:

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, 
o conceito correspondente e a mensagem “APROVADO” 
se o conceito for A, B ou C ou “REPROVADO” se o 
conceito for D ou E."""
n1 = float(input("Digite a n1: "))
n2 = float(input("Digite a n2: "))
media = (n1+n2)/2
print("Nota 1: {}".format(n1))
print("Nota 2: {}".format(n2))
print("Media: {}".format(media))
if media>=9 and media<=10:
	print("Conceito: A")
	print("Parabéns!! Aprovado")
elif media>=7.5 and media<9:
	print("Conceito: B")
	print("Aprovado!!!")
elif media>=6 and media<7.5:
	print("Conceito: C")
	print("Passou na média!! Aprovado!!")
elif media>=4 and media<6:
	print("Conceito: D")
	print("Reprovado!!!")
else:
	print("Conceito: E")
	print("Reprovado!!")