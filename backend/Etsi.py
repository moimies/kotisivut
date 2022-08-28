
import time
from Position import Position


class Etsi:

    def __init__(self, l):
        self.words = []
        self.letters = l
        for x in range(len(self.letters)):
            self.letters[x] = str(self.letters[x]).lower()
        self.wordsForGame = []
        self.foundWords = ""

        self.initWordlist()

        self.main()



    def initWordlist(self):
        # CREATE WORDS FOR GAME, LETTERS IN ITEM MUST BE IN SELF.LETTERS, Len < 16
        file = open("words_for_game.txt", encoding="utf-8", mode="r")
        addWord = False
        for item in file:
            #print(item)

            for l in item.rstrip("\n"):
                if l not in self.letters:
                    addWord = False
                    break
                else:
                    addWord = True

            if len(item.rstrip("\n")) > 16:
                addWord = False
                pass

            if addWord:

                self.wordsForGame.append(item.rstrip("\n"))

        file.close()


    def listforPos(self, p, wordlist):
        list = []

        pituus = len(p.mm)

        for item in wordlist:

            if item == p.word().rstrip("\n"):
                self.words.append(item)

            elif item[0:pituus] == p.word().rstrip("\n"):
                list.append(item)   

        return list


    def call(self,p,wordstoparse):

        possibles = p.pm

        for item in possibles:

            temp = Position(p.mm,item,self.letters,self.words)
            l = self.listforPos(temp,wordstoparse)

            if l:
                self.call(temp, l)

    def printLetters(self):
        l = ""
        x = 0
        for item in self.letters:

            if x == 3 or x == 7 or x == 11:
                l = l + str(item) + str("\n")
            else:
                l = l + str(item) + str(" ")

            x += 1

        return l


    def arrangeWords(self):

        self.words = list(dict.fromkeys(self.words))
        self.sorting(self.words)

        apuri = 0
        for tolo in self.words:

            if apuri == 3:
                self.foundWords = self.foundWords + str(tolo) + str("\n")
                apuri = 0
            else:
                self.foundWords = self.foundWords + str(tolo) + str("       ")
            apuri += 1



    def sorting(self,lst):
        lst.sort(reverse=True, key=len)
        return lst


    def main(self):
        p = Position([],0,self.letters,self.words)

        for xy in range(0, len(self.letters)):
            self.call(Position([], xy,self.letters, self.words),self.wordsForGame)


        print(self.printLetters())
        self.arrangeWords()
        #print(self.foundWords)










