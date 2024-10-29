
print('Para viagens com trajeto de até 200km, o valor do km rodado é R$0,50')
print('Para viagens com trajeto com mais de 200km, o valor do km rodado é R$0,45')
km = float(input('Digite a distância da sua viagem, em kilômetros: '))

if km <= 200:
    print('O valor da sua passagem é: R$', float(km * 0.5))
else: print('O valor da sua passagem é R$', float(km * 0.45))