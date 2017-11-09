'''
    Exercício Python 014: Escreva um programa que converta 
    uma temperatura digitando em graus Celsius e converta 
    para graus Fahrenheit.
'''
c = int(input('Temperatura em grau Celcius? '))
f = (9 / 5) * c + 32

print('{}ºC equivale a {}ºF'.format(c,f))