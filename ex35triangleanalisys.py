print('-='*20)
print('ANALISADOR DE TRIÂNGULOS')
print('-='*20)

l1 = float(input('Digite o comprimento da primeira reta: '))
l2 = float(input('Digite o comprimento da segunda reta: '))
l3 = float(input('Digite o comprimento da terceira reta: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('Essas retas são capazes de formar um triângulo!')
else:
    print('Não é possível desenhar um triângulo com essas medidas.')