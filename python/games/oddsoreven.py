#crie um algoritmo que jogue par ou impar

import random

compnumb = random.randint(1, 5)
choice = int(input('\nSe quiser par, digite 0\n'
                   'Se quiser impar, digite 1\n\n'
                   'PAR OU IMPAR?! '))

if choice == 0:
    print('Você escolheu PAR!\n')
    n = int(input('Digite o seu número, de 1 a 5: '))
    sum = int(n + compnumb)
    resto = sum % 2
    if resto == 0: print('\nMeu número é {}. Você ganhou!' .format(compnumb))
    else: print('\nMeu número é {}. Você perdeu!' .format(compnumb))

if choice == 1:
    print('Você escolher ÍMPAR!\n')
    n = int(input('Digite o seu número, de 1 a 5: '))
    sum = int(n + compnumb)
    resto = sum % 2
    if resto == 0: print('\nMeu número é {}. Você perdeu!' .format(compnumb))
    else: print('\n1Meu número é {}. Você ganhou!' .format(compnumb))
