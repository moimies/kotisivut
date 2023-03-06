import string
from pprint import pprint
import os


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
        to_ignore =[] 
        new_possibles = []
        
        for x in range(len(self.guess)):
            if(int(self.guess[x][1]) == 2):
                lettersDict["green"].append(x)
                to_ignore.append(x)
            elif(int(self.guess[x][1]) == 1):
                lettersDict["yellow"].append(x) 
            elif(int(self.guess[x][1]) == 0):
                lettersDict["gray"].append(x) 

        
        #pprint(lettersDict)
        #index = MONES KIRJAIN KÄYTTÄJÄN VEIKKAUKSESSA
        #letter in word
        #KUTISTA WORDIA MAHDOLLISUUKSIEN KANSSA
        for color in lettersDict:
            for x in lettersDict[color]:
                ignore = False
                
                #print(len(self.possible_words))

                for w in self.possible_words:
                    word = w.strip()
                    
                    if(color == "gray"):
                        if self.guess[x][0] in list([self.guess[n][0] for n in lettersDict['yellow']]):
                            ignore = True
                            break
                            
                        mword = ""
                        
                        for ign in range(len(word)):
                            if ign not in to_ignore:
                                mword += word[ign] 
                        
                        if self.guess[x][0] not in mword:
                            new_possibles.append(word)
                        #print('gray')

                    #KELTAINEN KIRJAIN
                    elif (color == "yellow"):
                        
                        y_to_ignore = to_ignore.copy()  
                        y_to_ignore.append(x)
                        for m in lettersDict['yellow']:
                            if x != m:
                                if self.guess[x][0] in list([self.guess[n][0] for n in lettersDict['yellow']]):
                                    y_to_ignore.append(m)
                            
                        for m in lettersDict['gray']:
                            if self.guess[x][0] == self.guess[m][0]:
                                y_to_ignore.append(m)    

                        mword = ""
                        
                        for ign in range(len(word)):
                            if ign not in y_to_ignore:
                                mword += word[ign] 
                            
                        if len(mword) > 0:
                            if self.guess[x][0] in mword:
                                new_possibles.append(word)
                        
                        #print('yellow')
                        
                        #eka vihree, poista vihreät valitut veikkauksesta
                    elif (color == "green"):

                        if self.guess[x][0] == word[x]:
                            new_possibles.append(word)

                        #print("green")


                print(f"color :{color} ")
                print(f"new possbles:{len(new_possibles)} ")
                print(f"self.possib.e :{len(self.possible_words)} ")
                if not ignore:
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
        if(len(l) == 0):
            print("List is empty")
            return
        trimmedStr = ""
        for item in l:
            trimmedStr += item + "\n"
        
        return trimmedStr



    def makeWordsOfLenghtFive(self):
        with open("english_words_alpha.txt", 'r') as f:
            for item in f:
                if(len(item.rstrip()) == 5):
                    self.possible_words.append(item.rstrip())


   


