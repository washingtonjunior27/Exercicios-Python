"""A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo."""
anterior = 1
proximo = 1
soma = 1
for i in range(10):
	print(f'{anterior}')
	soma = anterior+proximo
	anterior = proximo
	proximo = soma
