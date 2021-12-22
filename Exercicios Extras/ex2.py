"""2 - Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, 
escreva aprovado, senão escreva reprovado.   """
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2)/2
if media>=6:
	print(f"Media: {media}")
	print("Aprovado")
else:
	print(f"Media: {media}")
	print("Reprovado")