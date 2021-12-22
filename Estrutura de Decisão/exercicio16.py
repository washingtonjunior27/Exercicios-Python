# -*- coding: utf-8 -*-
"""Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de 
a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores,
sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""
a = float(input("Informe o 1º valor: "))
if a==0:
	print("Equação não é de segundo grau!!")
	exit()

b = float(input("Informe o 2º valor: "))
c = float(input("Informe o 3º valor: "))
delta = b**2 - 4*a*c
if delta<0:
	print("Resultado de delta: {}".format(delta))
	print("Equação não possui raizes reais!!")
	exit()
elif delta==0:
	print("Resultado de delta: {}".format(delta))
	x1 = (-b + delta**0.5)/(2*a)
	print("Equação possui apenas uma raiz real!! {}".format(x1))
else:
	print("Resultado de delta: {}".format(delta))
	x1 = (-b + delta**0.5)/2*a
	x2 = (-b - delta**0.5)/2*a
	print("Equação possui duas raizes reais!! {}, {}".format(x1,x2))