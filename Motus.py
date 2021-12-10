from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style
import random
dico=open("Dico.txt", "r")
indice=random.randint(0,9)
mot=dico.readlines()[0]
mot=mot[0:6]
essais=0
victoire=0

def verif() : 
    global mot,tentative,victoire
    mot2=mot
    for i in range (6) : 
        present=False
        if tentative[i]==mot[i] : 
            print (Back.RED+tentative[i], end="")
            victoire=victoire+1
        
        else: 
            for j in range (len(mot2)-1):
                if tentative[i]==mot2[j]:
                    present=True
            if tentative [i]!=mot[i] and present==True:
                print (Back.YELLOW+tentative[i], end="")
            if tentative [i]!=mot[i] and present==False:
                print (Back.BLUE+tentative[i], end="")




while essais<=8 and victoire!=6:
    tentative=input("Entrez un mot de 6 lettres""\n")
    verif()
    essais=essais+1

if victoire == 6 : 
    print("Gagné !")
else : 
    print("Perdu")
    print("Le mot était", mot)
dico.close()

