'''
    Exercício Python 035: Desenvolva um programa que leia o 
    comprimento de três retas e diga ao usuário se elas 
    podem ou não formar um triângulo.
'''
print('\033[33m-=-'*20)
print('\033[35mAnalisador de Triângulos')
print('\033[33m-=-'*20)

a = float(input('\033[mPrimeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima \033[34mPODEM FORMAR\033[m um triângulo')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m triângulo')