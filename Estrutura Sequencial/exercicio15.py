# -*- coding: utf-8 -*-
"""Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre 
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) o salário líquido.
e) calcule os descontos e o salário líquido, conforme 
a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""
salario = float(input("Informe quanto ganha por hora: "))
horas = float(input("Informe o numero de horas trabalhadas no mes: "))
bruto = salario * horas
inss = (bruto*8)/100
ir = (bruto*11)/100
sindicato = (bruto*5)/100
liquido = bruto - inss - ir - sindicato
print("Salario bruto: R${:.2f}".format(bruto))
print("8% de desconto do inss: R${:.2f}".format(inss))
print("5% de desconto do sindicato: R${:.2f}".format(sindicato))
print("11% do imposto de renda: R${:.2f}".format(ir))
print("Salario liquido: R${:.2f}".format(liquido))
