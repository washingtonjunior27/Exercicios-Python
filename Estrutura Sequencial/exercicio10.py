# -*- coding: utf-8 -*-
"""Faça um Programa que peça a temperatura em graus 
Celsius, transforme e mostre em graus Fahrenheit."""
c = float(input("Informe a temperatura em Celsius: "))
fh = c * (9/5)+32
print("Em fahrenheit fica: {}".format(fh))