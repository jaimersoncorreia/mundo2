r = 12 * '='
print(r,' DESAFIO 010 ',r)

#ENTRADA DOS DADOS
real = float(input('Quantos reais você tem na carteira? '))

#PROCESSAMENTO DOS DADOS (1U$$ = R$3.27)
dolar = real/3.27

#SAÍDA DAS INFORMAÇÕES

print('Com esses R${} você pode comprar U$${}'.format(real,dolar))
