'''
    Exercício Python 011: Faça um programa que leia a largura e a altura
    de uma parede em metros, calcule a sua área e a quantidade de tinta 
    necessária para pintá-la, sabendo que cada litro de tinta pinta uma 
    área de 2 metros quadrados.
'''
r = '=' * 12
print(r,' DESAFIO 011 ',r)

#ENTRADA DOS DADOS
largura = float(input('Qual a largura da casa: '))
altura = float(input('Qual a altura da casa: '))

#PROCESSAMENTO DOS DADOS
area = largura * altura
tinta = area / 2

print('Serão necessários {}l de tinta para pinta {}m²'.format(tinta, area))