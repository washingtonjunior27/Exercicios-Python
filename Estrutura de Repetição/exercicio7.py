# -*- coding: utf-8 -*-
"""Faça um programa que leia 5 números e informe o maior número."""
lista = []
for i in range(5):
	lista.append(int(input("Numero: ")))

print(max(lista))