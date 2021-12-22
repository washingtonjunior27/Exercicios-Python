#-*- coding: utf-8 -*-
"""Faça um Programa que peça o raio de um círculo, 
calcule e mostre sua área.
Formula area = pi * raio ao quadrado"""
raio = float(input("Digite o raio do círculo: "))
area = 3.14 * (raio**2)
print("A área do circulo é: {}".format(area))

"""biblioteca {import math} e comando {math.pi} 
podem ser usadas"""