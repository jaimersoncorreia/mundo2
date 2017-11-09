'''
    Exercício Python 034: Escreva um programa que pergunte 
    o salário de um funcionário e calcule o valor do seu 
    aumento. Para salários superiores a R$1250,00, calcule 
    um aumento de 10%. Para os inferiores ou iguais, 
    o aumento é de 15%.
'''

salario = float(input('Informe seu salário: '))

novo = (salario*1.1)if salario > 1250.0 else (salario*1.15)

print('Quem ganhava \033[31mR$ {:.2f}\033[m passa a ganhar \033[36mR$ {:.2f}\033[m'.format(salario, novo))
