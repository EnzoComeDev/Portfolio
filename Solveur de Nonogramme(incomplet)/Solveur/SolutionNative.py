#############################################
# Solveur de nonogramme NATIF NON OPTIMISER #
# MADE BY ENZO CÔME AND NICOLAS LE GALVIC   #
#   PROJET SCOLAIRE L1 INFO - 2023 2024     #
#############################################
'''
Cette solution native consiste à généré aléatoirement des grilles 
respectant la taille indiquer et procède ensuite à une vérification des indices
CE PROGRAMME N'EST PAS OPTIMAL !
Par exemple après compilation sur un nonogramme 5 par 5 on a obtenu comme résultats : 
1ère essai : 5 160 763 Tentatives
2ème essai : 27 315 654 Tentatives
3ème essai : 4 249 370 Tentatives
'''

import random

def verifier_nonogramme(grille, indices_lignes, indices_colonnes):
    #Vérifie si les lignes respectent les indices
    def verifier_indices_lignes(grille, indices_lignes):
        for idx, lignes in enumerate(grille):
            indices_tempo_ligne = []
            compteur = 0
            for case in lignes:
                if case:
                    compteur += 1
                else:
                    if compteur != 0:
                        indices_tempo_ligne.append(compteur)
                        compteur = 0
            if compteur != 0:
                indices_tempo_ligne.append(compteur)
            if indices_tempo_ligne != indices_lignes[idx]:
                return False
        return True

    def verifier_indices_colonnes(grille, indices_colonnes):
        for j in range(len(grille[0])):
            indices_tempo_colonne = []
            compteur = 0
            for i in range(len(grille)):
                if grille[i][j]:
                    compteur += 1
                else:
                    if compteur != 0:
                        indices_tempo_colonne.append(compteur)
                        compteur = 0
            if compteur != 0:
                indices_tempo_colonne.append(compteur)
            if indices_tempo_colonne != indices_colonnes[j]:
                return False
        return True

    lignes_valides = verifier_indices_lignes(grille, indices_lignes)
    colonnes_valides = verifier_indices_colonnes(grille, indices_colonnes)
    return lignes_valides and colonnes_valides

def generer_grille_aleatoirement(nb_lignes, nb_colonnes):
    #Génère une grille aléatoirement avec des True et des False
    grille = []
    for _ in range(nb_lignes):
        ligne = [random.choice([True, False]) for _ in range(nb_colonnes)]
        grille.append(ligne)
    return grille

lignes = 3
colonnes = 3 
indices_lignes = [[2],[1],[1]]
indices_colonnes = [[2],[1],[1]] #Permet à la compilation (à modifier en conséquence)

def ResolNative(indices_lignes,indices_colonnes):
    grille_gen = generer_grille_aleatoirement(lignes,colonnes)
    tentative = 0
    #Tant que le programme ne trouve pas la solution , il re-génère des grilles
    while not(verifier_nonogramme(grille_gen,indices_lignes,indices_colonnes)):
        grille_gen = generer_grille_aleatoirement(lignes,colonnes)
        tentative +=1
    print("La grille a été trouver au bout de la tentative n°",tentative)
    print("Solution : " , grille_gen)

ResolNative(indices_lignes,indices_colonnes)