'''
    Exercício Python 012: Faça um algoritmo que leia o preço 
    de um produto e mostre seu novo preço, com 5% de desconto.
'''
r = '=' * 12
print(r, ' DESAFIO 012', r)

#ENTRADA DOS DADOS
preco = float(input('Informe o preço de um produto: '))

#PROCESSAMENTO DOS DADOS
preco *= 0.95

#SAÍDA DAS INFORMAÇÕES
print('O novo preço é R${:.2f}'.format(preco))