#escreva um número e faça o algoritmo descrever se é par ou impar

n = int(input('Digite um número inteiro: '))
resultado = n % 2

if n == 0:
    print('INVÁLIDO!\nO número {} é zero!' .format(n))
elif n < 0:
    print('INVÁLIDO!\nO número {} é negativo!' .format(n))
elif resultado == 0:
    print('O número {} é par!' .format(n))
else:
    print('O número {} é impar!' .format(n))