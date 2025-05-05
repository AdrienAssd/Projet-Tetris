######################################################
########### PROGRAMME PYTHON PROJET TETRIS ###########
########### REALISÉ PAR ADRIEN ASSOUAD ET  ###########
########### JULIEN RAFALIMANANA--CHAN PENG ###########
###########           VERSION 1.0          ###########
######################################################


from Fonctions import *
from Blocs import *

if __name__ == '__main__':
    forme = 0
    print("-Commencer à jouer (1)\n-Afficher les règles du jeu (2)")
    choix_utilisateur = int(input("Saisir 1 ou 2\n"))

    while choix_utilisateur != 2 and choix_utilisateur != 1:
        choix_utilisateur = int(input("Saisir 1 ou 2\n"))
    if choix_utilisateur == 2:
        print_game_rules()
        choix_utilisateur = int(input("Saisir 1\n"))
        clear()
    else : #for case 1
        clear()
        print("MODE DE JEU")

    taille_plateau = int(input("choisir la dimension du plateau\n (au moins 21 et au plus 26): "))
    while taille_plateau < 21 or taille_plateau > 27:
        taille_plateau = int(input("choisir la dimension du plateau\n (au moins 21 et au plus 26): "))
    choix_forme = input("Choisir la forme du plateau : Cercle (C), Losange (L), Triangle (T)\n")
    while choix_forme != "C" and choix_forme != "L" and choix_forme != "T":
        choix_forme = input("Choisir la forme du plateau : Cercle (C), Losange (L), Triangle (T)\n")


    choix_grid(choix_forme, taille_plateau)
    # Cree le plateau de jeu
    grid = initialisation_grid(choix_forme, taille_plateau)
    path = choix_path(choix_forme)
    save_grid(path, grid)
    forme = form(path)
    essais = 0
    while essais <3:
        bloc_3 = choice_bloc_3(grid,forme)
        j = choix_user_case_h()
        i = choix_user_case_v()
        if postionnement(grid, bloc_3, i, j) == False:
            essais +=1
            print("position invalide")
        else:
            essais = 0
        update_score(grid)
    print("Vous avez perdu")
""" - choisir taille et le plateau 
    - ensuite afficher tous les blocs
    - afficher 3 blocs sélectionner 
    - demander à l'utilisateur de choisir entre les 3 blocs
    - verifier si coordonner valides 
    - verifier si ligne et colonnes pleines
    - annulation des lignes et scores"""