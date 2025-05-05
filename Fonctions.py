import os
import random
from Blocs import *
from math import *


# FONCTIONS ACCUEIL

# efface tout ce qui est afficher sur la console
def clear():
    os.system('clear')  # pour Windows os.system('cls')


# affiche les règles du jeu
def print_game_rules():
    print("REGLES DU JEU : \n Il s’agit de partir d’un plateau à 2 dimensions de taille minimum 21 x 21 cases"
          "\n - dont les lignes sont désignées par des lettres majuscules (‘A’, ‘B’ ...) "
          "et les colonnes par des lettres minuscules (‘a’, ‘b’, ...)"
          "\n - sur lequel sera délimitée une surface de jeu valide. "
          "Cette surface de jeu valide peut prendre trois formes différentes : cercle, losange ou triangle."
          "\n Dans ce jeu, l’utilisateur dispose d’un ensemble de blocs qu’il devra placer tour à tour sur "
          "la surface valide du plateau en saisissant les coordonnées de l’endroit où il veut les insérer."
          "\n Certains blocs à poser sont communs aux trois formes, mais à chacune d’entre elles d’autres formes "
          "plus adaptées peuvent s’ajouter")


# FONCTIONS PLATEAUX DE JEU

# Affiche la grille
def read_grid(path):
    grid = []
    with open(path, "r") as f:
        ligne = f.readlines()
        while ligne != "":
            L = []
            for ch in ligne:
                if ch != " " and ch != "\n":
                    L.append(ch)
            grid.append(L)
            ligne = f.readlines()
    return grid


# Sauvegarde la grille dans le fichier grid
def save_grid(path, grid):
    with open(path, "w") as f:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                f.write(str(grid[i][j]))
                if j == len(grid[i]) - 1:
                    f.write("\n")
                else:
                    f.write(" ")


# création de la grille
def initialisation_grid(choix_forme, taille_plateau):
    grid = []
    if choix_forme == "C":
        if taille_plateau % 2 != 0:
            for i in range(taille_plateau // 2):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 4 - i) and j <= (3 * taille_plateau // 4 + i):
                        L[j] = 1
                grid.append(L)
            for i in range(taille_plateau // 2, -1, -1):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 4 - i) and j <= (3 * taille_plateau // 4 + i):
                        L[j] = 1
                grid.append(L)
        if taille_plateau % 2 == 0:
            for i in range(taille_plateau // 2):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 4 - i) and j <= (3 * taille_plateau // 4 + i):
                        L[j] = 1
                grid.append(L)
            for i in range(taille_plateau // 2 - 1, -1, -1):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 4 - i) and j <= (3 * taille_plateau // 4 + i):
                        L[j] = 1
                grid.append(L)
    if choix_forme == "L":
        if taille_plateau % 2 == 0:
            for i in range(taille_plateau // 2):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 2 - i) and j <= (taille_plateau // 2 + i):
                        L[j] = 1
                grid.append(L)
            for i in range(taille_plateau // 2 - 1, -1, -1):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 2 - i) and j <= (taille_plateau // 2 + i):
                        L[j] = 1
                grid.append(L)
        if taille_plateau % 2 != 0:
            for i in range(taille_plateau // 2 + 1):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 2 - i) and j <= (taille_plateau // 2 + i):
                        L[j] = 1
                grid.append(L)
            for i in range(taille_plateau // 2 - 1, -1, -1):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 2 - i) and j <= (taille_plateau // 2 + i):
                        L[j] = 1
                grid.append(L)
    if choix_forme == "T":
        if taille_plateau % 2 != 0:
            for i in range((taille_plateau // 2) + 1):
                L = [0] * taille_plateau
                for j in range(taille_plateau):
                    if j >= (taille_plateau // 2 - i) and j <= (taille_plateau // 2 + i):
                        L[j] = 1
                grid.append(L)
        else:
            if taille_plateau % 2 == 0:
                for i in range(taille_plateau // 2):
                    L = [0] * taille_plateau
                    for j in range(taille_plateau):
                        if j >= (taille_plateau // 2 - i) and j <= (taille_plateau // 2 + i):
                            L[j] = 1
                    grid.append(L)
    return grid


# affiche tout les blocs de la liste
def print_line_of_bloc_list(L, line):
    for bloc in L:
        print("         ", end='')
        for j in range(len(bloc[line])):
            if bloc[line][j] == 1:
                print("■", end=" ")
            else:
                print(" ", end=" ")
    print("")


# retourne une copie de la liste complete de blocs
def complete_list_of_bloc(copie_liste_bloc):
    maximum_length = 5
    for bloc in copie_liste_bloc:
        for i in range(maximum_length - len(bloc)):
            bloc.insert(0, [0 for element in range(len(bloc[0]))])
    return copie_liste_bloc


# Affiche la grille et les blocs sur le coté
def print_grid_bloc(grid, copie_liste_bloc, forme):
    grille = []
    for i in range(len(grid)):
        grille.append([])
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                grille[i].append("■")
            elif grid[i][j] == 1:
                grille[i].append("□")
            elif grid[i][j] == 0:
                grille[i].append(".")

    print("    ", end="")
    for i in range(len(grille[0])):
        print(alphabet_maj[i], end=" ")
    print()
    print("  ╔", end=" ")
    for i in range(len(grille[0])):
        print("═", end=" ")
    print("╗")
    # Complete list a bloc to facilitate the printing
    list_bloc_complete = complete_list_of_bloc(copie_liste_bloc)

    for i in range(len(grille)):
        print(alphabet_min[i], "║", *grille[i], sep=" ", end=" ║")
        if i == len(grille) // 4:
            print("     -Score-", update_score(grid))
        elif i >= len(grille) // 3 and i < (len(grille) // 3) + 5:
            print_line_of_bloc_list(list_bloc_complete, i - len(grille) // 3)
        elif i == (len(grille) // 3) + 6:
            [print("         ", i, "   ", end='') for i in range(1, 4)]
            print("")
        else:
            print("")

    print("  ╚ ", end="")
    for i in range(len(grille[0])):
        print("═", end=" ")
    print("╝\n")


# attribut une forme suivant le plateau
def form(path):
    forme = 0
    if path == "cercle.txt":
        forme = 1
        print("Le plateau est un cercle")
    elif path == "losange.txt":
        forme = 2
        print("Le plateau est un losange")
    elif path == "triangle.txt":
        forme = 3
        print("Le plateau est un triangle")
    return forme


# suivant le plateau choisi et la taille la fonction va appeler la fonction initialisation_grid qui créera la grille
def choix_grid(choix_forme, taille_plateau):
    if choix_forme == "C":
        initialisation_grid(choix_forme, taille_plateau)
    if choix_forme == "L":
        initialisation_grid(choix_forme, taille_plateau)
    if choix_forme == "T":
        initialisation_grid(choix_forme, taille_plateau)


# suivant la forme choisie un fichier.txt est attribué à la variable path
def choix_path(choix_forme):
    if choix_forme == "C":
        path = "cercle.txt"
    if choix_forme == "L":
        path = "losange.txt"
    if choix_forme == "T":
        path = "triangle.txt"
    return path


# FONCTIONS BLOCS

# affiche un bloc
def print_bloc(bloc):
    for i in range(len(bloc)):
        for j in range(len(bloc[i])):
            if bloc[i][j] == 1:
                print("■", end=" ")
            else:
                print(".", end=" ")
        print(" ")
    print()


# affihce tous les blocs
def print_all_blocs():
    for i in range(len(ensemble_blocs)):
        for bloc in range(len(ensemble_blocs[i])):
            print_bloc(ensemble_blocs[i][bloc])


# affiche tous les blocs d'une forme
def print_blocs_liste(path):
    forme = 0
    for i in range(len(ensemble_blocs[forme])):
        print_bloc(ensemble_blocs[forme][i])
    if path == "cercle.txt":
        forme = 1
    elif path == "losange.txt":
        forme = 2
    elif path == "triangle.txt":
        forme = 3
    for i in range(len(ensemble_blocs[forme])):
        print_bloc(ensemble_blocs[forme][i])


# choisis un bloc au hasard en fonction de la forme
def random_select_bloc(forme):
    alea = 0
    if forme == 0:
        alea = random.randint(0, 19)
    elif forme == 1:
        alea = random.randint(0, 11)
    elif forme == 2:
        alea = random.randint(0, 13)
    elif forme == 3:
        alea = random.randint(0, 10)
    return select_bloc(forme, alea)


# sélectionne un bloc
def select_bloc(forme, num_bloc):
    return ensemble_blocs[forme][num_bloc]


# choisis trois blocs aléatoirement
def choice_bloc_3(grid, forme):
    L = []
    for i in range(3):
        f = random.choice([forme, 0])
        L.append(random_select_bloc(f))
    print_grid_bloc(grid, L, forme)
    choix_bloc = int(input("choisir un bloc entre 1 et 3 "))
    while choix_bloc < 1 or choix_bloc > 3:
        choix_bloc = int(input("choisir un bloc entre 1 et 3 "))
    return clean_row_empty(L[choix_bloc - 1])


# nettoies les lignes vides
def clean_row_empty(bloc):
    while sum(bloc[0]) == 0:
        bloc.remove(bloc[0])
    return bloc


# demande à l'utilisateur de choisir une valeur pour la ligne ou il veut poser son bloc
def choix_user_case_h():
    choix_case_h = input("choisir une lettre entre A et Z ")
    while choix_case_h < "A" or choix_case_h > "Z":
        choix_case_h = input("choisir une lettre entre A et Z ")
    for i in range(len(alphabet_maj)):
        if choix_case_h == alphabet_maj[i]:
            ind_h = i
    return ind_h


# demande à l'utilisateur de choisir une valeur pour la colonne ou il veut poser son bloc
def choix_user_case_v():
    choix_case_v = input("choisir une lettre entre a et z ")
    while choix_case_v < "a" or choix_case_v > "z":
        choix_case_v = input("choisir une lettre entre a et z ")
    for i in range(len(alphabet_min)):
        if choix_case_v == alphabet_min[i]:
            ind_v = i
    return ind_v


# FONCTIONS POSITIONNEMENT

# Test si l'emplacement est vide ou non
def valid_position(grid, bloc, i, j):
    for a in range(len(bloc)):
        for b in range(len(bloc[a])):
            if bloc[a][b] == 1 and grid[i + a][j + b] != 1 or (len(bloc) + i) > len(grid) or (len(bloc[a]) + j) > len(
                    grid[0]):
                return False
    return True


# change les valeurs de 1 par 2 quand un bloc est positionné aux emplecements du bloc
def emplace_bloc(grid, bloc, i, j):
    for a in range(len(bloc)):
        for b in range(len(bloc[a])):
            if bloc[a][b] == 1:
                grid[i + a][j + b] = 2
    return grid


# s'occupe de positionner les blocs une fois que la position est valide
def postionnement(grid, bloc, i, j):
    if valid_position(grid, bloc, i, j) == True:
        emplace_bloc(grid, bloc, i, j)
        return True
    return False


# ANNULATION DE LIGNES/COLONNES ET CALCUL DU SCORE

# Verifie si toute la ligne(i) est remplie
def row_state(grid, i):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            return False
    return True


# Verifie si toute la colonne(j) est remplie
def col_state(grid, j):
    for i in range(len(grid)):
        if grid[i][j] == 1:
            return False
    return True


# annule la ligne i une fois que celle-ci est pleine et abaisse les lignes du dessus une fois que la ligne est annulée et prend en compte les points gagnés
def row_clear(grid, i):
    if row_state(grid, i) == True:
        score = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                score += 1
        for colonne in range(len(grid[i])):
            for ligne in range(i, 0, -1):
                if grid[ligne][colonne] == 0:
                    grid[ligne][colonne] = 0
                elif (grid[ligne][colonne] == 1 or grid[ligne][colonne] == 2) and grid[ligne - 1][colonne] == 2:
                    grid[ligne][colonne] = 2
                # Case where actual is 2 and 1 is above, 2 and 0, 1 and 0
                else:
                    grid[ligne][colonne] = 1
        for i in range(len(grid[0])):
            if grid[0][i] == 2:
                grid[0][i] = 1
        return score


# annule la colonne j de la grille et prend en compte les points gagnés
def col_clear(grid, j):
    if col_state(grid, j) == True:
        score = 0
        for i in range(len(grid)):
            if grid[i][j] == 2:
                grid[i][j] = 1
                score += 1
        return score


# met à jour le score du joueur
score = 0


def update_score(grid):
    global score
    for i in range(len(grid)):
        if row_state(grid, i) == True:
            x = row_clear(grid, i)
            score += x
        for j in range(len(grid[i])):
            if col_state(grid, j) == True:
                x = col_clear(grid, j)
                score += x
    return score
