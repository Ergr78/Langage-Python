joueurX = 0
joueurY = 0
tresorX = 3
tresorY = 2
tresorTrouve = False

objetsTrouves = [
    "�p�e",
    "Armure",
    "Potion de soin",
    "Cl�",
    ""
]

while not tresorTrouve:
    print("Vous �tes aux coordonn�es ({}, {}).".format(joueurX, joueurY))

    if joueurX == tresorX and joueurY == tresorY:
        print("Vous avez trouv� le tr�sor !")
        tresorTrouve = True
        break

    print("Que voulez-vous faire ?")
    print("1. Aller vers le nord")
    print("2. Aller vers l'est")
    print("3. Aller vers le sud")
    print("4. Aller vers l'ouest")
    choix = int(input("Votre choix : "))

    if choix == 1:
        joueurY += 1
    elif choix == 2:
        joueurX += 1
    elif choix == 3:
        joueurY -= 1
    elif choix == 4:
        joueurX -= 1
    else:
        print("Choix invalide !")

print("Objets trouv�s :")
for objet in objetsTrouves:
    if objet != "":
        print("- {}".format(objet))

