# -*- coding: utf-8 -*-
"""Faça um Programa que peça 2 números inteiros e um número
real. Calcule e mostre:
a) o produto do dobro do primeiro com metade do segundo .
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo."""
n1 = int(input("Informe um numero inteiro: "))
n2 = int(input("Informe outro numero inteiro: "))
n3 = float(input("Agora informe um numero real: "))
produto = (n1*2)*(n2/2)
soma = (n1*3)+n3
cubo = n3**3
print("O produto é: {}".format(produto))
print("A soma é: {}".format(soma))
print("O terceiro elevado ao cubo é: {}".format(cubo))