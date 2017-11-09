'''
    Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, 
    mostrando em seguida o primeiro e o último nome separadamente.
'''

nomecompleto = str(input('Informe o nome completo: '))

nomefatiado = nomecompleto.split()



print('Primeiro Nome: {}'.format(nomefatiado[0]))

print('Último Nome: {}'.format(nomefatiado[len(nomefatiado)-1]))