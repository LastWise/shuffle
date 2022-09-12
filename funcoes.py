from ast import While


def linha(tam=65):
    print("-" * tam)


def cabecalho(txt):
    linha()
    print(f"\033[33m{txt.center(50)}\033[m")
    linha()


def menu(titulo, lista):
    from time import sleep

    cabecalho("JOGO EMBARALHA PALAVRAS")
    print(titulo)
    linha()

    for c, item in enumerate(lista):
        print(f"\033[33m[ {c+1} ] -\033[m \033[34m{item}\033[m")
    linha()

    jogador = leia_int(("\033[32mSua opção: \033[m"))

    while True:
        if jogador >= 1 and jogador <= len(lista):
            break
        else:
            print(f"\033[31mERRO!!\033[m Digite uma opção válida")
        jogador = leia_int(("\033[32mSua opção: \033[m"))

    return jogador


def embaralha_palavra(palavra_sorteada):
    from random import shuffle

    palavra_embaralhada = list(palavra_sorteada)
    shuffle(palavra_embaralhada)
    return "".join(palavra_embaralhada)


def verifica_acerto(palavra_embaralhada, palavra_sorteada):
    frases_motivacao = [
        "Fique tranquilo você consegue!",
        "Não se desespere, você vai acertar!",
        "Otimismo, pode ser na próxima tentativa!",
        "Quase lá! Vamos não desista, tente novamente!",
    ]
    cont = 0
    tentativas = 5

    cabecalho("INTRUÇÕES DO JOGO")
    print(f"Você tem {tentativas} tentativas para acertar a palavra.")
    print(f"A palavra embaralhada é: \033[32m{palavra_embaralhada}\033[m")
    print("A palavra deve ser escrita conforme embaralhada e sem espaços.")
    linha()

    while True:
        jogador = str(input("\nDigite a palavra: ")).strip()

        if jogador == palavra_sorteada:
            print(
                f"\n\033[32mMuito bem, você é um campeão! Você acertou a palavra na {cont+1}° tentativa\033[m"
            )
            break

        elif cont <= 3:
            print(f"\033[31m{frases_motivacao[cont]}\033[m")
            cont += 1

        print(f"{tentativas-1} tentativas restantes")
        tentativas -= 1

        if tentativas == 0:
            print(
                f"\033[31mInfelizmente não foi dessa vez...\033[m A palavra correta era {palavra_sorteada}"
            )
            break
    linha()


def leia_int(msg):
    while True:
        try:
            num = int(input(msg))
        except:
            print("\033[31mERRO!!\033[m Por favor digite um número inteiro válido...")
        else:
            return num
    