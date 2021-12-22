# -*- coding: utf-8 -*-
"""Faça um Programa que pergunte quanto você ganha 
por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês."""
ganho = float(input("Informe quanto ganha por hora: R$"))
horas = int(input("Informe o numero de horas trabalhadas no mes: "))
total = ganho * horas
print("Salario total: R${:.2f}".format(total))