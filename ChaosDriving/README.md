# 🚗 ChaosDriving - EN COURS

## 📋 Contexte

Ce projet fait partie de mon stage chez **Ours Agile Studio**.
**Objectif :** Développer un jeu de course arcade avec une route infinie générée procéduralement, des obstacles dynamiques et des interactions avec TikTok pour que les streamers puissent jouer en direct et que les viewers influencent le jeu (spawn de véhicules, obstacles, boosts etc)

## 🎮 Description du jeu

**ChaosDriving** est un jeu de course arcade de type *endless runner*.  
Le joueur doit survivre le plus longtemps possible sur une route infinie générée de manière procédurale, éviter des bombes, collecter de l’argent et utiliser des pouvoirs pour maximiser son score.

## 💻 Systèmes implémentés

### Génération de route infinie
- Système de **pooling d’objets** pour des performances optimales
- File de segments actifs numérotés (`RoadGenerator.cs`, `RoadStraight.cs`)
- Recyclage automatique des segments derrière le joueur
- Détection de la position de la voiture via **raycast**

### Contrôleur de voiture (`CarController.cs`)
- Déplacement avec **Rigidbody** et `MovePosition` pour une physique stable
- Support clavier ZQSD / WASD / flèches directionnelles
- Système de **boost**

### Caméra dynamique (`CameraFollow.cs`)
- Suivi fluide du véhicule
- **FOV dynamique** pour accentuer la sensation de vitesse

### Obstacles et collectibles
- **Bombes** (`Bomb.cs`)
- **Argent** (`Money.cs`)
- Suppression automatique après collecte

### UI & Menus
- **HUD** (`LiveUI.cs`) : Affichage des vies
- **Menu principal** (`MainMenu.cs`) : Navigation entre les scènes
- **Effets de boutons** (`ButtonHover.cs`) : Effet visuel au survol

## 🛠️ Technologies

**Unity 6** • **C#** • **Physique Rigidbody** • **Input System** • **TextMeshPro** • **Object Pooling**

## 🎓 Compétences acquises

- Architecture de jeu avec un **GameManager centralisé**
- Génération procédurale avec **recyclage mémoire** (pooling)
- Détection de collisions par **raycast**
- Gestion des états du jeu (*Playing*, *Paused*, *GameOver*)
