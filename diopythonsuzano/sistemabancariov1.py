def main():
    saldo = 5500
    saques_realizados = 0
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
            saldo = depositar(saldo, historico)
        elif opcao == "s":
            saldo, saques_realizados = sacar(saldo, saques_realizados, historico)
        elif opcao == "e":
            extrato(historico, saldo)
        elif opcao == "x":
            print("Obrigado por usar o banco DIO!")
            break
        else:
            print("Opcao invalida! Por favor digite uma das opcoes acima.")

def depositar(saldo, historico):
    while True:
        deposito = float(input("Digite o valor do deposito: R$"))
        if deposito <= 0:
                print("Por favor, digite um valor valido!")
        else:
                saldo += deposito
                historico.append(f"DEPOSITO: +R${deposito:.2f}")
                print(f"Deposito efetuado com sucesso! Saldo atualizado: {saldo:.2f}")
                return saldo

def sacar(saldo, saques_realizados, historico):
    LIMITE_SAQUES = 3
    LIMITE_POR_SAQUE = 500

    if saques_realizados >= LIMITE_SAQUES:
        print("Voce atingiu o limite diario de saques (3 saques por dia.)")
        return saldo, saques_realizados
    
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
            saques_realizados += 1
            historico.append(f"SAQUE: -R${saque:.2f}")
            print(f"Saque efetuado com sucesso! Saldo atualizado: {saldo:.2f}")
            return saldo, saques_realizados
        
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