'''
    Exercício Python 018: Faça um programa que leia um ângulo 
    qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
from math import cos, pi, sin, tan, radians
angulo = float(input('Informe o angulo :'))

seno = sin(angulo * pi / 180)
cosseno = cos(radians(angulo))
tangente = tan(angulo * pi / 180)

print('O seno de {} é {:.3f}'.format(angulo, seno))
print('O cosseno de {} é {:.3f}'.format(angulo, cosseno))
print('O tangante de {} é {:.3f}'.format(angulo, tangente))
