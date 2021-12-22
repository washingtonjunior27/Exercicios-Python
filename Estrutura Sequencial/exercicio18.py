#-*- coding: utf-8 -*-
"""Faça um programa que peça o tamanho de um arquivo para
 download (em MB) e a velocidade de um link de Internet 
 (em Mbps), calcule e informe o tempo aproximado de 
 download do arquivo usando este link (em minutos)."""
 
arquivo = float(input("Informe o tamanho do arquivo para donwload (em MB): "))
velocidade = float(input("Informe a velocidade de sua internet (em MBPS): "))
tempo = arquivo / velocidade
minuto = tempo / 60.0
print("O tempo de download do arquivo usando este link é de: {:.2f} minutos".format(minuto))
