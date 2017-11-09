r = 12
print('=' * r, 'DESAFIO 04', '=' * r)
algo = input('Digite algo: ')

print('\nTipo:{}\nÉ espaco:{}\nÉ número:{}\nÉ alfabético:{}\nÉ Alfanumérico:{}\nEstá em maúsculas:{}\nEstá em minúsculas:{}\nEstá capitalizada:{}'
      ''.format(type(algo), algo.isspace(), algo.isnumeric(), algo.isalpha(), algo.isalnum(), algo.isupper(),algo.islower(),algo.istitle()))