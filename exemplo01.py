from PySimpleGUI import Window, Button, Text, Slider


layout= [
    [Button('Botão 1'), Button('Botão 2')],
    [Text('Clica no botão acima')],
    [Slider(), Text('<-Arraste o Slide ao lado ')]
]

window = Window(
    'Titulo da janela', 
    size=(300,300),
    layout=layout
)

window.read()
window.close()