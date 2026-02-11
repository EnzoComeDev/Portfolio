# 🐢 Interpréteur Turtl

## 📋 Contexte

Projet de **compilation** en 3ème année d'informatique - Université d'Angers  
**Objectif :** Créer un interpréteur complet pour un langage de contrôle de tortues graphiques
(détail : https://leria-info.univ-angers.fr/~fabien.garreau/enseignements/compilation/Projet_2025-2026/turtl.php)

**Exemple de code Turtl :**
```turtl
fonction carre :
  repete 4 fois :
    avance $1
    tourne à droite
  fin repete
fin fonction

tortues 2
couleur #FF0000 @1
carre 5
```

## 💻 Ma contribution

Développement complet de l'**analyseur lexical (Scanner)** et de l'**analyseur syntaxique (Parser)**.

### Scanner (Flex)
Création de tous les tokens du langage :
- Mots-clés : `avance`, `recule`, `si`, `tant que`, `repete`, `fonction`, etc.
- Opérateurs arithmétiques : `+`, `-`, `*`, `/`, `()`
- Conditions : `mur`, `vide`, `pas de`
- Gestion multi-tortues avec `@n`
- Couleurs hexadécimales `#RRGGBB`

### Parser (Bison)
Implémentation de la grammaire complète :
- Instructions de déplacement avec répétitions optionnelles
- Expressions arithmétiques
- Conditionnelles (`si/sinon`)
- Boucles (`tant que`, `repete n fois`)
- Définition et appel de fonctions avec paramètres (`$1`, `$2`, etc.)
- Gestion de plusieurs tortues simultanément

### Structure de données (AST)
Construction d'un arbre syntaxique abstrait avec :
- Nœuds pour chaque type d'instruction
- Évaluation des expressions arithmétiques
- Table des symboles pour les fonctions


## 🛠️ Technologies

**Flex & Bison** • **C/C++** • **Qt 6** 

## 🎓 Compétences acquises

- Théorie de la compilation (analyse lexicale/syntaxique)
- Conception de grammaires formelles
- Structures de données avancées (AST)
- Travail collaboratif et méthodologie (conception → implémentation)
- Débogage de problèmes complexes (dépendances circulaires, parsing)

---

*Projet académique - LERIA - Université d'Angers*
