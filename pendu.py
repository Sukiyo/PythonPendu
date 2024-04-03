import random

# Création liste de mots

mots = ["princesse", "souris", "amis", "chateau", "films", "disney"]

# Fonction pour choisir un mot aléatoire dans la liste
def choisir_mot():
    return random.choice(mots)

# Fonction pour afficher le mot partiellement découvert
def afficher_mot(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre
        else:
            mot_affiche += "_"
    return mot_affiche

# Fonction pour afficher le bonhomme pendu
def afficher_bonhomme(chances_restantes):
    bonhomme = [
        "  _______     ",
        " |/      |    ",
        " |      (_)   ",
        " |      /|\   ",
        " |       |    ",
        " |      / \   ",
        " |            ",
        "_|___         "
    ]
    for i in range(7 - chances_restantes):
        print(bonhomme[i])

# Fonction pour jouer au jeu du pendu
def jouer_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = []
    chances_restantes = 7

    print("Bienvenue au jeu du pendu!")
    print("Le mot à deviner contient", len(mot_a_deviner), "lettres.")

    while chances_restantes > 0:
        print("\nMot à deviner :", afficher_mot(mot_a_deviner, lettres_trouvees))
        afficher_bonhomme(chances_restantes)

        try:
            lettre = input("Entrez une lettre : ").lower()  # Convertit l'entrée en minuscules
            if not lettre.isalpha():
                raise ValueError("L'entrée n'est pas une lettre.")
        except ValueError as ve:
            print("Erreur :", ve)
            continue

        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
            continue
        
        if lettre in mot_a_deviner:
            lettres_trouvees.append(lettre)
            if len(set(mot_a_deviner)) == len(lettres_trouvees):
                print("Félicitations! Vous avez deviné le mot :", mot_a_deviner)
                break
            else:
                print("Bien joué! Cette lettre est dans le mot.")
        else:
            print("Désolé, cette lettre n'est pas dans le mot.")
            chances_restantes -= 1
            print("Chances restantes :", chances_restantes)
    
    if chances_restantes == 0:
        print("\nDésolé, vous avez épuisé toutes vos chances. Le mot était :", mot_a_deviner)
        afficher_bonhomme(chances_restantes)

# Appel de la fonction pour jouer au jeu du pendu
jouer_pendu()
