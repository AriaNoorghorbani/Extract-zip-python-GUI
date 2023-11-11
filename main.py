import PySimpleGUI as sg
from extractor import extractor

file_label = sg.Text('Choose File:    ')
file_input = sg.Input()
file_button = sg.FileBrowse(' Select File  ')

folder_label = sg.Text('Choose Folder:')
folder_input = sg.Input()
folder_button = sg.FolderBrowse('Select Folder')

extract_button = sg.Button('Extract')
success_message = sg.Text(key='success')

window = sg.Window('Extract File', [
    [file_label, file_input, file_button],
    [folder_label, folder_input, folder_button],
    [extract_button, success_message]
])

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Extract":
            file_path = value[' Select File  ']
            folder = value['Select Folder']
            print(file_path)
            print(folder)
            extractor(file_path, folder)
            window['success'].update(value="Extracted Successfully")
        case sg.WINDOW_CLOSED:
            break
window.close()
