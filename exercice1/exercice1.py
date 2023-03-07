import math 

def seuil(prix, inflation):
    nmax = 0
    dictio = {nmax: prix}
    while prix < 1000:
        prix = round(prix * inflation, 2) 
        nmax += 1
        dictio[nmax] = prix
    return dictio



def exercice1():
    while True:
        prix = float(input("Rentrer P > "))
        inflation = float(input("Rentrez T > "))
        if prix < 1000:
            dictio = seuil(prix, inflation)
            break
        else:
            print("P doit être inférieur à 1000")
    print(" | Prix | Mois | ")
    for i in dictio:
        print(" | ", dictio[i], " | ", i, " | ")
    print("Nmax = ", i)    
        

