# -*- coding: utf-8 -*-
"""Faça um Programa que peça a temperatura em graus 
Fahrenheit, transforme e mostre a temperatura em 
graus Celsius.
C = 5 * ((F-32) / 9)."""
fh = float(input("Informe a temperatura em Fahrenheit: "))
c = 5 * ((fh-32)/9)
print ("A temperatura em celcius é: {}".format(c))