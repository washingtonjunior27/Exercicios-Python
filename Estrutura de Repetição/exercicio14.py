"""Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares."""
soma = 0
par = 0
impar = 0
for i in range(10):
	n = int(input(f'Digite o {i+1}º numero: '))
	soma+=n
	if n%2==0:
		par+=1
	else:
		impar+=1

print(f'A soma dos numeros é: {soma}')
print(f'Quantidade de numeros pares: {par}')
print(f'Quantidade de numeros impares: {impar}')