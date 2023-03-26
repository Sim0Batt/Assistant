import os.path
list_of_args = open("argv/list_of_args.txt", 'a')

class sett():

    def date_modifying(query):
        aa = query
        if '/' in aa:
            aa = aa.replace('/', ' ')
        if "january" in aa:
            aa = aa.replace('january', '1')
            print('confirmed')
        if "february" in aa:
            aa = aa.replace('february', '2')
        if "march" in aa:
            aa = aa.replace('march', '3')
        if "april" in aa:
            aa = aa.replace('april', '4')
        if "may" in aa:
            aa = aa.replace('may', '5')
        if "june" in aa:
            aa = aa.replace('june', '6')
        if "july" in aa:
            aa = aa.replace('july', '7')
        if "august" in aa:
            aa = aa.replace('august', '8')
        if "september" in aa:
            aa = aa.replace('septermber', '9')
        if "october" in aa:
            aa = aa.replace('october', '10')
        if "november" in aa:
            aa = aa.replace('november', '11')
        if "december" in aa:
            aa = aa.replace('december', '12') 
        return aa 
    
    
    def check_create(aa):
        if os.path.isfile(f'.\ToDo\{aa}.txt') == True:
            p = open(f'.\ToDo\{aa}.txt', 'a')
        else:
            p = open(f'.\ToDo\{aa}.txt', 'x')
            p = open(f'.\ToDo\{aa}.txt', 'a')
        return p