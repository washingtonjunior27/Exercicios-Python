#Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))
sinal = input("Informe o sinal: +, -, *, /: ")
if sinal == "+":
	num = n1+n2
elif sinal == "-":
	num = n1-n2
elif sinal == "*":
	num = n1*n2
elif sinal == "/":
	num = n1/n2
else:
	print("Sinal invalido!!")

print(f"Operacao foi {num}")