# 🚗 ChaosDriving - EN COURS

## 📋 Contexte

Projet en cours liée a mon stage au sein de l'entreprise Ours Agile Studio   
**Objectif :** Créer un jeu de course arcade avec route infinie procédurale, obstacles dynamiques et intéractivités tiktok afin pour que le jeu soit jouée par des streamers et les viewers influent leurs jeux , spanw de 
véhicules , obstacles , gain de vitesse etc

## 🎮 Description du jeu

ChaosDriving est un jeu de course arcade en vue isométrique où le joueur doit survivre le plus longtemps possible sur une route infinie générée procéduralement. Il doit éviter les bombes, collecter de l'argent 
et utiliser des pouvoirs pour maximiser son score.

## 💻 Systèmes implémentés

### Génération de route infinie
Système de **pooling d'objets** pour une route procédurale performante :
- File de segments actifs avec numérotation (`RoadGenerator.cs`, `RoadStraight.cs`)
- Recyclage automatique des segments derrière le joueur
- Détection de position par **raycast** pour savoir sur quel segment se trouve la voiture

### Contrôleur de voiture (`CarController.cs`)
- Déplacement **Rigidbody** avec `MovePosition` pour une physique stable
- Support clavier ZQSD / WASD / flèches directionnelles
- Système de **boost** 

### Caméra dynamique (`CameraFollow.cs`)
- Suivi fluide
- **FOV dynamique** 

### Obstacles et collectibles
- **Bombes** (`Bomb.cs`)
- **Argent** (`Money.cs`)
- Destruction après collecte

### UI & Menus
- **HUD** (`LiveUI.cs`) : Affichage des vies
- **Menu principal** (`MainMenu.cs`) : Navigation entre les scènes 
- **Effets de boutons** (`ButtonHover.cs`) : Effet visuel lors du survol des boutons

## 🛠️ Technologies

**Unity 6** • **C#** • **Rigidbody Physics** • **Input System** • **TextMeshPro** • **Object Pooling**

## 🎓 Compétences acquises

- Architecture de jeu avec un GameManager centralisé
- Génération procédurale avec recyclage de la mémoire (pooling)
- Détection de collisions par raycast
- Gestion des états de jeu (Playing, Paused, GameOver)

---

