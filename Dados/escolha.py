import random
from time import sleep
while True:
    es = int(input('Escolha o numero de lados que o seu dado vai rodar:'))
    es_1 = input('Seu dado tem {} lados, deseja jogar ele?:'.format(es)).upper()
    resultado = (random.randrange(1, es))
    if es_1 == 'SIM':
        print('O Resultado do dado foi de {}'.format(resultado))
        print('Deseja reiniciar o programa ou sair?')
        es_3 = input(':').upper()
        if es_3 == 'SAIR':
            print('Encerrando o programa')
            sleep(1)
            break
        elif es_3 == 'REINICIAR':
            print('Reiniciando o programa')

    elif es_1 == 'NÃO' or es_1 == 'NAO':
        print('deseja escolaher outro valor ou sair?')
        es_2 = input(':').upper()
        if es_2 == 'OUTRO VALOR' or es_2 == '1':
            print('reiniciando o programa')
        
        elif es_2 == 'SAIR' or es_2 == '2':
            print('Encerrando o Programa')
            sleep(2)
            break

