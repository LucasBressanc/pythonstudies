#escreva um algoritmo que pergunte um salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a R$1.250,00, calcule um aumento de 10%
#para os inferiores ou iguais, o aumento é de 15%

paywage = float(input('Digite o seu salário: '))

if paywage > 1250:
    raisepercent = 0.1
    raised = paywage + (paywage * raisepercent)
if paywage <= 1250:
    raisepercent = 0.15
    raised = paywage + (paywage * raisepercent)

print('Com um aumento de {}%, seu salário vai para: R${:.2f}' .format(raisepercent*100, raised))
