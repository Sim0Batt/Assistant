play = open('argv/play.txt', 'r')
list_of_args = open("argv/list_of_args.txt", 'a')

class rec():
    def rendering():
        keys = []
        for i in play:
            keys = i.split(',')
        for j in keys:
            j.strip()
        keys.pop(-1)
        return keys


    def dictionarying(keys):
        dic_play = {}
        for i in keys:
            if not i in dic_play:
                dic_play[i] = 1
            else:
                dic_play[i] += 1
        return dic_play      
        
