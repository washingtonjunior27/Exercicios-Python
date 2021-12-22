# -*- coding: utf-8 -*-
"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações."""
login = input("Digite um nome de usuario: ")
senha = input("Digite uma senha diferente do nome de usuario: ")
while senha==login:
	print("Senha invalida!!")
	login = input("Digite um nome de usuario: ")
	senha = input("Digite uma senha diferente do nome de usuario: ")

print("Seu login é: {}".format(login))
print("Sua senha é: {}".format(senha))