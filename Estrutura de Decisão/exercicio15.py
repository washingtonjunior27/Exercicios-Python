# -*- coding: utf-8 -*-
"""Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;"""
lado1 = float(input("Digite o 1º lado do triangulo: "))
lado2 = float(input("Digite o 2º lado do triângulo: "))
lado3 = float(input("Digite o 3º lado do triângulo: "))
if lado1+lado2>lado3 and lado1+lado3>lado2 and lado2+lado3>lado1:
	print("Os valores formam um triângulo!!!")
	if lado1==lado2 and lado1==lado3:
		print("Triângulo Equilátero!!!")
	elif lado1==lado2 or lado1==lado3 or lado2==lado3:
		print("Triângulo Isósceles!!!")
	else:
		print("Triângulo Escaleno!!!")
else:
	print("Não formam um triângulo!!!")