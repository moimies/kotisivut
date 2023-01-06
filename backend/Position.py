

class Position:


    def __init__(self, madeMoves,x_,letters_, wordlist):
        self.letters = letters_
        self.x = x_
        self.mm = madeMoves.copy()
        self.pm = self.createPossibleDirections() 
        #max length
        if len(self.mm) < 15:
            self.mm.append(self.x)
            #wordlist.append(self.word())


    def createPossibleDirections(self):
        possibles = []
        if self.x == 0:
            possibles.append(1)
            possibles.append(4)
            possibles.append(5)
        elif self.x == 1:
            possibles.append(0)
            possibles.append(2)
            possibles.append(4)
            possibles.append(5)
            possibles.append(6)
        elif self.x == 2:
            possibles.append(1)
            possibles.append(3)
            possibles.append(5)
            possibles.append(6)
            possibles.append(7)
        elif self.x == 3:
            possibles.append(2)
            possibles.append(6)
            possibles.append(7)
        elif self.x == 4:
            possibles.append(0)
            possibles.append(1)
            possibles.append(5)
            possibles.append(8)
            possibles.append(9)
        elif self.x == 5:
            possibles.append(0)
            possibles.append(1)
            possibles.append(2)
            possibles.append(4)
            possibles.append(6)
            possibles.append(8)
            possibles.append(9)
            possibles.append(10)
        elif self.x == 6:
            possibles.append(1)
            possibles.append(2)
            possibles.append(3)
            possibles.append(5)
            possibles.append(7)
            possibles.append(9)
            possibles.append(10)
            possibles.append(11)
        elif self.x == 7:
            possibles.append(2)
            possibles.append(3)
            possibles.append(6)
            possibles.append(10)
            possibles.append(11)
        elif self.x == 8:
            possibles.append(4)
            possibles.append(5)
            possibles.append(9)
            possibles.append(12)
            possibles.append(13)
        elif self.x == 9:
            possibles.append(4)
            possibles.append(5)
            possibles.append(6)
            possibles.append(8)
            possibles.append(10)
            possibles.append(12)
            possibles.append(13)
            possibles.append(14)
        elif self.x == 10:
            possibles.append(5)
            possibles.append(6)
            possibles.append(7)
            possibles.append(9)
            possibles.append(11)
            possibles.append(13)
            possibles.append(14)
            possibles.append(15)
        elif self.x == 11:
            possibles.append(6)
            possibles.append(7)
            possibles.append(10)
            possibles.append(14)
            possibles.append(15)
        elif self.x == 12:
            possibles.append(8)
            possibles.append(9)
            possibles.append(13)
        elif self.x == 13:
            possibles.append(8)
            possibles.append(9)
            possibles.append(10)
            possibles.append(12)
            possibles.append(14)
        elif self.x == 14:
            possibles.append(9)
            possibles.append(10)
            possibles.append(11)
            possibles.append(13)
            possibles.append(15)
        elif self.x == 15:
            possibles.append(10)
            possibles.append(11)
            possibles.append(14)

        p = []

        for item in possibles:
            if item in self.mm:
                pass
            else:
                p.append(item)
        return p

    def word(self):
        word = ""
        for item in self.mm:
            word += self.letters[item]

        word += "\n"
        return word








