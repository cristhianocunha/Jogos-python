import random

import rich
from rich.panel import Panel

def total_de_tentativas():
    print("qual nivel de dificuldade?")
    print("Hello, [red]World!")
    print("(1) facil, (2) medio, (3) dificil ")
    nivel = int(input("define qual nivel: "))

    total_de_tentativas = 0
    if (nivel == 1):
        total_de_tentativas = 9
    elif (nivel == 2):
        total_de_tentativas = 6
    elif (nivel == 3):
        total_de_tentativas = 3
    return total_de_tentativas


def jogar_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = random.randrange(1,101)

    pontos = 1000

    tentativas = total_de_tentativas()
    for rodada in range( 1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))

        chute_str = input("Digite o seu número: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Parabéns! Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo o numero segreto era: {} ".format(numero_secreto))

if(__name__ == "__main__"):
    jogar_adivinhacao()
