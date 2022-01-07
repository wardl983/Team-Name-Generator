import PySimpleGUI as sg

sg.theme('TanBlue')

layout = [
  [sg.Text('Team Name Generator')],
  [sg.Text('How Many Names Would You Like? (1-10): '), sg.Text(size=(2,1), 
  key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Get Names'), sg.Button('Exit')]]
  
window = sg.Window('Team Name Generator', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()