import forca
import adivianhacao

def jogos():
    print("*********************************")
    print("ESCOLHA SEU JOGO")
    print("*********************************")

    print("(1) forca, (2) Adivinhaçao")

    jogo = int(input("qual jogo?"))

    if(jogo == 1):
        print("jogando forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("jogando adivinhação")
        adivianhacao.jogar_adivinhacao()

if(__name__ == "__main__"):
    jogos()
