# -*- coding: utf-8 -*-
"""Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação."""
anos = 0

a = int(input("Digite a população de A: "))
while a<0:
	a = int(input("Digite a população de A: "))

b = int(input("Digite a população de B: "))
while b<0:
	b = int(input("Digite a população de B: "))

taxaA = float(input("Informe a taxa de crescimento de A: "))
while taxaA<0:
	taxaA = float(input("Informe a taxa de crescimento de A: "))

taxaB = float(input("Informe a taxa de crescimento de B: "))
while taxaB<0:
	taxaB = float(input("Informe a taxa de crescimento de B: "))

while a<=b:
		anos+=1
		a = a+(a*taxaA)
		b = b+(b*taxaB)

print("Levarão {} anos para A ultrapassar B".format(anos))