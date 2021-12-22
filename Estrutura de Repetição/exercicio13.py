"""Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem."""
calculo = 1
n1 = int(input("Digite a base: "))
n2 = int(input("Digite o expoente: "))
for i in range(n2):
	calculo = calculo*n1
	
print(f'Calculo = {calculo}')