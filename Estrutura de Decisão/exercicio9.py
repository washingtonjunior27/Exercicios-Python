# -*- coding: utf-8 -*-
"""Faça um Programa que leia três números e mostre-os
em ordem decrescente."""
lista = []
for n in range(3):
	n = int(input(f"Digite o {n+1}º valor: "))
	lista.append(n)

lista.sort(reverse=True)
print(lista)