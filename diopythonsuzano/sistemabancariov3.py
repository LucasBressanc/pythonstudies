from datetime import datetime

usuarios = []
contas = []
numero_conta = 1

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
        [c]: CADASTRAR USUARIO
        [l]: LISTAR USUARIOS
        [a]: CRIAR CONTA
        [x]: SAIR
        """)

        opcao = input("Digite a opcao desejada: ").lower()

        if opcao == "d":
            saldo, operacoes_realizadas = depositar(saldo, operacoes_realizadas, historico)

        elif opcao == "s":
            saldo, operacoes_realizadas = sacar(saldo, operacoes_realizadas, historico)

        elif opcao == "e":
            extrato(historico, saldo)

        elif opcao == "c":
            cadastrar_usuario()

        elif opcao == "l":
            listar_usuarios()

        elif opcao == "a":
            criar_conta()
            
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
            print(f"O limite por saque e de {LIMITE_POR_SAQUE} por dia.")
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

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    cpf = input("Digite o CPF (somente numeros): ").replace("-", "").replace(".", "")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    if any(usuario['cpf'] == cpf for usuario in usuarios):
        print("Já existe um usuário cadastrado com esse CPF!")
        return
    
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    
    usuarios.append(usuario)
    print(f"Usuario com o CPF {cpf} cadastrado com sucesso!")

def listar_usuarios():
    if not usuarios:
        print("Nenhum usuario cadastrado.")
        return

    print("\n===== USUARIOS CADASTRADOS =====")
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"Data de Nascimento: {usuario['data_nascimento']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Endereco: {usuario['endereco']}")
        print("===============================")

def criar_conta():
    cpf_usuario = input("Digite o CPF do usuario para criar a conta (somente numeros): ").replace("-", "").replace(".", "")
    
    usuario = next((u for u in usuarios if u['cpf'] == cpf_usuario), None)
    
    if usuario is None:
        print("Usuário não encontrado!")
        return
    
    global numero_conta
    agencia = "0001"
    numero_conta_str = f"{numero_conta:04d}"
    
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta_str,
        "usuario": usuario['nome']
    }
    
    contas.append(conta)
    numero_conta += 1

    print(f"Conta criada com sucesso! Nomero da conta: {numero_conta_str}")

main()