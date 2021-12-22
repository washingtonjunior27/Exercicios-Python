# -*- coding: utf-8 -*-
"""Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar, sabendo que a 
decisão é sempre pelo mais barato."""
p1 = float(input("Digite o preço do primeiro produto: R$"))
p2 = float(input("Digite o preço do segundo produto: R$"))
p3 = float(input("Digite o preço do terceiro produto: R$"))

if p1<p2 and p1<p3:
	print("Produto mais barato é o de R${:.2f}".format(p1))
elif p2<p1 and p2<p3:
	print("Produto mais barato é o de R${:.2f}".format(p2))
elif p3<p1 and p3<p2:
	print("Produto mais barato é o de R${:.2f}".format(p3))
else:
	print("Produtos mais baratos com preços iguais!!")