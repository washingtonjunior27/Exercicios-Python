# -*- coding: utf-8 -*-
"""Faça um programa que leia 5 números e informe a soma e a média dos números."""
soma = 0
for i in range(5):
	num = int(input("Informe um numero: "))
	soma+=num
	media = soma/5

print("Soma: {}\nMedia: {}".format(soma, media))
