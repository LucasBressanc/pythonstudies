import random

MAXIMO_DE_LINHAS = 3
APOSTA_MAXIMA = 100
APOSTA_MINIMA = 1

FILEIRAS = 3
COLUNAS = 3

contador_de_simbolos = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

valores_de_simbolos = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def checagem(colunas, linhas, aposta, valores):
    ganhos = 0
    ganhos_em_linhas = []
    for linha in range(linhas):
        simbolo = colunas[0][linha]
        for coluna in colunas:
            checagem_de_simbolo = coluna[linha]
            if simbolo != checagem_de_simbolo:
                break
        else:
            ganhos += valores[simbolo] * aposta
            ganhos_em_linhas.append(linha + 1)

    return ganhos, ganhos_em_linhas

def processar_giro(fils, cols, simbolos):
    todos_simbolos = []
    for simbolo, contador_de_simbolo in simbolos.items():
        for _ in range(contador_de_simbolo):
            todos_simbolos.append(simbolo)

    colunas = []
    for _ in range(cols):
        coluna = []
        simbolos_atuais = todos_simbolos[:]
        for _ in range(fils):
            valor = random.choice(simbolos_atuais)
            simbolos_atuais.remove(valor)
            coluna.append(valor)

        colunas.append(coluna)

    return colunas

def caca_niquel(colunas):
    for linha in range(len(colunas[0])):
        for i, coluna in enumerate(colunas):
            if i != len(colunas) - 1:
                print(coluna[linha], end=" | ")
            else:
                print(coluna[linha], end="")

        print()

def deposito():
    while True:
        valor_deposito = input("Qual o valor a ser depositado? R$")
        if valor_deposito.isdigit():
            valor_deposito = int(valor_deposito)
            if valor_deposito > 0:
                break
            else:
                print("A quantia deve ser maior que R$0,00.")
        else:
            print("Por favor, digite um número.")

    return valor_deposito

def quantidade_de_linhas():
    while True:
        linhas = input("Qual a quantidade de linhas que deseja apostar (1-" + str(MAXIMO_DE_LINHAS) + ")? ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAXIMO_DE_LINHAS:
                break
            else:
                print("Digite uma quantidade valida de linhas.")
        else:
            print("Por favor, digite um número.")

    return linhas

def processar_aposta():
    while True:
        quantia = input("Quanto gostaria de apostar em cada linha? R$")
        if quantia.isdigit():
            quantia = int(quantia)
            if APOSTA_MINIMA <= quantia <= APOSTA_MAXIMA:
                break
            else:
                print(f"A quantia deve estar entre R${APOSTA_MINIMA} e R${APOSTA_MAXIMA}.")
        else:
            print("Por favor, digite um número.")

    return quantia

def jogo(saldo):
    linhas = quantidade_de_linhas()
    while True:
        aposta = processar_aposta()
        aposta_total = aposta * linhas

        if aposta_total > saldo:
            print(f"Seu saldo nao e suficiente para essa aposta. Seu saldo: {saldo},00")
        else:
            break

    print(f"Voce esta apostando R${aposta},00 em {linhas} linhas. Aposta total: R${aposta_total},00")

    slots = processar_giro(FILEIRAS, COLUNAS, contador_de_simbolos)
    caca_niquel(slots)
    ganhos, ganhos_em_linhas = checagem(slots, linhas, aposta, valores_de_simbolos)
    print(f"Voce ganhou R${ganhos},00.")
    print(f"Voce ganhou nas linhas:", *ganhos_em_linhas)
    return ganhos - aposta_total

def main():
    saldo = deposito()
    while True:
        (f"Seu saldo: ${saldo}")
        resposta = input("Digite enter para jogar (s para sair).")
        if resposta == "s":
            break
        saldo += jogo(saldo)

    print(f"Voce saiu com ${saldo},00")

main()
