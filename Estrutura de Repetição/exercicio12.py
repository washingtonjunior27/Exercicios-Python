"""Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:"""
n1 = int(input("Informe o numero que deseja ver a tabuada: "))
for i in range(0, 11):
	tabuada=n1*i
	print(f'{n1} X {i} = {tabuada}')