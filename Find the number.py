from random import randint 


class FindTheNumber():
    def __init__(self) -> None:
        self.compteur = 0
        self.nombre = 0
        self.entry = 0 

    def genere(self):
        self.nombre = randint(1,10000)

    def getEntry(self):
        self.entry = int(input("ta propostion : "))

    def calcul(self):
        if self.nombre == self.entry : 
            self.code = 1
        elif self.nombre < self.entry :
            self.code = 2
        else : 
            self.code = 3
    
    
    def start(self):
        self.genere()
        self.code = -1
        while True : 
            self.getEntry()
            self.calcul()
            if self.code == 1 :
                print("Bravo le nombre était : {}".format(self.nombre))
                break
            elif self.code == 2 :
                print("-")
            elif self.code == 3 :
                print("+")
        restart = input("Tu veux rejouer ? Y/N : ").upper()
        if restart == "Y" : 
            self.start()
        else :
            exit() 
            

game = FindTheNumber()
game.start()