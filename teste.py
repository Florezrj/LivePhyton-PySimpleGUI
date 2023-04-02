import PySimpleGUI as sg

sg.theme('DarkBlue3')
sg.set_options(font=('Courier New', 16))

layout = [
    [sg.Input('Enter para gerar um evento', key='Input1')],
    [sg.Button('Ok'), sg.Button('Cancel')]
]

window = sg.Window('Janela', layout, finalize=True)
window['Input1'].bind("<Return>", "_Enter")


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    elif event == 'Ok':
        print('Botão Ok pressionado')
    elif event == 'Input1' + '_Enter':
        print('Tecla Enter pressionada em Input1')

window.close()