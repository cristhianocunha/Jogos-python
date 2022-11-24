import forca
import adivianhacao
import PySimpleGUI as sg


def jogos():

    sg.theme('DarkAmber')
    layout = [[sg.Text('--- JOGOS PYTHON ---')],
              [sg.Text('Qual Jogo?')],
              [sg.Button('Adivinhacao'), sg.Button('Forca')]],

    window = sg.Window('Window Title', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
            break
        elif (event == 'Forca'):
            forca.jogar_forca()
        elif (event == 'Adivinhacao'):
            adivianhacao.jogar_adivinhacao()


    window.close()


if (__name__ == "__main__"):
    jogos()
