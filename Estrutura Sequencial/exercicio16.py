# -*- coding:utf-8 -*-
"""Faça um programa para uma loja de tintas. O programa 
deverá pedir o tamanho em metros quadrados da área a ser 
pintada. Considere que a cobertura da tinta é de 1 litro 
para cada 3 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta 
a serem compradas e o preço total."""
tamanho = float(input("Informe o tamanho em metros quadrados da area: "))
litro = tamanho/3
latas = int(litro/18)
if(litro%18!=0):
	latas += 1
total = latas*80.00
print("Litros necessarios: {}".format(litro))
print("Quantidade de latas a serem compradas: {}".format(latas))
print("Total a pagar: R${}".format(total))
