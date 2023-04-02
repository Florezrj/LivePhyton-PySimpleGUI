# Tive a ideia de criar uma interface para um game simples utilizando o Random.

from PySimpleGUI import *
from random import randint

pc = randint(1,5)
count = 0
theme('Dark')
layout = [
    [Text('Você consegue ler minha mente?')],
    [Text('Qual número de 1 a 5 eu pensei?')],
    [Text('Resposta: '), Input(key='-RESP-')],
    [Button('TENTAR RESPOSTA', key='-TENTAR-')],
    [Text(f'Você errou {count} vezes', key='text')]
]

janela = Window(
    'Leia minha Mente',
    layout=layout,
    finalize=True
)

janela['-RESP-'].bind("<Return>", "_Enter")


while True:
    event, values = janela.read()
    if event == WINDOW_CLOSED:
        break
    elif event == "-RESP-" + "_Enter" or event == '-TENTAR-':
        user = int(values['-RESP-'])
        if user == pc:
            popup('PARABÉNS ACERTOU')
            break
        else:
            popup('Errou, tente novamente')
            count += 1
            janela.FindElement('text').Update(f'Você errou {count} vezes')

janela.close()
