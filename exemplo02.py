from PySimpleGUI import (
    Window, Button, Text, Image, Input
    )

layout=[
    [Image(filename='Barbara0_1.png')],
    [Text('Olá, eu sou Barbara, Faça login para continuar.')],
    [Text('Email:'), Input()],
    [Text('Senha:'), Input(password_char='*')],
    [Button('Login'), Button('Recuperar Senha')],

]

janela = Window(
    'PySimpleGUI Test',
    layout=layout,
    element_justification='c'

)

janela.read()

janela.close()
