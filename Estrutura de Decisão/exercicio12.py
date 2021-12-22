# -*- coding: utf-8 -*-
"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário 
bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao 
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00"""
valor = float(input("Digite o valor da hora: R$"))
horas = int(input("Informe a quantidade de horas trabalhadas no mês: "))
salariobruto = valor*horas
sindicato = salariobruto*0.03
fgts = salariobruto*0.11
if salariobruto <= 900:
	print("Salario bruto de: R${:.2f}".format(salariobruto))
	print("IR isento")
	print("INSS(3%): R${:.2f}".format(sindicato))
	print("FGTS(11%): R${:.2f}".format(fgts))
	print("Total de descontos: R${:.2f}".format(sindicato))
	salarioliquido = salariobruto-sindicato
	print("Salario liquido: R${:.2f}".format(salarioliquido))
elif salariobruto>900 and salariobruto<=1500:
	print("Salario bruto de: R${:.2f}".format(salariobruto))
	ir = salariobruto*0.05
	print("IR(5%): R${:.2f}".format(ir))
	print("INSS(3%): R${:.2f}".format(sindicato))
	print("FGTS(11%): R${:.2f}".format(fgts))
	desconto = sindicato+ir
	print("Total de descontos: R${:.2f}".format(desconto))
	salarioliquido = salariobruto-desconto
	print("Salario liquido de: R${:.2f}".format(salarioliquido))
elif salariobruto>1500 and salariobruto<=2500:
	print("Salario bruto de: R${:.2f}".format(salariobruto))
	ir = salariobruto*0.10
	print("IR(10%): R${:.2f}".format(ir))
	print("INSS(3%): R${:.2f}".format(sindicato))
	print("FGTS(11%): R${:.2f}".format(fgts))
	desconto = sindicato+ir
	print("Total de descontos: R${:.2f}".format(desconto))
	salarioliquido = salariobruto-desconto
	print("Salario liquido de: R${:.2f}".format(salarioliquido))
else:
	print("Salario bruto de: R${:.2f}".format(salariobruto))
	ir = salariobruto*0.20
	print("IR(20%): R${:.2f}".format(ir))
	print("INSS(3%): R${:.2f}".format(sindicato))
	print("FGTS(11%): R${:.2f}".format(fgts))
	desconto = sindicato+ir
	print("Total de descontos: R${:.2f}".format(desconto))
	salarioliquido = salariobruto-desconto
	print("Salario liquido de: R${:.2f}".format(salarioliquido))