from tkinter import Tk, PhotoImage, Frame, Canvas, messagebox, Menu, Label
from random import randint
from tkinter.simpledialog import askinteger

#######################################################
# Tic Tac Toe par Enzo Côme , projet de NSI 2022-2023 # 
#######################################################

Page = Tk()
Joueur = randint(1, 2)  # Joueur = 1 = Croix / Joueur = 2 = Rond
Nombre = 9  # Nombre de manches restantes
ScoreCroix = 0  # Définit les scores par défaut (0)
ScoreRond = 0


def nv():
    """Lance une nouvelle partie en décrémentant le nombre de manches"""
    global Page, ScoreCroix, ScoreRond, Nombre
    
    if Nombre > 0:
        Nombre = Nombre - 1
    
    sc = ScoreCroix
    sr = ScoreRond
    Page.destroy()
    ScoreCroix = sc
    ScoreRond = sr
    Page = Tk()
    NouvellePartie()


def afficher_fin_jeu():
    """Affiche le message de fin de tournoi"""
    if ScoreRond > ScoreCroix:
        messagebox.showinfo(title="Fin du jeu", message=f"Le gagnant est : Rond ({ScoreRond} - {ScoreCroix})")
    elif ScoreRond < ScoreCroix:
        messagebox.showinfo(title="Fin du jeu", message=f"Le gagnant est : Croix ({ScoreCroix} - {ScoreRond})")
    else:
        messagebox.showinfo(title="Fin du jeu", message=f"Égalité ! ({ScoreCroix} - {ScoreRond})")



def NouvellePartie():
    """Initialise une nouvelle partie avec l'interface graphique"""
    global Croix, Rond, Joueur, ScoreCroix, ScoreRond, TikTak, Page, Score, Player
    
    # Menu
    menubar = Menu(Page)
    menuPartie = Menu(menubar, tearoff=0)
    menuPartie.add_command(label="Nouvelle Partie", command=nv)
    menuPartie.add_command(label="Redémarrer à 0", command=restart)
    menuPartie.add_separator()
    menuPartie.add_command(label="Quitter", command=Page.destroy)
    menubar.add_cascade(label="Partie", menu=menuPartie)
    Page.config(menu=menubar)
    
    # Configuration de la fenêtre 
    TikTak = Frame(Page)
    Page.title("Tic Tac Toe")
    Page.resizable(0, 0)
    Page.geometry('500x600+300+100')  
    Page.config(bg="#1a1a2e") 
    
    # Importation des Images
    Croix = PhotoImage(file='croix.png')
    Rond = PhotoImage(file='rond.png')
    
    # Redimensionnement 
    Croix = Croix.subsample(Croix.width() // 80, Croix.height() // 70)
    Rond = Rond.subsample(Rond.width() // 80, Rond.height() // 70)
    
    # Titre du jeu
    titre = Label(Page, text="TIC TAC TOE", 
                  bg="#1a1a2e", fg="#00d9ff")
    titre.pack(pady=10)
    
    # grille de jeu
    TikTak.config(bg="#1a1a2e", padx=20, pady=10)
    TikTak.pack()
    
    Map()  # Création de la carte de jeux
    
    # Affichage du score 
    Score = Label(Page, text=f"⭕ {ScoreRond}  |  ❌ {ScoreCroix}  |  Manches: {Nombre}", 
                  font=("Arial", 14, "bold"), bg="#1a1a2e", fg="#ffffff",
                  pady=10)
    Score.pack(side="top")
    
    # Zone d'affichage
    tour_frame = Frame(Page, bg="#1a1a2e")
    tour_frame.pack(side="top", pady=10)
    
    tour_label = Label(tour_frame, text="Tour de :", font=("Arial", 12), 
                       bg="#1a1a2e", fg="#ffffff")
    tour_label.pack(side="left", padx=5)
    
    Player = Canvas(tour_frame, width=80, height=75, bg="#0f3460", 
                    highlightbackground="#00d9ff")
    Player.pack(side="left")
    
    # Affichage du tour
    if Joueur == 1:
        Player.create_image(40, 40, image=Croix)
    else:
        Player.create_image(40, 40, image=Rond)


def Map():
    """Crée la grille de jeu 3x3"""
    global Tours, Cliquable, Joueur, Carte, Corres, i, z
    
    Tours = 0
    Carte = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    
    # 0 = Vide / 1 = Croix / 2 = Rond
    Corres = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    Cliquable = [[True, True, True],
                 [True, True, True],
                 [True, True, True]]
    
    # Création des boutons 
    for i in range(3):
        for z in range(3):
            Carte[i][z] = Canvas(TikTak, width=110, height=110, 
                                bg="#0f3460",  
                                highlightbackground="#00d9ff", 
                                highlightthickness=3)  
            Carte[i][z].grid(column=i, row=z, padx=3, pady=3)
            Carte[i][z].bind("<Button-1>", lambda e=0, x=i, y=z: Clic(e, x, y))
            # Effet hover
            Carte[i][z].bind("<Enter>", lambda e, x=i, y=z: hover_enter(e, x, y))
            Carte[i][z].bind("<Leave>", lambda e, x=i, y=z: hover_leave(e, x, y))


def hover_enter(event, i, z):
    """Effet visuel au survol de la souris"""
    if Cliquable[i][z]:
        Carte[i][z].config(bg="#16213e")  


def hover_leave(event, i, z):
    """Retour à la couleur normale"""
    if Cliquable[i][z]:
        Carte[i][z].config(bg="#0f3460")


def NbManche():
    """Définit au début du jeu le nombre de manches"""
    global Nombre
    
    nb = askinteger(title="Nombre de manches", prompt="Combien de manches souhaitez-vous jouer ?")
    
    if nb and nb > 0:
        Nombre = nb
        return Nombre
    else:
        messagebox.showerror(message="Le nombre de parties doit être supérieur à 0")
        return NbManche()


def fin(gagnant, positions, type_victoire):
    """Gère la fin de partie quand il y a un gagnant"""
    global Nombre, ScoreCroix, ScoreRond, Score
    
    # Désactive tous les boutons
    for h in range(3):
        for j in range(3):
            Cliquable[h][j] = False
    
    # Dessine la ligne de victoire selon le type
    if type_victoire == "horizontale":
        # Ligne horizontale
        ligne = positions[0][0]
        for col in range(3):
            Carte[col][ligne].create_line(15, 55, 95, 55, width=6, fill="#00ff41")
    
    elif type_victoire == "verticale":
        # Ligne verticale
        colonne = positions[0][1]
        for ligne in range(3):
            Carte[colonne][ligne].create_line(55, 15, 55, 95, width=6, fill="#00ff41")
    
    elif type_victoire == "diagonale_desc":
        # Diagonale descendante (\)
        for i in range(3):
            Carte[i][i].create_line(15, 15, 95, 95, width=6, fill="#00ff41")
    
    elif type_victoire == "diagonale_mont":
        # Diagonale montante (/)
        for i in range(3):
            Carte[i][2-i].create_line(15, 95, 95, 15, width=6, fill="#00ff41")
    
    # Attribution des points (1 point par victoire)
    if gagnant == 1:
        ScoreCroix = ScoreCroix + 1
    else:
        ScoreRond = ScoreRond + 1
    
    # Mise à jour du score
    Score.config(text=f"⭕ {ScoreRond}  |  ❌ {ScoreCroix}  |  Manches: {Nombre}")
    
    # Vérification de la fin du jeu
    if Nombre == 0:
        Page.after(2000, afficher_fin_jeu)  # Affiche le message final après 2 secondes
    else:
        Page.after(2000, nv)  # Relance une nouvelle partie après 2 secondes


def egalite():
    """Gère le cas d'égalité (grille remplie)"""
    global ScoreCroix, ScoreRond, Score, Nombre
    
    # Désactive tous les boutons
    for h in range(3):
        for j in range(3):
            Cliquable[h][j] = False
    
    
    Score.config(text=f"⭕ {ScoreRond}  |  ❌ {ScoreCroix}  |  Manches: {Nombre}")
    
    # Vérification de la fin du jeu
    if Nombre == 0:
        Page.after(2000, afficher_fin_jeu)
    else:
        Page.after(2000, nv)  # Relance automatiquement après 2 secondes


def verif(i, z):
    """Vérifie s'il y a un gagnant après chaque coup"""
    # Ligne horizontale
    if Corres[z][0] == Corres[z][1] == Corres[z][2] != 0:
        fin(Corres[z][0], [(z, 0), (z, 1), (z, 2)], "horizontale")
    # Colonne verticale
    elif Corres[0][i] == Corres[1][i] == Corres[2][i] != 0:
        fin(Corres[0][i], [(0, i), (1, i), (2, i)], "verticale")
    # Diagonale \
    elif Corres[0][0] == Corres[1][1] == Corres[2][2] != 0:
        fin(Corres[0][0], [(0, 0), (1, 1), (2, 2)], "diagonale_desc")
    # Diagonale /
    elif Corres[0][2] == Corres[1][1] == Corres[2][0] != 0:
        fin(Corres[0][2], [(0, 2), (1, 1), (2, 0)], "diagonale_mont")
    elif Tours == 9:
        egalite()


def Clic(AntiBug, i, z):
    """Gère les clics sur les cases de la grille"""
    global Joueur, Player, Tours
    
    if Cliquable[i][z]:
        Tours = Tours + 1
        Cliquable[i][z] = False
        Carte[i][z].config(bg="#1a1a2e")  # Change la couleur de fond quand cliqué
        
        if Joueur == 1:
            # Le joueur 1 (Croix) joue
            Player.delete('all')
            Carte[i][z].create_image(55, 55, image=Croix)  # Affiche une croix sur la carte
            Player.create_image(40, 40, image=Rond)  # Affiche le prochain tour (Rond)
            Corres[z][i] = 1  # Applique la valeur "croix" à la case correspondante
            Joueur = 2  # Change de joueur
            
            if Tours >= 5:
                verif(i, z)
        else:
            # Le joueur 2 (Rond) joue
            Player.delete('all')
            Carte[i][z].create_image(55, 55, image=Rond)
            Player.create_image(40, 40, image=Croix)
            Corres[z][i] = 2
            Joueur = 1
            
            if Tours >= 5:
                verif(i, z)


def restart():
    """Redémarre complètement le jeu à zéro"""
    global Page, Joueur, ScoreCroix, ScoreRond, Nombre
    
    ScoreCroix = 0
    ScoreRond = 0
    Joueur = randint(1, 2)
    
    Page.destroy()
    Page = Tk()
    
    NbManche()  # Redemande le nombre de manches
    NouvellePartie()


# Lancement du jeu
NbManche()
NouvellePartie()
Page.mainloop()