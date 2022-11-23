import forca
import adivianhacao
import PySimpleGUI as sg

jogo = sg.InputText()
sg.theme('DarkAmber')
layout = [[sg.Text('Some text on Row 1')],
              [sg.Text('qual jogo?')],
              [sg.Button('adivinhacao'), sg.Button('forca')]],



window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    elif(event == 'forca'):
         forca.jogar_forca()
    elif(event == 'adivinhacao'):
        adivianhacao.jogar_adivinhacao()
window.close()
#def jogos():






    #jogo = int(input("qual jogo?"))

  #  if(jogo == 1):
   #     print("jogando forca")
   #     forca.jogar_forca()
   # elif(jogo == 2):
   #     print("jogando adivinhação")
   #     adivianhacao.jogar_adivinhacao()

#if(__name__ == "__main__"):
#    jogos()
