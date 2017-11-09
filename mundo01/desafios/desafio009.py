r = 12 * '='
print(r,' DESAFIO 009 ', r)

#ENTRADA DE DADOS
n = int(input('Digite um número para ver sua tabuada: '))

#PROCESSAMENTO DOS DADOS
tabuada  = '\n{:2} x {:2} = {:2}'.format(n, 1, n*1)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 2, n*2)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 3, n*3)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 4, n*4)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 5, n*5)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 6, n*6)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 7, n*7)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 8, n*8)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 9, n*9)
tabuada += '\n{:2} x {:2} = {:2}'.format(n, 10, n*10)


#SAÍDA DAS INFORMAÇÕES
print(tabuada)
