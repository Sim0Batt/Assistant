import wolframalpha
import PySimpleGUI as sg
import PySimpleGUI as jk
import pywhatkit as pwt
import pywhatkit as kt
import PySimpleGUI as lt
from script.recognition import rec
from script.setting import sett
app_id = "9X4PEH-6HGQJAW8XP"

args = open("argv/list_of_args.txt", "a")
words = open("argv/specific_words.txt", "r")
play = open("argv/play.txt", "r")
plays = open("argv/play.txt", "a")

a = words.read()
list_words = a.split(',')

sg.theme('DarkPurple')
layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Gaia', layout)

#ToDo       
jk.theme('BluePurple')
layout2 = [[jk.Text('Enter the day'), jk.InputText()],[jk.Button('Ok'), jk.Button('Close')]]
window2 = jk.Window("Gaia ToDos", layout2)
 
lt.theme('BluePurple')
layout3 = [[lt.Text('Enter your ToDo'), lt.InputText()],[lt.Button('Ok'), lt.Button('Close')]]
window3 = lt.Window("Gaia ToDos", layout3)


#PLAY
lista2 = []
aa = rec.rendering()
rec.dictionarying(aa)

#TO DO SECTION
todo_list = list()


while True:
    event, values = window.read()
    try:
        if event in (None, 'Cancel'):
            sg.Popup("Goodbye sir")
            break

        values[0] = values[0].lower()
        
        if "ciao" in values[0]:
            sg.Popup('HI')
            args.write(values[0] + ',')


        if 'play' in values[0]:
            args.write(values[0] + ',')
            query = values[0].replace('play', '')
            if 'from' in query:
                query = query.replace('from', '')
            if 'on' in query:
                query = query.replace('on', '')
            if 'youtube' in values[0]:
                query = query.replace('youtube', '').strip()
                lista2.append(query.strip())
                pwt.playonyt(query)
                sg.Popup(f'Here it is {query}')        
        
        
        if 'search' in values[0]:
            args.write(values[0] + ';;')
            query = values[0].replace('search', ' ')
            kt.search(query)


        if 'todo' in values[0]:
            sg.Popup("Welcome to Gaia's To Do section")
            while True:
                event2, values2 = window2.read()
                if event2 in (None, 'Close'):
                    jk.Popup("Goodbye sir")
                    window2.close()
                    break
                query = values2[0]
                query = query.lower()
                file_todo = query
                while True:
                    event3, values3 = window3.read()
                    if event3 in (None, 'Close'):
                        lt.Popup("Goodbye sir")
                        window3.close()
                        break
                    query0 = values3[0]
                    todo_list.append(query0)
                
                    
              
        
        
#        if not values[0] in list_words:
#            client = wolframalpha.Client(app_id)
#            wolfram_res = next(client.query(values[0]).results).text
#            sg.Popup(wolfram_res)
#            args.write(values[0] + ',')



    except:
        sg.Popup('Sorry there is nothing that satisfy your question')



#client = wolframalpha.Client(app_id)
#res = client.query(question)
#answer = next(res.results).text

file_opened_todo = sett.check_create(sett.date_modifying(file_todo))
for i in todo_list:
    file_opened_todo.write(i + ',')
    
for j in lista2:
    plays.write(j + ',')

plays.close()
play.close()
words.close()
args.close()
window.close()