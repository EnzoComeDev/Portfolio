import copy# Permet de copier sans bug la grille
'''
   Programme pour la compétition 
   Enzo Côme | Nicolas Le Galvic

   La fonction solveur() se charge
   d'effectuer tout le programme 
   elle ouvre le fichier puis le traite
   et renvoie le fichier output

   Ligne avec le nom du fichier 266 
'''

def RecupFichierCouleur():

    fichier_entre = 'nonogramInput.txt'

    with open(fichier_entre, 'r') as fichier:
        mode = None
        nb_lignes_classique = None
        nb_lignes_couleur = None
        nb_colonnes_classique = None
        nb_colonnes_couleur = None
        nb_couleurs = None
        couleurs = []
        indices_lignes_classique = []
        indices_lignes_couleur = []
        indices_colonnes_classique = []
        indices_colonnes_couleur = []

        for ligne in fichier:
            partie = ligne.strip().split()

            if len(partie) == 0:  # Ignorer les lignes vides
                continue

            if len(partie) == 1:  # Vérifier le mode
                if '_' in partie[0]:
                    mode, dimensions = partie[0].split('_')
                    if mode == 'classique':
                        nb_lignes_classique, nb_colonnes_classique = map(int, dimensions.split('x'))
                    elif mode == 'couleur':
                        nb_lignes_couleur, nb_colonnes_couleur, nb_couleurs = map(int, dimensions.split('x'))
                elif len(partie[0].split('=')) == 2:  # Traiter les informations de couleur
                    couleur_numero, couleur_code = partie[0].split('=')
                    couleurs.append((int(couleur_numero), couleur_code))
            else:  # Traiter les indices
                if partie[0].startswith('L'):
                    if mode == 'classique':
                        indices_lignes_classique.append([int(x) for x in partie[1:]])
                    elif mode == 'couleur':
                        indices_ligne = []
                        for i in range(1, len(partie)):
                            index = int(partie[i])
                            autres_infos = partie[i]
                            indices_ligne.append((index, autres_infos))
                        indices_lignes_couleur.append(indices_ligne)
                elif partie[0].startswith('C'):
                    if mode == 'classique':
                        indices_colonnes_classique.append([int(x) for x in partie[1:]])
                    elif mode == 'couleur':
                        indices_colonne = []
                        for i in range(1, len(partie)):
                            index = int(partie[i])
                            autres_infos = partie[i]
                            indices_colonne.append((index, autres_infos))
                        indices_colonnes_couleur.append(indices_colonne)
    #print("Nombre de lignes classiques:", nb_lignes_classique)
    #print("Nombre de lignes couleur:", nb_lignes_couleur)
    #print("Nombre de colonnes classiques:", nb_colonnes_classique)
    #print("Nombre de colonnes couleur:", nb_colonnes_couleur)
    #print("Nombre de couleurs:", nb_couleurs)
    #print("Couleurs:", couleurs)
    #print("Indices des lignes classiques:", indices_lignes_classique)
    #print("Indices des lignes couleur:", indices_lignes_couleur)
    #print("Indices des colonnes classiques:", indices_colonnes_classique)
    #print("Indices des colonnes couleur:", indices_colonnes_couleur)

def Solveur(): #Programe pour la compétition
    ''' Partie Résolution : '''

    def solution_trouver(grille):
        for ligne in grille:
            if None in ligne:
                return False
        return True
    def sauvegarde_grille(grille):
        return copy.deepcopy(grille)
    sauvegarde = [[]]
    def Resolution(indices_lignes, indices_colonnes, nb_lignes, nb_colonnes):
        grille = [[None for _ in range(nb_lignes)] for _ in range(nb_colonnes)]
        sauvegarde = [[]]
        while grille != sauvegarde:
            sauvegarde = sauvegarde_grille(grille)
            grille = resolution_trivial_ligne(grille, indices_lignes)
            grille = resolution_trivial_colonne(grille, indices_colonnes)
            grille = remplissage_false_ligne(grille,indices_lignes)
            grille = remplissage_false_colonne(grille,indices_colonnes)
            grille = remplir_obligatoire_colonne_true(grille,indices_colonnes)
            grille = remplir_obligatoire_ligne_true(grille,indices_lignes)
            grille = coloration_obligatoire_ligne(grille,indices_lignes)
            grille = coloration_obligatoire_colonne(grille,indices_colonnes)
        return grille

    #Resolution Trivial : 
    def resolution_trivial_ligne(grille, indice_lignes):
        for i, indices in enumerate(indice_lignes):
            if type(indices) == int:
                if indices == len(grille[0]):
                    grille[i] = [True] * len(grille[0])

            elif type(indices) == list:
                somme_indice = sum(indice_lignes[i])
                nb_indice = len(indice_lignes[i])
                if somme_indice + nb_indice - 1 == len(grille[0]):
                    for rang,indice in enumerate(indices):
                        for _ in range(indice):
                            grille[i][rang] = True
                        if rang < len(grille[0]):
                            grille[i][rang] = False

            if indices == [0]:
                grille[i] = [False] * len(grille[0])
        return grille
    
    def resolution_trivial_colonne(grille, indices_colonnes):
        for i, indices in enumerate(indices_colonnes):
            if type(indices) == int:
                if indices == len(grille):
                    for j in range(len(grille)):
                        grille[j][i] = True
            elif type(indices) == list:
                if sum(indices) + len(indices) - 1 == nb_colonnes:
                    rang = 0
                    for indice in indices:
                        for j in range(indice):
                            grille[j][rang] = True
                        rang += 1
                        if rang < len(grille):
                            grille[j][rang] = False
                        rang += 1
            if indices == [0]:
                for j in range(len(grille)):
                    grille[j][i] = False
        return grille
    
    #Fonction utilitaire : 
    def compter_false_ligne(grille, numero_de_ligne):
        return grille[numero_de_ligne].count(False)
    
    def compter_false_colonne(grille, numero_de_colonne):
        return sum(1 for ligne in grille if not(ligne[numero_de_colonne]))
    
    def compter_true_ligne(grille, numero_de_ligne):
        return sum(1 for case in grille[numero_de_ligne] if case)
    
    def compter_true_colonne(grille,numero_de_colonne):
        return sum(1 for ligne in grille if ligne[numero_de_colonne])
    
    def compter_none_ligne(grille, numero_de_ligne):
        return grille[numero_de_ligne].count(None)
    
    def compter_none_colonne(grille, numero_de_colonne):
        return sum(1 for ligne in grille if ligne[numero_de_colonne] is None)
    
    #Resolution obligatoire : 
    def remplissage_false_ligne(grille, indices_lignes):
        for i, indices in enumerate(indices_lignes):
            if type(indices) == list:
                indices = sum(indices)
            if compter_true_ligne(grille,i) == indices:
                for j in range(len(grille[i])):
                    if grille[i][j] == None:
                        grille[i][j] = False
        return grille

    def remplissage_false_colonne(grille, indices_colonnes):
        for j, indices in enumerate(indices_colonnes):
            if type(indices) == list:
                indices = sum(indices)
            if compter_true_colonne(grille, j) == indices:
                for i in range(len(grille)):
                    if grille[i][j] is None:
                        grille[i][j] = False
        return grille

    def coloration_obligatoire_ligne(grille,indices_lignes):
        nb_cases_total = len(grille)
        for rang , indice_ligne in enumerate(indices_lignes):
            if type(indice_ligne) == list:
                if len(indice_ligne) == 1:
                    indice_ligne = indice_ligne[0]
            if type(indice_ligne) == int:
                if indice_ligne >= nb_cases_total // 2 + nb_cases_total % 2: #Arrondi au suppérieur
                    debut_coloration =  nb_cases_total - indice_ligne
                    fin_coloration = nb_cases_total - (nb_cases_total - indice_ligne)
                    for j in range(debut_coloration,fin_coloration):
                        if grille[rang][j] == None:
                            grille[rang][j] = True
        return grille
    
    def coloration_obligatoire_colonne(grille, indices_colonnes):
        nb_cases_total = len(grille[0]) 
        for indice_colonne, indice in enumerate(indices_colonnes):
            if type(indice) == int and indice >= nb_cases_total // 2 + nb_cases_total % 2:  # Arrondi au supérieur
                debut_coloration = nb_cases_total - indice
                fin_coloration = nb_cases_total - (nb_cases_total - indice)
                for i in range(debut_coloration, fin_coloration):
                    if grille[i][indice_colonne] is None:
                        grille[i][indice_colonne] = True
        return grille
    
    #Resolution élaboré :
    def trouver_cases_disponibles_ligne(grille, numero_de_ligne):
        cases = []
        longueur_segment = 0
        for cellule in grille[numero_de_ligne]:
            if cellule is None:
                longueur_segment += 1
            else:
                if longueur_segment > 0:
                    cases.append(longueur_segment)
                    longueur_segment = 0
        if longueur_segment > 0:
            cases.append(longueur_segment)
        return cases
    
    def trouver_cases_disponibles_colonne(grille, numero_de_colonne):
        cases = []
        longueur_segment = 0
        for i in range(len(grille)):
            if grille[i][numero_de_colonne] is None:
                longueur_segment += 1
            else:
                if longueur_segment > 0:
                    cases.append(longueur_segment)
                    longueur_segment = 0
        if longueur_segment > 0:
            cases.append(longueur_segment)
        return cases
    
    def remplir_obligatoire_ligne_true(grille, indices_lignes):
        for ligne in range(len(grille[0])):
            case_dispo = trouver_cases_disponibles_ligne(grille,ligne)
            somme_indice = 0
            nb_true_ligne_liste = compter_true_ligne(grille,ligne)
            if type(indices_lignes[ligne]) == list:
                for indices in indices_lignes[ligne]:
                    somme_indice += indices
            elif type(indices_lignes[ligne]) == int:
                somme_indice = indices_lignes[ligne]
            if len(case_dispo) == 1:
                case_dispo = case_dispo[0]
            if type(nb_true_ligne_liste) == int:
                nb_true_ligne = nb_true_ligne_liste
            elif type(nb_true_ligne_liste) == list:
                nb_true_ligne = sum(nb_true_ligne_liste)
            if type(case_dispo) == list:
                case_dispo = sum(case_dispo)
            if case_dispo + nb_true_ligne == somme_indice:
                for i in range(len(grille[0])):
                    if grille[ligne][i] == None:
                        grille[ligne][i] = True
            somme_indice = 0
        return grille
    
    def remplir_obligatoire_colonne_true(grille, indices_colonnes):
        for colonne in range(len(grille)):
            somme_indice = 0
            nb_true_colonne_liste = compter_true_colonne(grille, colonne) #Peut renvoyer un entier !

            if type(indices_colonnes[colonne]) == list:
                for indices in indices_colonnes[colonne]:
                    somme_indice += indices
            elif type(indices_colonnes[colonne]) == int:
                somme_indice = indices_colonnes[colonne]
            case_dispo = trouver_cases_disponibles_colonne(grille, colonne)

            if type(case_dispo) == list:
                case_dispo = sum(case_dispo)

            if type(nb_true_colonne_liste) == int:
                nb_true_colonne = nb_true_colonne_liste
            elif type(nb_true_colonne_liste) == list:
                nb_true_colonne = sum(nb_true_colonne_liste)

            if case_dispo + nb_true_colonne == somme_indice:
                for i in range(len(grille)):
                    if grille[i][colonne] is None:
                        grille[i][colonne] = True
            somme_indice = 0
        return grille
    
    ''' Fin de partie Résolution '''

    ''' Partie Traitement du fichier et du nonogramme '''
    fichier_entre = 'nonogramInput2.txt'

    with open(fichier_entre, 'r') as fichier_lecture:
        with open("NonogramOuput2.txt", 'w') as fichier_sortie:
            print("Les deux fichiers ont été open avec succès !")

            line = fichier_lecture.readline().strip() #Contient la première ligne
            while line:
                if "classique_" in line:
                    premiere_ligne_nonogramme = line
                    indices_lignes = []
                    indices_colonnes = []

                    dimensions = line.split('_')[1].split('x') # Extraire les dimensions
                    nb_lignes = int(dimensions[0])
                    nb_colonnes = int(dimensions[1])

                elif line.startswith('L'):
                    valeurs_str = line.strip().split()[1:]
                    indice_tempo = [int(valeur) if valeur.isdigit() else 0 for valeur in valeurs_str]
                    indices_lignes.append(indice_tempo)

                elif line.startswith('C'):
                    valeurs_str = line.strip().split()[1:]
                    indice_tempo = [int(valeur) if valeur.isdigit() else 0 for valeur in valeurs_str]
                    indices_colonnes.append(indice_tempo)

                if len(indices_lignes) == nb_lignes and len(indices_colonnes) == nb_colonnes:
                    for i in range(len(indices_lignes)):
                        if not indices_lignes[i]:
                            indices_lignes[i] = [0] 
                    for i in range(len(indices_colonnes)):
                        if not indices_colonnes[i]:
                            indices_colonnes[i] = [0]
                    grille = Resolution(indices_lignes, indices_colonnes, nb_lignes, nb_colonnes)
                    fichier_sortie.write(premiere_ligne_nonogramme)
                    fichier_sortie.write("\n")
                    for ligne in grille:
                        for element in ligne:
                            if element:
                                fichier_sortie.write("X")
                            elif not(element):
                                fichier_sortie.write("O")
                            else:
                                fichier_sortie.write(".")
                        fichier_sortie.write("\n")

                    line = fichier_lecture.readline().strip()
                else:
                    line = fichier_lecture.readline().strip() 
                

                



    #print("Nombre de lignes :", nb_lignes)
    #print("Nombre de colonnes :", nb_colonnes)
    #print("Indices des lignes :", indices_lignes)
    #print("Indices des colonnes :", indices_colonnes)


    
def main():
    Solveur()
    print("Programme compilé avec succès !")

main()