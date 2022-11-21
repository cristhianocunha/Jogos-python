import random
import os
from rich import print
from rich.panel import Panel

import adivianhacao


def mensagem_abertura():

    print(Panel.fit("************************\n Bem vindo ao jogo de Forca \n *******************************"))
    os.system("cls")
def carregar_palavra_secreta():
    arquivo = open("Lista-de-Palavras.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()
    n = random.randrange(0,len(palavra))
    palavra_secreta = palavra[n].upper()
    return palavra_secreta

def inicializa_letra_acertada(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra?").strip().upper()
    os.system("cls")
    return chute


def marca_chute_correto(chute, letras_acertasa, palavra_secreta):

    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertasa[posicao] = letra
        posicao = posicao + 1
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(Panel.fit("A palavra era {}".format(palavra_secreta)))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print(Panel.fit("A palavra era {}".format(palavra_secreta)))



def jogar_forca():
    mensagem_abertura()

    palavra_secreta = carregar_palavra_secreta()

    letras_acertasa = inicializa_letra_acertada(palavra_secreta)
    tentativas = adivianhacao.total_de_tentativas()
    print(tentativas)
    print(letras_acertasa)
    #print(Panel.fit(palavra_secreta))
    enforcou = False
    acertou = False
    erros = 0
    falta = len(palavra_secreta) + tentativas

    while (not enforcou and not acertou):
        chute = pede_chute()
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertasa, palavra_secreta)
            print(Panel.fit("Ops, você acertou! \n Faltam {} tentativas.".format(falta)))
        else:
            erros += 1
            falta -= 1
            print(Panel.fit("Ops, você errou! \n Faltam {} tentativas.".format(falta)))

        enforcou = erros == len(palavra_secreta) + tentativas
        acertou = "_" not in letras_acertasa
        print(letras_acertasa)
    if(acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)



if(__name__ == "__main__"):
    jogar_forca()