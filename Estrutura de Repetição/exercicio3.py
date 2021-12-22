# -*- coding: utf-8 -*-
"""Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';"""
nome = str(input("Digite um nome maior que 3 caracteres: "))
while len(nome)<=3:
	print("Nome muito pequeno!!")
	nome = str(input("Digite um nome maior que 3 caracteres: "))

idade = int(input("Informe uma idade entre 0 e 150: "))
while (idade<0) or (idade>150):
	print("Idade invalida!!")
	idade = int(input("Informe uma idade entre 0 e 150: "))

salario = float(input("Informe um salario maior que 0: R$"))
while salario<=0:
	print("Salario invalido!!")
	salario = float(input("Informe um salario maior que 0: R$"))

sexo = str(input("Informe o sexo: (f)feminino ou (m)masculino: ")).lower()
while sexo!="f" and sexo!="m":
	print("Sexo invalido!!")
	sexo = str(input("Informe o sexo: (f)feminino ou (m)masculino: ")).lower()

estadocivil = str(input("Informe o estado civil: (s)solteiro, (c)casado, (v)viuvo ou (d)divorciado: ")).lower()
while estadocivil!="s" and estadocivil!="c" and estadocivil!="v" and estadocivil!="d":
	print("Estado civil invalido!!")
	estadocivil = str(input("Informe o estado civil: (s)solteiro, (c)casado, (v)viuvo ou (d)divorciado: ")).lower()

print("Nome: {}\nIdade: {}\nSalario: R${}\nSexo: {}\nEstado Civil: {}".format(nome, idade, salario, sexo, estadocivil))