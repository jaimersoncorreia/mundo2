'''
    Exercício Python 025: Crie um programa que leia 
    o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Informe seu nome completo? ')).upper().strip()
'''
pos = int(nome.find('SILVA'))
subnome = nome[pos:(pos + len('SILVA'))]

print('Seu nome tem Silva? {}'.format(subnome.startswith('SILVA')))
'''
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))