import wolframalpha
import PySimpleGUI as sg
import pywhatkit as pwt
import pywhatkit as kt
app_id = "9X4PEH-6HGQJAW8XP"

path_args = "argv/list_of_args.txt"
path_spec = "argv/specific_words.txt"
args = open(path_args, "a")
words = open(path_spec, "r")

a = words.read()
list_words = a.split(';')




sg.theme('DarkPurple')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Gaia', layout)


while True:
    event, values = window.read()
    try:
        if event in (None, 'Cancel'):
            sg.Popup("Goodbye sir")
            break


        if values[0] == "ciao":
            sg.Popup('HI')
            args.write(values[0] + ";;")

        if 'play' in values[0]:
            args.write(values[0] + ";;")
            values[0].replace('play', '')
            if 'youtube' in values[0]:
                pwt.playonyt(values[0])

        if 'search' in values[0]:
            query  == values[0]
            query.replace(search, ' ')
            kt.search(query)

        if not values[0] in list_words:
            client = wolframalpha.Client(app_id)
            wolfram_res = next(client.query(values[0]).results).text
            sg.Popup(wolfram_res)
            args.write(values[0] + ";;")



    except:
        sg.Popup('Sorry there is nothing that satisfy your question')



#client = wolframalpha.Client(app_id)
#res = client.query(question)
#answer = next(res.results).text



words.close()
args.close()
window.close()
