"""1 - Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade."""
idade = int(input("Informe a idade: "))
if idade>=18:
	print("Usuario de {} anos maior de idade!!".format(idade))
else:
	print(f"Usuario de {idade} anos menor de idade!!")
