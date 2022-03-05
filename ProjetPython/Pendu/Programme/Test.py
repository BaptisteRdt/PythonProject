phrase_cachee = "j'ai le mort putain"
fin_partie = True
lettre_input = "*"
ensemble_lettre_phrase_cachee = set()
ensemble_lettre = set()

for i in phrase_cachee:
    if i != '\'' or i != ' ' or i != '!' or i != '?':
        ensemble_lettre_phrase_cachee.add(i)


while fin_partie:
    for i in phrase_cachee:
        if ensemble_lettre.__contains__(i) > 0 or i=="'" or i==" ":
           print(i, end="")
        else:
           print("_", end="")
    
    print("Saisir une lettre : ", end="")
    lettre_input=input()

    if ensemble_lettre.__contains__(lettre_input):
        print("Lettre deja saisie, dommage -1 <3")
    else: 
        ensemble_lettre.add(lettre_input)

    print(ensemble_lettre)                              #problème pour la vérif de fin 
    print(ensemble_lettre_phrase_cachee)                #l'ensemble possède ' ', "'", or il ne faut pas 
    if ensemble_lettre == ensemble_lettre_phrase_cachee:
        fin_partie=False