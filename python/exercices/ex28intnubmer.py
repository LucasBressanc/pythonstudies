#Faça o algoritmo pensar em um número e fazer você adivinhar, falando se acertou ou erro.

from random import randint 

n = randint(0,5)
palpite = int(input('Estou pensando em um número de 0 a 5. Será que consegue acertar?\n\nPalpite: '))

if palpite == n:
    print('Parabéns! Você acertou!')
else: print('Infelizmente você errou...\nO número era {}!' .format(n))