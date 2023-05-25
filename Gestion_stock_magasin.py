ordinateurs = []

def ajouter_ordinateur(marque, quantite, prix):
    nouvel_ordinateur = {
        'marque': marque,
        'quantite': quantite,
        'prix': prix
    }
    ordinateurs.append(nouvel_ordinateur)
    print("Ordinateur ajouté avec succès.")

def afficher_liste_ordinateurs():
    print("Liste des ordinateurs :")
    for i, ordinateur in enumerate(ordinateurs, 1):
        print(f"{i}. {ordinateur['marque']} - Quantité : {ordinateur['quantite']} - Prix : {ordinateur['prix']}")

def afficher_details_ordinateur(id):
    if id >= 1 and id <= len(ordinateurs):
        ordinateur = ordinateurs[id - 1]
        print("Détails de l'ordinateur :")
        print(f"Marque : {ordinateur['marque']}")
        print(f"Quantité : {ordinateur['quantite']}")
        print(f"Prix : {ordinateur['prix']:.2f}")
    else:
        print("ID d'ordinateur invalide.")

def modifier_stock_ordinateur(id, quantite):
    if id >= 1 and id <= len(ordinateurs):
        ordinateurs[id - 1]['quantite'] = quantite
        print("Stock modifié avec succès.")
    else:
        print("ID d'ordinateur invalide.")

def afficher_menu_principal():
    print("Menu Principal")
    print("1. Ajouter un nouvel ordinateur")
    print("2. Afficher la liste des ordinateurs")
    print("3. Afficher les détails d'un ordinateur")
    print("4. Modifier le stock d'un ordinateur")
    print("5. Autres opérations...")
    print("6. Quitter")
    choix = int(input("Choix : "))
    return choix

# Boucle principale du programme
while True:
    choix = afficher_menu_principal()
    
    if choix == 1:
        marque = input("Marque de l'ordinateur : ")
        quantite = int(input("Quantité : "))
        prix = float(input("Prix : "))
        ajouter_ordinateur(marque, quantite, prix)
    elif choix == 2:
        afficher_liste_ordinateurs()
    elif choix == 3:
        id = int(input("ID de l'ordinateur : "))
        afficher_details_ordinateur(id)
    elif choix == 4:
        id = int(input("ID de l'ordinateur : "))
        quantite = int(input("Nouvelle quantité : "))
        modifier_stock_ordinateur(id, quantite)
    elif choix == 5:
        # Autres opérations...
        pass
    elif choix == 6:
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")
