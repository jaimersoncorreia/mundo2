#nome = str(input('Qual é o seu nome? '))
nome = 'Jaimerson'

if nome == 'Jaimerson':
    print('Que nome lindo você tem! ')
else:
    print('Seu nome é tão normal!')

print('Bom dia, {}! '.format(nome))

nota01 = float(input('Informe a primeira nota: '))
nota02 = float(input('Informe a segunda nota: '))

media = (nota02 + nota01)/2

print('A sua média foi {:.1f}'.format(media))

if media >= 6.0:
    print('Sua média foi boa! PARABENS')
else:
    print('A sua média foi ruim ! ESTUDE MAIS!')

#OUTRA MANEIRA
print('PARABÉNS' if media >= 6 else 'ESTUDE MAIS')