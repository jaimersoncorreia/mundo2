'''
    Exercício Python 024: 
    Crie um programa que leia o nome de uma cidade 
    diga se ela começa ou não com o nome "SANTO".
'''
cidade = str(input('Em que cidade você nasceu? ')).strip()

primeironome = cidade.split()[0].upper()


print(primeironome.startswith('SANTO'))