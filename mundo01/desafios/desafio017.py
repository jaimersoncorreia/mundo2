'''
    Python – Exercício 017 – Catetos e Hipotenusa
    Exercício Python 017: Faça um programa que leia o comprimento do cateto 
    oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre 
    o comprimento da hipotenusa.
'''
from math import hypot

oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))

#hipotenusa = (oposto ** 2 + adjacente ** 2) ** (1 / 2)
hipotenusa = hypot(oposto, adjacente)

print('A hipotenusa é {:.3f}'.format(hipotenusa))