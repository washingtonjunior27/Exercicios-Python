# -*- coding:utf-8 -*-
"""Faça um Programa que leia três números e mostre o
maior e o menor deles."""
n1 = int(input("Digite o 1º numero: "))
n2 = int(input("Digite o 2º numero: "))
n3 = int(input("Digite o 3º numero: "))

menor = n1
if n2<n1 and n2<n3:
	menor=n2
elif n3<n1 and n3<n2:
	menor=n3

maior = n1
if n2>n1 and n2>n3:
	maior = n2
elif n3>n1 and n3>n2:
	maior = n3
print("O maior numero foi: {}".format(maior))
print("O menor numero foi: {}".format(menor))
