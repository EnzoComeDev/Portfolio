# 🧩 **Solveur de Nonogrammes**

## 📌 **Présentation**

Ce projet consiste à développer un **solveur de nonogrammes** en Python.  
Il a été réalisé dans le cadre d’un **projet universitaire de L1 Informatique (2023–2024)**.

L’objectif était de comparer une approche **naïve aléatoire** avec une approche **logique plus structurée**, afin de mieux comprendre les contraintes et la complexité des nonogrammes.

---

## 👥 **Auteurs**

- **Enzo Côme**
- **Nicolas Le Galvic**

---

## 🎯 **Objectifs**

- Comprendre le fonctionnement des nonogrammes  
- Implémenter différentes stratégies de résolution  
- Comparer performances et limites des approches  
- Appliquer des règles logiques de déduction  

---

## 📁 **Structure**

- SolutionNative.py # Solveur aléatoire non optimisé
- Solveur.py # Solveur logique (partiel)

---

## 🎲 **Solveur natif — SolutionNative.py**

Ce solveur génère des grilles **aléatoirement** jusqu’à trouver une solution correspondant aux indices.

- Approche simple mais très coûteuse
- Nombre de tentatives extrêmement élevé
- Utilisé comme point de comparaison 

---

## 🧠 **Solveur logique — Solveur.py**

Ce solveur repose sur des **règles logiques** :

- Résolution triviale par lignes et colonnes  
- Remplissage automatique des cases certaines  
- Déductions basées sur les contraintes restantes  

⚠️ Le solveur est **partiel**, mais permet de résoudre des **nonogrammes simples**.

---
