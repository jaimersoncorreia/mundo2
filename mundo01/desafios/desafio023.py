'''
    Exercício Python 023: Faça um programa que leia 
    um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

'''

numero = str(input('Informe um número: '))
'''
print('Unidade: {}'.format(lista[3]))
print('Dezena: {}'.format(lista[2]))
print('Centena: {}'.format(lista[1]))
print('Milhar: {}'.format(lista[0]))
'''
n = int(numero)
print(n)

unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10



print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))