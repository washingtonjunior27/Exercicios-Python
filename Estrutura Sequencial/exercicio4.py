# -*- coding: utf-8 -*-
"""Faça um Programa que peça as 4 notas bimestrais 
e mostre a média."""
n1 = float(input("n1: "))
n2 = float(input("n2: "))
n3 = float(input("n3: "))
n4 = float(input("n4: "))
media = (n1+n2+n3+n4)/4
print(f"A media é: {media}")
print("n1 {}, n2 {}, n3 {}, n4 {}, media {}".format(n1,n2,n3,n4,media))