from PySimpleGUI import (
    Window, Button, Text, Image, Input, Column, VSeparator, ## Nesse exemplos exportamos mais algumas funções para criar uma janela dividida
    Push   
)


layout_esquerda = [
    [Image(filename='Barbara0_1.png')]
]

layout_direita = [
    [Text('Faça login para CONTINUAR')],
    [Text('Email:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [Push(), Button('LOGIN'), Push(), Button('RECUPERAR SENHA'), Push()],
]

layout = [
    [Column(layout_esquerda), VSeparator(), Column(layout_direita)]  
]

janela = Window(
    'Exemplo03',
    layout=layout
)

janela.read()
janela.close()