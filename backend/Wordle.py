import string
from pprint import pprint


# 0 = GREY
# 1 = YELLOW
# 2 = GREEN



#Jos veikkauksessa sama kirjain vihreänä ja harmaana, haku kusee jos HARMAA ENSIN.

class Wordle:

    def __init__(self, guess_, ongoing=False):
        self.possible_words = []
        self.ongoing = ongoing
        self.guess = guess_
        
        self.makeLower()  
        
        self.initList()



    def makeLower(self):
        holder =[] 
        for x in range(len(self.guess)):
            holder.append(self.guess[x].lower())
        self.guess = holder

    def parseWords(self):

        lettersDict ={} 
        lettersDict["green"] = []
        lettersDict["yellow"] = []
        lettersDict["gray"] = []

        for x in range(len(self.guess)):
            if(int(self.guess[x][1]) == 2):
                lettersDict["green"].append(x)
            elif(int(self.guess[x][1]) == 1):
                lettersDict["yellow"].append(x) 
            elif(int(self.guess[x][1]) == 0):
                lettersDict["gray"].append(x) 

        new_possibles = []
        
        
        #pprint(lettersDict)
        for color in lettersDict:
            for index in lettersDict[color]:
                ignore = False
                if(color == "gray"):
                    for item in lettersDict["green"]:
                        if self.guess[index][0] == self.guess[item][0]:
                            ignore = True
                            break
                    for item in lettersDict["yellow"]:
                        if self.guess[index][0] == self.guess[item][0]:
                            ignore = True
                            break
                if ignore:
                    break  

                for word in self.possible_words:
   
                    if int(self.guess[index][1]) == 0:
                        if self.guess[index][0] not in word:
                            new_possibles.append(word.rstrip("\n"))

                    #KELTAINEN KIRJAIN
                    elif int(self.guess[index][1]) == 1:
                        ignore = False
                        noni = ""
                        
                        if self.guess[index][0] in word and self.guess[index][0] != word[index]:
                            for x in range(len(word)):
                                if x in lettersDict["green"]:
                                    pass
                                else:
                                    noni += word[x]
                            if self.guess[index][0] in noni:
                                new_possibles.append(word.rstrip("\n"))
                    #VIHREÄ
                    elif int(self.guess[index][1]) == 2:
                        if self.guess[index][0] == word[index]:
                            new_possibles.append(word.rstrip("\n"))

                
                self.possible_words = new_possibles
                new_possibles = []
                

        return self.trimList(self.possible_words)

    def initList(self):

        if self.ongoing:
            path = "wordsFound.txt"
        else:
            path = "eng_alpha.txt"
        with open(path, "r") as f:
            for item in f:
                self.possible_words.append(item)


    def trimList(self, l):
        trimmedStr = ""
        for item in l:
            trimmedStr += item + "\n"
        
        return trimmedStr



    def makeWordsOfLenghtFive(self):
        with open("english_words_alpha.txt", 'r') as f:
            for item in f:
                if(len(item.rstrip()) == 5):
                    self.possible_words.append(item.rstrip())


   


