'''
    Exercício Python 029: Escreva um programa que leia a velocidade 
    de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem 
    dizendo que ele foi multado. A multa vai custar 
    R$7,00 por cada Km acima do limite.
'''

velocidade = float(input('Informe sua velocidade: '))

if velocidade > 80:
    print('\033[31mMULTADO! Você exerceu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de \033[33mR$ {:.2f}\033[m!!'.format((velocidade - 80) * 7.0))

print('\033[32mTenha um bom dia! Dirija com segurança!')
