'''
    Exercício Python 030: Crie um programa que leia um número 
    inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

numero = int(input('Informe um número inteiro: '))

resultado = '\033[34mPAR\033[m' if numero % 2 == 0 else '\033[31mÍMPAR\033[m'
print('O número {} é {}'.format(numero, resultado))
