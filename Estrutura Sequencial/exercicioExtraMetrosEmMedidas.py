# -*- coding: utf-8 -*-
"""Faça um Programa que converta metros para km, hm,
 dam, dm, cm, mm."""
medida = float(input("Digite um valor em metros a ser convertido: "))
km = medida/1000
hm = medida/100
dam = medida/10
dm = medida*10
cm = medida*100
mm = medida*1000
print(f"A conversão de {medida}m é: \nkm: {km}\nhm: {hm}\ndam: {dam}\ndm: {dm:.0f}\ncm: {cm:.0f}\nmm: {mm:.0f}")