
#Code to develop GUI, using realpython website 06-10-2021 using pysimpleGUI

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Window

global mode,formname,date,client,isdownload,tstatus

#You can use the output from here in sg.theme
# theme_name_list = sg.theme_list()
# print(theme_name_list)

def pyGUI():
    # sg.Window(title="Hello World", layout=[[]], margins=(500, 100)).read()
    # sg.theme('DarkAmber')
    
    layout = [
                [sg.Text("Do you want to run Automatic or Manual Process:?\n 1=Automatic\n 2=Manual\n")], 
                [sg.Input(key='MODE')],
                # [sg.Button("OK")],

                [sg.Text("Select the form name:?\n 1=EX201 - Excise Goods that require Customs clearance\n 2=EX202A – Designated Zone Reporting\n 3=EX202B – Producer Declaration\n 4=Inventory - EX203A - Local Purchase Form\n 5=Inventory - EX203B - Lost and Damaged Declaration\n 6=Inventory – EX203C – Transfer of Ownership Within Designated Zones\n 7=EX203 - Deductible Excise Tax\n")], 
                [sg.Input(key='FORMNAME')],
                # [sg.Button("OK")]

                [sg.Text("Please Enter the Period in the format M-YYYY / MM-YYYY (Eg: 1-2021 / 10-2021 :\n)")], 
                [sg.Input(key='DATE')],
                # [sg.Button("OK")]

                # [sg.Text("You are running for which user?\n 1 Alfakhar\n 2 Steinweg\n 3 Al Fakhama\n")], 
                # [sg.Input(key='CLIENT')],
                # [sg.Button("OK")]

                [sg.Text("Do you want to download data from taxcise? (y/n)")], 
                [sg.Input(key='ISDOWNLOAD')],
                # [sg.Button("OK")]

                [sg.Text("Please Select the Transaction Status to be considered\n 1 'Approved'\n 2 All Status except 'Drafted' and 'Reject'")], 
                [sg.Input(key='TSTATUS')],
                # [sg.Button("OK")]

                [sg.Text(size=(40,1), key='-OUTPUT-'),
                sg.Button('Proceed'),
                sg.Button('Quit')]
                ]

    #Creating a window

    window = sg.Window("ReconBOT", layout)#, margins=(300, 50)
    

    #create a event loop
    # event, values = window.read()

    # while True:
    #     event, values = window.read()
    #     # End program if user closes window or
    #     # presses ok button
    #     if event == "OK" or event == sg.WIN_CLOSED:
    #         break

    # Display and interact with the Window using an Event Loop
    while True:
        event, values = window.read()
            
        mode = values['MODE']
        formname = values['FORMNAME']
        date = values['DATE']
        # client = values['CLIENT']
        client = '1'
        isdownload = values['ISDOWNLOAD']
        tstatus = values['TSTATUS']
        eventmode = event
        
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Proceed':
            break

        break

        # Output a message to the window
        # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")
        ## window['-OUTPUT-'].update('Hello ' + values['CLIENT'] + "! Thanks for trying PySimpleGUI")
        ## print('Hello', values['FORMNAME'], "! Thank for using it")
        # print(mode,formname,date,client,isdownload)

    window.close

    if eventmode=='Proceed':
        result = mode,formname,date,client,isdownload,eventmode,tstatus
        # result = mode,formname,date,isdownload,eventmode,tstatus
    else:
        result = False

    return(result)

# print(pyGUI())
#testing07-07-2022 commit
