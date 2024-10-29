#Digite a velocidade e calcule a multa por excesso de velocidade

print('Limite de velocidade: 80km/h')
print('Multa: R$7,00 por km acima do limite')

speed = int(input('Digite a velocidade que seu carro estava no momento que passou no radar: '))

if speed <= 80:
    print('Não se preocupe! Sua velocidade estava dentro dos limites.')
else:
    print('EXCESSO DE VELOCIDADE')
    print('Sua velocidade: {}km/h' .format(speed))
    print('Valor da multa: R${}' .format((speed - 80)* 7))