# 🚗 ChaosDriving

> Endless Runner arcade post-apocalyptique développé sous Unity 6

## 📘 Game Design Document

Le projet possède également un **GDD (Game Design Document)** contenant :
- les mécaniques détaillées,
- les systèmes de gameplay,
- les boucles de jeu,
- des visuels

📄 Consulter le GDD : [ChaosDriving_GDD.pdf](./Gdd_ChaosDriving.pdf)

---

## 📖 Présentation

**ChaosDriving** est un jeu arcade de type *Endless Runner*

Le joueur pilote une voiture dans un univers post-apocalyptique, sur une route infinie générée procéduralement.  
L’objectif est de survivre le plus longtemps possible tout en évitant des obstacles, en collectant de l’argent et en améliorant son véhicule via une boutique.

Le projet est également pensé pour une future interaction avec **TikTok Live**, permettant aux viewers d’influencer directement la partie en temps réel (spawn d’obstacles, boosts, véhicules ennemis, etc.).

---

# 🎮 Gameplay

- 🚘 Route infinie
- 💣 Obstacles :
  - Bombes
  - Voitures ennemies
  - Flaques d’huile
  - Wagons couchés
- 💰 Collecte d’argent
- 🧲 Système d’aimant pour attirer l'argent
- ⚡ Nitro / Boost de vitesse
- ❤️ Gestion des vies
- 🛒 Boutique avec upgrades et déblocage de véhicules
- 📈 Système de progression sauvegardé

---

# 🕹️ Contrôles

| Action | Touches |
|---|---|
| Avancer | `Z` / `W` / `↑` |
| Reculer / ralentir | `S` / `↓` |
| Ralentir | `Q` / `A` / `←` |
| Nitro / Boost | `Espace` / `D` / `→` |

---

# 🧠 Fonctionnalités principales

## 🌍 Génération de route

Le jeu utilise un système de génération infinie basé sur le **pooling d’objets** afin d’optimiser les performances.

### Fonctionnement
- Segments de route recyclés dynamiquement
- File de segments actifs numérotés
- Raycast sous le véhicule pour détecter le segment actuel
- Recyclage automatique des segments derrière le joueur
- Respawn dynamique des pickups à chaque réutilisation

### Scripts principaux
- `RoadGenerator.cs`
- `RoadStraight.cs`

---

## 🚗 Vehicule

### Fonctionnalités
- Déplacement basé sur `Rigidbody`
- Utilisation de `MovePosition` pour une physique stable
- Gestion du Nitro
- Gestion du ralentissement
- Système de glissade sur huile
- Détection des collisions et perte de vies

### Script principal
- `CarController.cs`

---

## 🎥 Caméra 

Le système de caméra renforce la sensation de vitesse grâce à :
- Un suivi fluide du véhicule
- Un angle positionné sur le côté droit de la voiture
- Un FOV dynamique évoluant selon la vitesse (`60° → 80°`)

### Script principal
- `CameraFollow.cs`

---

# ⚠️ Obstacles & Pickups

## Obstacles
| Objet | Effet |
|---|---|
| 💣 Bombe | Retire une vie |
| 🚗 Voiture ennemie | Retire une vie |
| 🛢️ Flaque d’huile | Glissade incontrôlable pendant 2 secondes |
| 🚃 Wagon couché | Retire une vie |

## Pickups
| Objet | Effet |
|---|---|
| 💰 Argent | +50$ |
| 🧲 Aimant | Attire l’argent autour du joueur |

---

# 🛒 Boutique & Progression

## 🚘 Véhicules disponibles (visuels dans le Gdd)
- Betall
- Toyoyo
- Landy Lorean
- Tristar

Chaque véhicule possède ses propres statistiques de base.

---

## 📈 Système d’amélioration

Chaque voiture dispose de 4 upgrades indépendants :

| Upgrade | Effet |
|---|---|
| ❤️ Santé | +1 vie |
| ⚡ Vitesse | Augmente la vitesse de base |
| 🧲 Aimant | Augmente le rayon d’attraction |
| 🔥 Nitro | Augmente la puissance du boost |

- 5 niveaux maximum par upgrade
- Prix évolutifs
- Sauvegarde via `PlayerPrefs`

---

# 💾 Sauvegarde des données

Le système sauvegarde :
- L'argent total
- La meilleure distance
- Le véhicule sélectionné
- Les upgrades débloqués
- La distance totale parcourue
- Le nombre de parties jouées
- La distance moyenne

---

# 🖥️ Interface utilisateur

## HUD en jeu
- ❤️ Nombre de vies
- 💰 Argent collecté
- Distance parcourue

## Menus
- Menu principal
- Écran de Game Over
- Boutique
- Effets de hover

### Scripts UI
- `LiveUI.cs`
- `MainMenu.cs`
- `ButtonHover.cs`

---

# 🛠️ Technologies utilisées

- **Unity 6**
- **C#**
- **PlayerPrefs**

---

# 🎓 Compétences acquises

Ce projet m’a permis de travailler sur :

- L’architecture d’un jeu Unity
- La génération procédurale
- L’optimisation avec le pooling
- La gestion d’états de jeu (`Menu`, `Playing`, `Dead`, `GameOver`)
- Les systèmes de sauvegarde
- Le développement d’une boutique et d’un système de progression
- La gestion de physique avec `Rigidbody`
- Les interactions UI / UX
- Les mécaniques arcade orientées gameplay

---

# 📌 Possible amélioration

🚧 Projet actuellement terminé.

Fonctionnalités ajoutable :
- Intégration TikTok Live
- Nouveaux obstacles
- Nouveaux véhicules
- Effets visuels et sonores avancés
- Système de score en ligne

---

# 👨‍💻 Auteur

Développé par Enzo Côme

