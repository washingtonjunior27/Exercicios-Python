# -*- coding: utf-8 -*-
"""Tendo como dado de entrada a altura (h) de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""
h = float(input("Informe a altura da pessoa: "))
sexo = input("Informe o sexo da pessoa: ")
pesoidealm = (72.7*h) - 58
pesoidealf = (62.1*h) - 44.7
if sexo == "m" or sexo == "masculino":
	print("Seu peso ideal é: {:.2f}kg".format(pesoidealm))
elif sexo == "f" or sexo == "feminino":
	print("Seu peso ideal é: {:.2f}kg".format(pesoidealf))
else:
	print("Sexo invalido!!!")
