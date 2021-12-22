# -*- coding: utf-8 -*-
"""Faça um Programa que verifique se uma letra digitada é 
"F" ou "M". Conforme a letra escrever: F - Feminino, 
M - Masculino, Sexo Inválido."""
sexo = input("Digite seu sexo: (F) para feminino ou (M) para masculino: ")
if sexo == 'f':
	print("Sexo feminino!!!")
elif sexo == 'm':
	print("Sexo masculino!!!")
else:
	print("Sexo invalido!!!")
