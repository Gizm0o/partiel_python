from exercice1.exercice1 import  exercice1
from exercice2.exercice2 import  exercice2
from exercice3.exercice3 import  exercice3
 
def menu():
    print("Bienvenue dans le menu du partiel de Python")
    while True:
        try:
            print("--------------------")
            print("1. Exercice 1")
            print("2. Exercice 2")
            print("3. Exercice 3")
            print("4. Quitter")
            print("--------------------")
            choix = int(input("Choix > "))
            if choix == 1:
                #add 1 space before and after the function name
                print("")
                exercice1()
                print("")
            elif choix == 2:
                exercice2()
            elif choix == 3:
                exercice3()
            elif choix == 4:
                break
            else:
                print("Choix invalide")
        except ValueError:
            print("Choix invalide")

if __name__ == "__main__":
    menu()
   
