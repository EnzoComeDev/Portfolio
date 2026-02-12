##############################
# NONOGRAM BY ENZO / NICOLAS #
#        MADE IN 2024        #
#  PROJET SCOLAIRE L1 INFO   #
##############################

import tkinter
import tkinter.filedialog
import tkinter.messagebox
import PIL 
from PIL import Image
import random

def suppresion_bouton():
    BoutonNB.pack_forget()
    BoutonCouleur.pack_forget()
    BoutonQuitter.pack_forget()
    bandeau_label.pack_forget()

def cellule(event):
    global nb_coup 
    nb_coup += 1
    x, y = event.x, event.y
    # Convertir les coordonnées du clic en coordonnées de la cellule
    cell_x = x // cell_size
    cell_y = y // cell_size
    if grid[cell_y][cell_x] == 0:
        grid[cell_y][cell_x] = 1
        color = "black"
    else:
        grid[cell_y][cell_x] = 0
        color = "white"
    canvas.itemconfig(cells[cell_y][cell_x], fill=color)
    victoire()

def indices_nb():
    global indices_lignes, indices_colonnes
    indices_lignes = []
    indices_colonnes = []

    #lignes
    for ligne in matrice_vrai:
        indices = []
        compteur = 0
        for cellule in ligne:
            if cellule:
                compteur += 1
            elif compteur > 0: #En cas de cellule vide et de compteur non nul
                indices.append(compteur)
                compteur = 0
        if compteur > 0:
            indices.append(compteur)
        elif len(indices) ==0: #En cas de ligne vide 
            indices.append(0)
        indices_lignes.append(indices)

    #colonnes
    for j in range(len(matrice_vrai[0])): 
        indices = [] 
        compteur = 0
        for i in range(len(matrice_vrai)): 
            if matrice_vrai[i][j]:
                compteur += 1
            elif compteur > 0:
                indices.append(compteur)
                compteur = 0
        if compteur > 0:
            indices.append(compteur)
        elif len(indices) ==0: 
            indices.append(0)
        indices_colonnes.append(indices)

def PartieNoirBlanc():
    global canvas , grid , cells , ChoixJeux 
    #Grille Solution : matrice_vrai 
    def GenerationAleatoireNB():
        global matrice_vrai , nb_coup_mini
        matrice_vrai = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
        nb_coup_mini = 0 
        for ligne in matrice_vrai:
            for element in ligne:
                if element == 1:
                    nb_coup_mini += 1
    ChoixJeux = 1
    suppresion_bouton()
    if ChoixGen =="GenImage":
        img = image()
        grille_nb(img)
    else:
        GenerationAleatoireNB()

    indices_nb()

    Titre_label = tkinter.Label(Page, text="Nonogram", bg="Gray", fg="white", font=("Arial", 14))
    Titre_label.pack(padx=10,pady=10)
    Cadre_principal = tkinter.Frame(Page)

    #INDICES : 
    indices_lignes_frame = tkinter.Frame(Cadre_principal)
    indices_lignes_frame.grid(row=1, column=0)

    indices_colonnes_frame = tkinter.Frame(Cadre_principal)
    indices_colonnes_frame.grid(row=0, column=1)

    espace_vide = tkinter.Label(Cadre_principal, width=5, height=3)#, borderwidth=2, relief="solid"-> affiche la bordure
    espace_vide.grid(row=0, column=0)

    canvas = tkinter.Canvas(Cadre_principal, width=cols*cell_size, height=rows*cell_size, bg="white")
    canvas.grid(row=1, column=1)

    #Affichage : 
    grid = [[0] * cols for _ in range(rows)]
    cells = [[None] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            cell_id = canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
            cells[i][j] = cell_id
    canvas.bind("<Button-1>", cellule)  #Clic gauche pour changer la couleur
    #Fin Affichage

    #Affichage des indices
    for i in range(len(indices_lignes)):
        ligne = " ".join(str(x) for x in indices_lignes[i])
        tkinter.Label(indices_lignes_frame, text=ligne, anchor="e").grid(row=i, column=0, pady=9)

    for j in range(len(indices_colonnes)):
        colonne = "\n".join(str(x) for x in indices_colonnes[j])
        tkinter.Label(indices_colonnes_frame, text=colonne, anchor="s").grid(row=0, column=j, padx=13)

    Cadre_principal.place(relx=0.5, rely=0.5, anchor="center")

def PartieCouleur():
    global couleur_actuelle, cell_size, canevas, matrice_couleur , ChoixJeux
    ChoixJeux = 2
    couleur_actuelle = "white"
    # Fonctions pour choisir la couleur actuelle
    def rouge():
        global couleur_actuelle
        couleur_actuelle = "red"
    def vert():
        global couleur_actuelle
        couleur_actuelle = "green"
    def bleu():
        global couleur_actuelle
        couleur_actuelle = "blue"
    def violet():
        global couleur_actuelle
        couleur_actuelle = "purple"
    def jaune():
        global couleur_actuelle
        couleur_actuelle = "yellow"
    # Fonction pour remplir une case avec la couleur actuelle
    def RemplirCase(event, i, j):
        global couleur_actuelle , nb_coup
        if couleur_actuelle != "white": #Empeche toute vérification alors que l'utilsateur n'as pas choisi de couleur
            if matrice_couleur[i][j] == couleur_actuelle:
                matrice_couleur[i][j] = "white"
                canevas.itemconfig(cell_couleur_ids[i][j], fill="white")
            else:
                matrice_couleur[i][j] = couleur_actuelle
                canevas.itemconfig(cell_couleur_ids[i][j], fill=couleur_actuelle)
            nb_coup += 1
            victoire()
    def GenerationAleatoireCouleur():
        global matrice_vrai_couleur, nb_coup_mini
        couleurs =["white", "red", "green", "blue", "purple", "yellow"] #Ajouter des "white" pour réduire la facilité
        matrice_vrai_couleur = [[random.choice(couleurs) for _ in range(cols)] for _ in range(rows)]
        nb_coup_mini = 0
        for ligne in matrice_vrai_couleur:
            for element in ligne:
                if element != "white":
                    nb_coup_mini += 1

    if ChoixGen =="GenImage":
        img = image()
        grille_couleur_solution(img)
    else:
        GenerationAleatoireCouleur()

    suppresion_bouton()
    indices_couleur() #Génération des indices

    #BOUTONS
    cadre_boutons = tkinter.Frame(Page)
    cadre_boutons.pack(side=tkinter.BOTTOM, fill='x')
    bouton_rouge = tkinter.Button(cadre_boutons, text="Rouge", bg="red", command=rouge, height=3)
    bouton_rouge.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    bouton_vert = tkinter.Button(cadre_boutons, text="Vert", bg="green", command=vert, height=3)
    bouton_vert.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    bouton_bleu = tkinter.Button(cadre_boutons, text="Bleu", bg="#4169E1", command=bleu, height=3)
    bouton_bleu.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    bouton_violet = tkinter.Button(cadre_boutons, text="Violet", bg="purple", command=violet, height=3)
    bouton_violet.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    bouton_jaune = tkinter.Button(cadre_boutons, text="Jaune", bg="yellow", command=jaune, height=3)
    bouton_jaune.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
    Cadre_principal = tkinter.Frame(Page)#Affichage de la bordure -> borderwidth=2, relief="solid"
    Cadre_principal.place(relx=0.5, rely=0.5, anchor="center")

    indices_lignes_couleur_frame = tkinter.Frame(Cadre_principal)
    indices_lignes_couleur_frame.grid(row=1, column=0)
    indices_colonnes_couleur_frame = tkinter.Frame(Cadre_principal)
    indices_colonnes_couleur_frame.grid(row=0, column=1)

    espace_vide = tkinter.Label(Cadre_principal, width=5, height=3)
    espace_vide.grid(row=0, column=0)
    canevas = tkinter.Canvas(Cadre_principal, width=cols*cell_size, height=rows*cell_size, bg="white")
    canevas.grid(row=1, column=1)

    matrice_couleur = [["white" for _ in range(cols)] for _ in range(rows)]
    cell_couleur_ids = [[None] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            x1, y1 = j * cell_size, i * cell_size
            x2, y2 = x1 + cell_size, y1 + cell_size
            cell_id = canevas.create_rectangle(x1, y1, x2, y2, outline="black", fill="white")
            cell_couleur_ids[i][j] = cell_id
            canevas.tag_bind(cell_id, "<Button-1>", lambda event, i=i, j=j: RemplirCase(event, i, j))

    #Affichage des indices : 
    for i in range(len(indices_lignes_couleur)):
        ligne_index = 0
        for chiffre, couleur in indices_lignes_couleur[i]:
            if couleur == 'yellow': #Le jaune est illisible de base
                label = tkinter.Label(indices_lignes_couleur_frame, text=chiffre, anchor="e", fg="#FFB100")
                label.grid(row=i, column=ligne_index, pady=9)
                ligne_index += 1
            elif couleur != 'white':
                label = tkinter.Label(indices_lignes_couleur_frame, text=chiffre, anchor="e", fg=couleur)
                label.grid(row=i, column=ligne_index, pady=9)
                ligne_index += 1
            elif chiffre == rows:
                label = tkinter.Label(indices_lignes_couleur_frame, text=str(0), anchor="e", fg="black")
                label.grid(row=i, column=ligne_index, pady=9)  
                ligne_index += 1  

    for j in range(len(indices_colonnes_couleur)):
        colonne_index = 0
        for chiffre, couleur in indices_colonnes_couleur[j]:
            if couleur == 'yellow': #Le jaune est illisible de base
                label = tkinter.Label(indices_lignes_couleur_frame, text=chiffre, anchor="e", fg="#FFB100")
                label.grid(row=i, column=ligne_index, pady=9)
                ligne_index += 1
            elif couleur != 'white':
                label = tkinter.Label(indices_colonnes_couleur_frame, text=chiffre, anchor="s", fg=couleur)
                label.grid(row=colonne_index, column=j, padx=13)
                colonne_index += 1
            elif chiffre == cols:
                label = tkinter.Label(indices_colonnes_couleur_frame, text=str(0), anchor="s", fg="black")
                label.grid(row=colonne_index, column=j, padx=13)  
                colonne_index += 1

def indices_couleur():
    global indices_lignes_couleur, indices_colonnes_couleur
    indices_lignes_couleur = []
    indices_colonnes_couleur = []

    #lignes
    for ligne in matrice_vrai_couleur:
        indices = []
        couleur_precedente = None
        compteur = 0
        for case in ligne:
            if case != couleur_precedente:
                if couleur_precedente is not None:
                    indices.append((compteur, couleur_precedente))
                compteur = 1
                couleur_precedente = case
            else:
                compteur += 1
        if compteur != 0: 
            indices.append((compteur, couleur_precedente))
        indices_lignes_couleur.append(indices)

    #colonnes
    for j in range(cols):
        indices = []
        couleur_precedente = None
        compteur = 0
        for i in range(rows):
            case = matrice_vrai_couleur[i][j]
            if case != couleur_precedente:
                if couleur_precedente is not None:
                    indices.append((compteur, couleur_precedente))
                compteur = 1
                couleur_precedente = case
            else:
                compteur += 1
        if compteur != 0:  
            indices.append((compteur, couleur_precedente))
        indices_colonnes_couleur.append(indices)
        #print("Indices lignes couleur :", indices_lignes_couleur)
        #print("Indices colonnes couleur :", indices_colonnes_couleur)

def image():
    #Récupère l'image et la stock dans une variable
    fichier_image= tkinter.filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if fichier_image: #Vérifie que l'image a bel et bien été récupérer
        image = PIL.Image.open(fichier_image)
        image = image.convert('RGB') #Evite tous bug !
        image = image.resize((rows,cols))
    return image

def grille_nb(image):
    #Genère la solution grâce à l'image
    global matrice_vrai , nb_coup_mini , rows , cols 
    nb_coup_mini = 0
    image_nb = image.convert('L') #Convertir l'image en noir et blanc
    image_nb = image_nb.resize((cols, rows))

    matrice_vrai = []
    # Parcourir chaque pixel de l'image
    for y in range(rows):
        ligne = []
        for x in range(cols):
            luminosite_pixel = image_nb.getpixel((x, y)) # Obtenir la luminosité du pixel à la position (x, y)
            #print("Position x :", x, "position y :" , y ," = " ,luminosite_pixel , end = "")
            if luminosite_pixel < 129: # Vérifie si la luminosité du pixel est inférieure à 129
                ligne.append(True) 
                nb_coup_mini += 1 
            else:
                ligne.append(False) 
        matrice_vrai.append(ligne) 

def grille_couleur_solution(image):
    global matrice_vrai_couleur , nb_coup_mini
    def choisir_couleur(r,g,b):
        if r > 128 and g < 128 and b < 128:
            return "red"
        elif r < 128 and g > 128 and b < 128:
            return "green"
        elif r < 128 and g < 128 and b > 128:
            return "blue"
        elif r > 100 and g < 128 and b > 128:
            return "purple"
        elif r > 128 and g > 128 and b < 128:
            return "yellow"
        else:
            return "white"
    nb_coup_mini = 0
    image = image.resize((cols,rows))
    matrice_vrai_couleur = []
    for y in range(rows):
        ligne = []
        for x in range(cols):
            couleur_pixel = image.getpixel((x, y))
            couleur = choisir_couleur(couleur_pixel[0],couleur_pixel[1],couleur_pixel[2])
            ligne.append(couleur)
            if couleur != "white":
                nb_coup_mini += 1
        matrice_vrai_couleur.append(ligne)
    #print(f"Solution : {matrice_vrai_couleur}")

def victoire():
    if ChoixJeux == 1:
        #print("Coup jouer : " , nb_coup , " Coup minimum : ", nb_coup_mini)
        #print(f"Solution : {matrice_vrai}")
        if nb_coup >= nb_coup_mini:
            if grid == matrice_vrai:
                tkinter.messagebox.showinfo("Victoire", "Félicitations, vous avez gagné !")
    if ChoixJeux == 2:
        #print("Matrice actuelle:", matrice_couleur)
        #print("Matrice solution:", matrice_vrai_couleur)
        if nb_coup >= nb_coup_mini:
            if matrice_couleur == matrice_vrai_couleur:
                tkinter.messagebox.showinfo("Victoire", "Félicitations, vous avez gagné !")

def taille(): #Récupère la taille du Nonogramme
    global bouton_aleatoire , bouton_image
    def valider_taille():
        global rows,cols , cell_size
        try:
            rows = int(rows_entre.get())
            cols = int(cols_entre.get())
            if rows < 1 or cols <1: #Vérification de valeur positive non nul
                raise ValueError
            if ChoixGen == "":
                raise ValueError("Choissisez un mode de génération.")
            Taille_Nono.destroy()
        except ValueError:
            tkinter.messagebox.showerror("Erreur", "Veuillez saisir des nombres entiers valides et choisir un mode de génération.")
            Taille_Nono.destroy()
            taille()

    Taille_Nono=tkinter.Toplevel(Page)
    Taille_Nono.title("Taille du Nonogram : ")
    Taille_Nono.resizable(False,False)
    tkinter.Label(Taille_Nono, text="Nombre de lignes : ").grid(row=0, column=0)
    tkinter.Label(Taille_Nono, text="Nombre de colonnes : ").grid(row=1, column=0)
    rows_entre = tkinter.Entry(Taille_Nono)
    cols_entre = tkinter.Entry(Taille_Nono)
    rows_entre.grid(row=0, column=1)
    cols_entre.grid(row=1, column=1)
    bouton_valider = tkinter.Button(Taille_Nono, text="Valider", command=valider_taille)
    bouton_valider.grid(row=3, columnspan=2,pady=8)
    bouton_aleatoire = tkinter.Button(Taille_Nono, text="Génération aléatoire" , command=BoutonGenAleatoire)
    bouton_aleatoire.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    bouton_image = tkinter.Button(Taille_Nono, text="Génération via une image", command=BoutonGenImage)
    bouton_image.grid(row=2, column=1, padx=10, pady=10, sticky="e")


def restart():
    suppresion_bouton()
    Page.destroy()
    Jouer()

def Jouer():
    global Page , BoutonNB , BoutonCouleur , BoutonQuitter , nb_coup , bandeau_label , ChoixJeux , cell_size , ChoixGen
    ChoixGen = str("") 
    #CREATION DE LA PAGE
    cell_size = 38 
    ChoixJeux = 0 # 0 = Non séléctionner / 1 = Noir et Blanc / 2 = Coloré
    Page = tkinter.Tk()
    Page.title('Nonogram Enzo / Nicolas') #Titre de la page
    Page.iconbitmap('Logo.ico') #Icon de la page
    Page.geometry('750x600') #Dimension
    Page.config(bg = 'Gray')
    """ Permet de mettre une image d'arrière plan
    arrplan = tkinter.PhotoImage(file="Logo.ico")
    can = tkinter.Canvas(Page,width=750,height=600)
    can.create_image(0, 0, anchor=tkinter.NW, image=arrplan)
    can.pack()
    """

    menubar = tkinter.Menu(Page)
    MenuPartie = tkinter.Menu(menubar, tearoff=0)
    MenuPartie.add_command(label="Nouvelle Partie (Noir/Blanc)" , command=PartieNoirBlanc)
    MenuPartie.add_command(label="Nouvelle Partie (Coloré)" , command=PartieCouleur)
    MenuPartie.add_command(label="Choix image" , command=image)
    MenuPartie.add_command(label="Redémarrer" ,command=restart)
    MenuPartie.add_command(label="Quitter", command=Page.destroy)
    menubar.add_cascade(label="Partie", menu=MenuPartie)
    Page.config(menu=menubar)
    taille()

    bandeau_label = tkinter.Label(Page, text="Choix du mode de jeu", bg="Gray", fg="white", font=("Arial", 14))
    bandeau_label.pack(padx=10)
    BoutonNB = tkinter.Button(Page, text= "Noir et Blanc", command=PartieNoirBlanc , activebackground= "black", activeforeground="white", width=35 , height= 8, relief = tkinter.FLAT)
    BoutonCouleur = tkinter.Button(Page, text= "Coloré", command=PartieCouleur , activebackground= "red", activeforeground="white", width=35 , height= 8, relief = tkinter.FLAT)
    BoutonQuitter = tkinter.Button(Page, text="Quitter" , command=Page.destroy , activebackground= "white", activeforeground="white", height= 4, relief = tkinter.SUNKEN)
    BoutonNB.pack(padx='5',pady='5')
    BoutonCouleur.pack(padx='10',pady='10')
    BoutonQuitter.pack(side= tkinter.BOTTOM , fill='x')

    nb_coup = 0
    Page.mainloop()

def BoutonGenAleatoire():
    global ChoixGen
    ChoixGen = "Aleatoire" 
    bouton_aleatoire.config(bg="lightblue")
    bouton_image.config(bg="SystemButtonFace")

def BoutonGenImage():
    global ChoixGen
    ChoixGen = "GenImage"
    bouton_image.config(bg="lightblue")
    bouton_aleatoire.config(bg="SystemButtonFace") #SystemButtonFace = Couleur par défaut 

def main():
    Jouer()

print("Programme compiler !")
main()