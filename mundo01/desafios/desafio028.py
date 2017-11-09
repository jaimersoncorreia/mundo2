from random import randint
from time import sleep
'''
    Exercício Python 028: Escreva um programa que faça o 
    computador "pensar" em um número inteiro entre 0 e 5 
    e peça para o usuário tentar descobrir qual foi o 
    número escolhido pelo computador. O programa deverá 
    escrever na tela se o usuário venceu ou perdeu.
'''
print('\033[0;33m-=-'*20)
print('\033[0;36mVou pensar em um número entre 0 e 5. Tente advinhar...')
print('\033[0;33m-=-'*20)

jogador = int(input('\033[0;36mInforme o número pensado? '))

print('\033[0;35mPROCESSANDO...')
sleep(2)
computador = randint(0, 5)

if jogador == computador:
    print('\033[0;34mParabéns, você GANHOU! Advinhou meu pensamento')
else:
    print('\033[0;31mGANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))



