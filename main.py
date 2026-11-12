ls = []
print("==== GESTION DES TACHES ====")

ch = -1

while ch != 0:
    print("\n1. Ajoute une tache   2. Afficher   3. Rechercher   0. Quitter")
    ch = int(input("Votre choix: "))

    if ch == 1:
        titre = input("Donner le titre: ")
        if titre == "":
            print("Erreur: le titre est vide")
        else:
            ls.append(titre)
            print("Tâche ajoutée avec succès!")

    elif ch == 2:
        print("Liste des tâches:", ls)

    elif ch == 3:
        titre_rech = input("Donner le titre a rechercher: ")
        if titre_rech in ls:
            print("Le titre existe!")
        else:
            print("Le titre n'existe pas.")

    elif ch == 0:
        print("Au revoir!")

    else:
        print("Erreur: choix invalide")
