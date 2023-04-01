## Começando a ler eventos e pegar o valor das coisas.

from PySimpleGUI import Window, Button, Text, Image, Input, Column, HSeparator, Push, theme, popup


theme('DarkPurple')

layout_esquerda = [
    [Image(filename='Barbara0_1.png')]
]

layout_direita = [
    [Text('Faça login para CONTINUAR')],
    [Text('Email:'), Input(key='-EMAIL-')],
    [Text('Senha:'), Input(password_char='*', key='-SENHA-')],
    [Push(), Button('LOGIN'), Push(), Button('RECUPERAR SENHA'), Push()],
]

layout = [
    [layout_esquerda], 
    [HSeparator()],
    [layout_direita]  
]

janela = Window(
    'Exemplo03',
    layout=layout
)

while True:
    event, values = janela.read()
    print(event, values)
    match(event):
        case 'LOGIN':
            if values['-EMAIL-'] == 'bernardowelsing90@gmail.com':
                popup('LOGIN FEITO COM SUCESSO')
                break
            else: 
                popup('Email invalido!')
        case None:
            break

janela.close()