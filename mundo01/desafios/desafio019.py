'''
    Exercício Python 019: Um professor quer sortear um dos seus quatro 
    alunos para apagar o quadro. Faça um programa que ajude ele, lendo 
    o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random
listadenomes = []
listadenomes.append(input('Primeiro nome: '))
listadenomes.append(input('Segundo nome: '))
listadenomes.append(input('Terceiro nome: '))
listadenomes.append(input('Quarto nome: '))


sorte01 = random.choice(listadenomes)

print('{}'.format(sorte01))