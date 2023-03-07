import os

class Materiel:
    def __init__(self, type, num_serie):
        self.type = type
        self.num_serie = num_serie

    def __str__(self):
        return "Type: %s, Numéro de série: %s" % (self.type, self.num_serie)
    

class Clavier(Materiel):
    def __init__(self, type, num_serie, nb_touche):
        Materiel.__init__(self, type, num_serie)
        self.nb_touche = str(nb_touche)

    def __str__(self):
        return "Type: %s, Numéro de série: %s, Nombre de touches: %s" % (self.type, self.num_serie, self.nb_touche)
    
class Ecran(Materiel):
    def __init__(self, type, num_serie, taille):
        Materiel.__init__(self, type, num_serie)
        self.taille = taille

    def __str__(self):
        return "Type: %s, Numéro de série: %s, Taille: %s" % (self.type, self.num_serie, self.taille)
    
class PC(Materiel):
    def __init__(self, type, num_serie, ecran, clavier):
        Materiel.__init__(self, type, num_serie)
        self.ecran = ecran
        self.clavier = clavier

    def __str__(self):
        return "Type: %s, Numéro de série: %s, Ecran: %s, Clavier: %s" % (self.type, self.num_serie, self.ecran, self.clavier)    
    
    #sauvegarder la configuration du PC dans un fichier texte
    def saveConfig(self):
        #save as type of pc .txt  
        fichier = open(self.type + ".txt", "w")
        fichier.write("Materiel : " + self.type + "[" + self.num_serie + "]\n")
        fichier.write("Matériel : " + self.ecran.type + "[" + self.ecran.num_serie + "]\n")
        fichier.write("* Taille : " + self.ecran.taille + "\n")
        fichier.write("Matériel : " + self.clavier.type + "[" + self.clavier.num_serie + "]\n")
        fichier.write("* Nombre de touches : " + self.clavier.nb_touche + "\n")
        fichier.close()

    def loadConfig(self):
        fichier = open(self.type + ".txt", "r")
        print(fichier.read())
        fichier.close()

def exercice3():
    materiel = Materiel("materiel1", "123456789")
    clavier = Clavier("clavier123", "7594293", 100)
    ecran = Ecran("écran456", "987654321", "105 x 75 cm")
    pc = PC("pc666", "69420", ecran, clavier)
    pc.saveConfig()
    pc.loadConfig() 
