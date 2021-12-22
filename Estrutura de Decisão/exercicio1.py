# -*- coding: utf-8 -*-
"""Faça um Programa que peça dois números e imprima 
o maior deles."""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
if n1>n2:
	print("O maior numero é: {}".format(n1))
elif n2>n1:
	print("O maior numero é: {}".format(n2))
elif n1==n2:
	print("Numeros iguais!!!")
