# -*- coding: utf-8 -*-
"""Faça um Programa que leia três números e mostre o maior
 deles."""
n1 = int(input("Digite o 1 numero: "))
n2 = int(input("Digite o 2 numero: "))
n3 = int(input("Digite o 3 numero: "))
if n1>n2 and n1>n3:
 	print("O maior numero é: {}".format(n1))
elif n2>n1 and n2>n3:
 	print("O maior numero é: {}".format(n2))
elif n3>n1 and n3>n2:
 	print("O maior numero é: {}".format(n3))
else:
	print("Numeros iguais!!")