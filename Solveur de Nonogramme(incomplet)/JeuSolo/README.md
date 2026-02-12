# Nonogram – Jeu de logique

Projet universitaire réalisé en L1 Informatique, développé en Python.

Ce projet consiste à implémenter un **jeu de nonogramme entièrement jouable**, avec génération de grilles et interface graphique.

---

## 🧩 Présentation

Un nonogramme est un jeu de logique basé sur une grille.
Le but est de remplir correctement les cases en respectant les indices numériques indiqués pour chaque ligne et chaque colonne.

---

## 🎯 Objectifs du projet

- Créer un **jeu de nonogramme fonctionnel**
- Générer des grilles jouables :
  - aléatoirement
  - à partir d’une image
- Calculer automatiquement les indices de lignes et de colonnes
- Proposer une interface graphique interactive

---

## 🛠️ Fonctionnalités

### ✔️ Modes de jeu
- Noir et blanc
- Couleur

### ✔️ Génération des grilles
- Génération aléatoire
- Génération à partir d’une image :
  - conversion en noir et blanc
  - conversion en couleurs à partir des valeurs RGB

### ✔️ Interface graphique
- Interface réalisée avec **Tkinter**
- Grille interactive cliquable
- Affichage dynamique des indices
- Choix de la taille de la grille
- Menu de navigation (nouvelle partie, recommencer, quitter)

### ✔️ Conditions de victoire
- Comparaison entre la grille du joueur et la grille solution
- Validation uniquement lorsque la solution est correcte

---

## 🧠 Aspects techniques

- Langage : **Python**
- Interface graphique : **Tkinter**
- Manipulation d’images : **Pillow (PIL)**
- Structures de données :
  - grilles sous forme de matrices 2D
  - listes d’indices pour lignes et colonnes
- Logique :
  - génération des indices
  - transformation image → grille de jeu
  - vérification de la victoire


