# -*- coding: utf-8 -*-
"""Altere o programa anterior para mostrar no final a soma dos números."""
soma = 0
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
for i in range(n1+1, n2):
	print(i, end=" ")
	soma=soma+i

print("\nA soma é: {}".format(soma))