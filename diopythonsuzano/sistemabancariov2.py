from datetime import datetime

def main():
    saldo = 5500
    operacoes_realizadas = 0
    historico = []

    print("Bem vindo ao banco DIO")
    print(f"Seu saldo: R${saldo:.2f}")

    while True:
        print("""
        [d]: DEPOSITO
        [s]: SAQUE
        [e]: EXTRATO
        [x]: SAIR
        """)

        opcao = input("Digite a opcao desejada: ").lower()

        if opcao == "d":
            saldo, operacoes_realizadas = depositar(saldo, operacoes_realizadas, historico)
        elif opcao == "s":
            saldo, operacoes_realizadas = sacar(saldo, operacoes_realizadas, historico)
        elif opcao == "e":
            extrato(historico, saldo)
        elif opcao == "x":
            print("Obrigado por usar o banco DIO!")
            break
        else:
            print("Opcao invalida! Por favor digite uma das opcoes acima.")

def depositar(saldo, operacoes_realizadas, historico):
    LIMITE_OPERACOES = 10

    if operacoes_realizadas >= LIMITE_OPERACOES:
        print("Voce atingiu o limite diario de operacoes (10 por dia.)")
        return saldo, operacoes_realizadas
    
    while True:
        deposito = float(input("Digite o valor do deposito: R$"))
        if deposito <= 0:
            print("Por favor, digite um valor valido!")
        else:
            saldo += deposito
            operacoes_realizadas += 1
            hora_transacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            historico.append(f"{hora_transacao} - DEPOSITO: +R${deposito:.2f}")
            print(f"Deposito efetuado com sucesso! Saldo atualizado: {saldo:.2f}")
            return saldo, operacoes_realizadas

def sacar(saldo, operacoes_realizadas, historico):
    LIMITE_POR_SAQUE = 500
    LIMITE_OPERACOES = 10

    if operacoes_realizadas >= LIMITE_OPERACOES:
        print("Voce atingiu o limite diario de operacoes (10 por dia.)")
        return saldo, operacoes_realizadas
    
    while True:
        saque = float(input("Digite o valor do saque: R$"))
        if saque <= 0:
            print("O valor do saque deve ser maior que zero.")
        elif saque > LIMITE_POR_SAQUE:
            print(f"O limite por saque é de {LIMITE_POR_SAQUE} por dia.")
        elif saque > saldo:
            print("Saldo insuficiente! Por favor, digite um valor menor.")
        else:
            saldo -= saque
            operacoes_realizadas += 1
            hora_transacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            historico.append(f"{hora_transacao} - SAQUE: -R${saque:.2f}")
            print(f"Saque efetuado com sucesso! Saldo atualizado: {saldo:.2f}")
            return saldo, operacoes_realizadas
        
def extrato(historico, saldo):
    print("\n========= EXTRATO =========")
    if historico:
        for operacao in historico:
            print(operacao)
    else:
        print("Nenhuma operacao efetuada.")
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("===========================")

main()