# -*- coding: utf-8 -*-
"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
a) salários até R$ 280,00 (incluindo) : aumento de 20%
b) salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
c) salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
d) salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
e) o salário antes do reajuste;
f) o percentual de aumento aplicado;
g) o valor do aumento;
h) o novo salário, após o aumento."""
salario = float(input("Digite o salario do colaborador: R$"))
if salario <= 280:
	aumento = salario*0.20
	print("Salario atual de R${:.2f}".format(salario))
	print("Receberá aumento de R${:.2f}".format(aumento))
	salario+=aumento
	print("Salario de R${:.2f} com aumento de 20%".format(salario))
elif salario >280 and salario<=700:
	aumento = salario * 0.15
	print("Salario atual de R${:.2f}".format(salario))
	print("Receberá aumento de R${:.2f}".format(aumento))
	salario+=aumento
	print("Salario de R${} com aumento de 15%".format(salario))
elif salario > 700 and salario<=1500:
	aumento = salario * 0.10
	print("Salario atual de R${:.2f}".format(salario))
	print("Receberá aumento de R${:.2f}".format(aumento))
	salario+=aumento
	print("Salario de R${:.2f} com aumento de 10%".format(salario))
else:
	aumento = salario * 0.05
	print("Salario atual de R${}".format(salario))
	print("Receberá aumento de R${}".format(aumento))
	salario+=aumento
	print("Salario de R${} com aumento de 5%".format(salario))