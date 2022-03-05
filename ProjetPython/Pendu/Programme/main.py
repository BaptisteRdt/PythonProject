##importation des librairies 
import string
import mef
import random


##fonctions et procédures
def partie_finie():
    if ensemble_lettre_phrase_cachee.__len__() != ensemble_lettre.__len__():
        return True
    return False 

def chiffre_aleatoire():
    return random.randrange(0, 12, 1)

##déclarations des variables
liste_phrases_pendu = [
    "league of legends n'est pas un jeu sain",
    "il faut regarder breaking bad, vraiment",
    "c'est une mauvaise idee de lancer tft en cours!",
    "rejoignez notre ecole pour apprendre a faire ca",
    "ceci est un pendu, et oui c'etait simple!",
    "je suis grand champion sur rocket league",
    "bonne continuation dans la journee porte ouverte",
    "l'iut du limousin est le meilleur pour l'info",
    "le bac c'est dans la poche en juin!",
    "ce programme a ete realise par baptiste, oui je signe mon code",
    "anticonstitutionnellement, ce mot est long",
    "zygotique, c'est simple non?",
    "l'embryon est haploide car la cellule est divisee"
]
phrase_cachee = liste_phrases_pendu[chiffre_aleatoire()]
fin_partie = True
nombre_de_vie = 8
lettre_input = "*"
ensemble_lettre_phrase_cachee = set()
ensemble_lettre = set()



##programme principal
for i in phrase_cachee:
    if i != "'" and i != ' ' and i != '!' and i != '?' and i != ',':
        ensemble_lettre_phrase_cachee.add(i)


##boucle du jeu 
while fin_partie and nombre_de_vie != 0:
    
    ##affichage de la potence
    if nombre_de_vie == 8:
        mef.potence8()
    elif nombre_de_vie == 7:
        mef.potence7()
    elif nombre_de_vie == 6:
        mef.potence6()
    elif nombre_de_vie == 5:
        mef.potence5()
    elif nombre_de_vie == 4:
        mef.potence4()
    elif nombre_de_vie == 3:
        mef.potence3()
    elif nombre_de_vie == 2:
        mef.potence2()
    elif nombre_de_vie == 1:
        mef.potence1()

    mef.mise_en_forme()

    ##affichage de la phrase cachée
    for i in phrase_cachee:
        if ensemble_lettre.__contains__(i) or i=="'" or i==" " or i == '!' or i == '?' or i == ',':
           print(i, end="")
        else:
           print("_", end="") 

    mef.mise_en_forme()

    ##saisie de la lettre de l'utilsateur 
    while True:
        lettre_input = (input("Saisir une lettre : "))
        if lettre_input in string.ascii_lowercase:
            break
        else:
            print("Erreur de saisie")


    ##vérification de la lettre saisie
    # 
    ##la lettre est dans la phrase cachée
    if ensemble_lettre_phrase_cachee.__contains__(lettre_input):
        ##la lettre a déjà été saisie 
        if ensemble_lettre.__contains__(lettre_input):
            print("Lettre deja saisie, dommage -1 <3")
            nombre_de_vie -= 1
        ##la lettre n'a pas été saisie, on l'ajoute à ensemble_lettre
        else: 
            ensemble_lettre.add(lettre_input)
    ##la lettre n'est pas dans la phrase cachée
    else:
        print(lettre_input + " n'est pas dans la phrase cachee, dommage -1 <3")
        nombre_de_vie -= 1
        


    ##test
    #print(ensemble_lettre)
    #print(ensemble_lettre_phrase_cachee)
    #
    #print(nombre_de_vie)
    ##

    ##vérification de fin de partie 
    fin_partie = partie_finie()

    mef.mise_en_forme()

##fin de la boucle et du jeu, affichage de la victoire ou de la défaite
if nombre_de_vie < 1:
    print(mef.potenceFinale())
    print(mef.mise_en_forme_defaite())
else:
    print("Bravo la phrase etait : " + phrase_cachee)
    print(mef.mise_en_forme_victoire())
