import PySimpleGUI as sg

file_label = sg.Text('Choose File:    ')
file_input = sg.Input()
file_button = sg.Button(' Select File  ')

folder_label = sg.Text('Choose Folder:')
folder_input = sg.Input()
folder_button = sg.Button('Select Folder')

extract_button = sg.Button('Extract')
success_message = sg.Text()

window = sg.Window('Extract File', [
    [file_label, file_input, file_button],
    [folder_label, folder_input, folder_button],
    [extract_button, success_message]
])

window.read()
window.close()
