#faça um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))

#verificar o menor
low = n1
if n2<n1 and n2<n3:
    low = n2
if n3<n1 and n3<n2:
    low = n3

print('O menor número é ', low)

#verificar o maior

high = n1
if n2>n1 and n2>n3:
    high = n2
if n3>n1 and n3>n2:
    high = n3

print('O maior número é ', high)