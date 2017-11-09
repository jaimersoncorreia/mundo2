'''
    Exercício Python 026: Faça um programa que leia uma frase pelo teclado e 
    mostre quantas vezes aparece a letra "A", 
    em que posição ela aparece a primeira vez
    e em que posição ela aparece a última vez.
'''

frase = str(input('Digite um frase: ')).strip().upper()

print('Quantidades de A é {}'.format(frase.count('A')))
print('Primeira ocorrência foi na posição {} '.format(frase.find('A') + 1))
print('Última ocorrência foi na posição {} '.format(frase.rfind('A') + 1))
