#-*- coding=utf-8 -*-
"""Faça um Programa que calcule a área de um quadrado, 
em seguida mostre o dobro desta área para o usuário."""
base = float(input("Informe o tamanho do lado do quadrado: "))
area = base**2
dobro = area*2
print(f"Base: {base}")
print("Area: {}".format(area))
print("Dobro da area: {}".format(dobro))