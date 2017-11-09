'''
    Exercício Python 022: 
    Crie um programa que leia o nome completo de uma pessoa e mostre: 
    - O nome com todas as letras maiúsculas e minúsculas. 
    - Quantas letras ao todo (sem considerar espaços). 
    - Quantas letras tem o primeiro nome.

'''

nomecompleto = str(input('Informe o nome completo '))

print('Analisando o seu nome ...')
print('Seu nome em maiúsculo é {}'.format(nomecompleto.upper()))
print('Seu nome em minúsculo é {}'.format(nomecompleto.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nomecompleto.replace(' ',''))))

print('Seu primeiro nome é {} e ele tem {} letras'.format(nomecompleto.split(' ', 1)[0],len(nomecompleto.split(' ', 1)[0])))

