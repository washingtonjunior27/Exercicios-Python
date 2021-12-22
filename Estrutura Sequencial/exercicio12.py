# -*- coding: utf-8 -*-
"""Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58"""
altura = float(input("Digite a altura da pessoa: "))
peso = (72.7*altura) - 58
print("Seu peso ideal é: {:.2f}kg".format(peso))