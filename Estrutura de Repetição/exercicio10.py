# -*- coding: utf-8 -*-
"""Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles."""
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
for i in range(n1, n2+1):
	print(i, end=", ")