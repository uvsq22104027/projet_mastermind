import tkinter as tk
import random

racine = tk.Tk()
racine.title("MasterMind")

################################ création racine 1 /menu #######################

#fonctions pour les commandes des boutons
def bouton_1_joueur() :
    global vg_mode_jeux, vg_phase
    frame1.grid_forget()
    frame2.grid()
    frame5.grid(row = 14, column = 8, columnspan = 2)
    vg_mode_jeux = 1
    vg_phase = 1
    f_2_replay()

frame1 = tk.Frame(racine)   #"menu"
frame1.grid()
frame2 = tk.Frame(racine)   #base
frame3 = tk.Frame(frame2)   #ajout du second joueur pour mode multijoueur
frame4 = tk.Frame(frame2)   #combinaison lancée aléatoirement par l'ordi pour mode 1 joueur
frame5 = tk.Frame(frame2)   #bouton valider pour les 2 modes

#### Variables global
vg_frame4_existe = False
vg_mode_jeux = 0          # 0 = menu, 1 = 1 joueur, 2 = multijoueur
vg_phase = 0     # 0:auccun joueur joue, 1 : joueur 1, 2 : joueur 2 (qui rentre le code)
cpt_code = 0    # position liste du code à remplire

#########truc aleatoire de l'ordi pour facon 1 joueur ###############
HEIGHT_canva_aleatoire = 50
WIDTH_canva_aleatoire = 50*4

c_4_canvas_aleatoire = tk.Canvas(frame4, height = HEIGHT_canva_aleatoire, width=WIDTH_canva_aleatoire, bg = "grey")
c_4_canvas_aleatoire.grid(row = 0, column = 0)

liste_al = [] #
def f_initialisation_rond_solution() :
    global liste_al
    for i in range(0, HEIGHT_canva_aleatoire, 50) :
        for j in range (0, WIDTH_canva_aleatoire, 50) :
            rond = c_4_canvas_aleatoire.create_oval(j+10, i+10, j+40, i+40, fill = "grey")
            liste_al.append(rond)
f_initialisation_rond_solution()

color=["red", "orange", "yellow", "green", "blue", "purple", "brown", "pink"]

l_al=[] #solution

def f_reinitialisation_rond_solution() :
    for i in liste_al :
        c_4_canvas_aleatoire.itemconfigure(liste_al[i-1], fill = "grey")

def f_solution_alleatoire() :
    global l_al
    for i in range(len(liste_al)) :
        x = random.choice(color)
        c_4_canvas_aleatoire.itemconfigure(liste_al[i], fill = x)
        l_al.append(x)

###### Pour la proposition de code, a adapter

vg_l_bien_mal_place = [[] for i in range(10)]       # valeurs des b/m placé

##########@

def bouton_multi_joueur() :
    global vg_mode_jeux, vg_phase, vg_frame4_existe
    frame1.grid_forget()
    frame2.grid()
    frame3.grid(row = 7, column = 1)
    frame5.grid(row = 15, column = 8, columnspan=2)
    frame4.grid(row = 14, column = 3, columnspan=4)
    vg_frame4_existe = True
    vg_mode_jeux = 2
    vg_phase = 2
    f_2_replay()

def bouton__reprendre() :
    pass

#création des boutons
bouton_1joueur=tk.Button(frame1, text = "1 joueur", command = bouton_1_joueur)
bouton_1joueur.grid(row = 2, column = 2)
bouton_multijoueur=tk.Button(frame1, text = "multijoueur", command = bouton_multi_joueur)
bouton_multijoueur.grid(row = 3, column =  2)
bouton_reprendre=tk.Button(frame1, text = "reprendre", command = bouton__reprendre)
bouton_reprendre.grid(row = 4, column = 2)



############################### creation racine 2 ################################

#labels texts
l_2_bien_placé = tk.Label(frame2, text = "bien placé", bg = "pink")
l_2_bien_placé.grid(row = 1, column = 8)
l_2_mal_placé = tk.Label(frame2, text = "mal placé", bg = "pink")
l_2_mal_placé.grid(row = 1, column = 9)
l_2_instructions = tk.Label(frame2, text = "Bienvenue sur MasterMind ! \n voici quelques instructions sur la maniere de jouer \n un fois que vous avez placé vos couleurs, appuyez sur 'valider'. \n Si vous voulez changer, appuyez sur 'effacer'", wraplength=0, justify="center")
l_2_instructions.grid(row = 1, column = 1, columnspan=7)

#fonctions pour les boutons
"""Variables globales pour les indices donnés au joueur"""
NbRightPlace = 0
NbWrongPlace = 0
"""initialisation des compteurs et de la liste qui retient les couleurs"""
cpt = 0
cpt_sol = 0      #pour remplissage des bien/mal placé
cpt_valider = 0
l_couleur = [] #couleurs en cours

def f_g_reinitialisation() :
    "réinitialise les variables et effaces les carrées "
    global l_al, liste_al, vg_l_bien_mal_place, cpt, cpt_valider, vg_frame4_existe, l_couleur

    # ovals --> gris
    for i in range(len(liste)) :
        c_2_canvas_principal.itemconfigure(liste[i], fill = "grey")
    cpt = 0

    # chiffres bien/mal placé
    for i in range(len(liste_sol)) :
        c_2_canvas_solutions.itemconfigure(liste_sol[i], text = "")
    cpt_valider = 0
    
    # Code

    l_al = []

    #

    l_couleur = []

    # Frame 4 solution final
    if vg_mode_jeux == 1:
        if vg_frame4_existe :
            frame4.grid_forget()
            vg_frame4_existe = False
        #proposition solution
        f_solution_alleatoire()
    elif vg_mode_jeux == 2:
        f_reinitialisation_rond_solution()


    vg_l_bien_mal_place = [[] for i in range(10)]

def f_2_replay() :
    global l_al
    f_g_reinitialisation()
    l_2_instructions.config(text = "Bienvenue sur MasterMind ! \n voici quelques instructions sur la maniere de jouer \n un fois que vous avez placé vos couleurs, appuyez sur 'valider'. \n Si vous voulez changer, appuyez sur 'effacer'")

def f_2_proposition() :
    pass

def f_2_sauvergarde() :
    pass

def f_2_menu() :
    global vg_mode_jeux, vg_phase
    if vg_mode_jeux == 1:
        frame2.grid_forget()
    if vg_mode_jeux == 2:
        frame2.grid_forget()
    frame1.grid()
    vg_mode_jeux = 0
    vg_phase = 0
    f_g_reinitialisation()

def f_2_blue() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "blue"
    if vg_phase == 1 and cpt < 4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code < 4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_red() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "red"
    if vg_phase == 1 and cpt < 4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_yellow() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "yellow"
    if vg_phase == 1 and cpt<4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_brown() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "brown"
    if vg_phase == 1 and cpt<4 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4 :
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_pink() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "pink"
    if vg_phase == 1 and cpt<4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_green() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "green"
    if vg_phase == 1 and cpt<4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_purple() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "purple"
    if vg_phase == 1 and cpt<4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_orange() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "orange"
    if vg_phase == 1 and cpt<4:
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur
    if vg_phase == 2 and vg_frame4_existe and cpt_code<4:
        cpt_code += 1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code-1], fill = couleur)
        l_al.append(couleur)
    if vg_phase == 1 and (not vg_frame4_existe) and cpt//4 != 0 :
        cpt += 1
        c_2_canvas_principal.itemconfigure(liste[cpt-1], fill = couleur)
        l_couleur.append(couleur)
        if cpt%4 == 0:
            return (l_couleur)
        return couleur, l_couleur

def f_2_effacer() :
    global couleur, cpt, l_couleur, cpt_code
    couleur = "grey"
    if vg_phase == 1 and cpt >= 0:
        if len(l_couleur) > 0:
            l_couleur.remove(l_couleur[-1])
        if cpt > 0:
            cpt = cpt-1
        c_2_canvas_principal.itemconfigure(liste[cpt], fill = couleur)
    if vg_phase == 2 and vg_frame4_existe and cpt_code >= 0:
        if cpt_code > 0:
            cpt_code = cpt_code-1
        c_4_canvas_aleatoire.itemconfigure(liste_al[cpt_code], fill = couleur)
        if len(l_al)>0:
            l_al.remove(l_al[-1])
    

def f_5_valider() :
    global l_couleur, NbRightPlace, NbWrongPlace, cpt_valider, vg_frame4_existe, l_couleur, vg_phase
    if vg_mode_jeux == 1 and l_couleur == 4:
        f_comparaison(l_al, l_couleur)
        l_couleur=[]
        c_2_canvas_solutions.itemconfigure(liste_sol[(cpt_valider*2)], text = NbRightPlace)
        c_2_canvas_solutions.itemconfigure(liste_sol[(cpt_valider*2) + 1], text = NbWrongPlace)
        cpt_valider += 1
        if NbRightPlace == 4 :
            l_2_instructions.config(text = "BRAVO ! \n Vous avez gagné ! Vous voulez refaire une partie ? Appuyez sur replay" )
            frame4.grid(row = 14, column = 3, columnspan=4)
            vg_frame4_existe = True
        if cpt_valider>9 and NbRightPlace!=4:
            l_2_instructions.config(text = "Perdue... Réessayez, la prochaine sera la bonne !" )
            frame4.grid(row = 14, column = 3, columnspan = 4)
            vg_frame4_existe = True
        NbRightPlace = 0
        NbWrongPlace = 0
    if vg_mode_jeux == 2 :
        if vg_phase == 2 and cpt_code == 4 and vg_frame4_existe :
            frame4.grid_forget()
            vg_phase = 1
        elif vg_phase == 1 and l_couleur == 4 :
            frame4.grid(row = 14, column = 3, columnspan = 4)
            vg_phase = 2


def f_comparaison(l1, l2) :
    """Compare la proposition du joueur avec la solution, indique le nombre de billes au bonne endroits
    et celles aux mauvais endroits"""
    global NbRightPlace
    global NbWrongPlace
    l_aux = [False, False, False, False]
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l_aux[j]:
                continue
            elif l1[i] == l2[i]:
                NbRightPlace += 1
                l_aux[i] = True
                break
            elif l1[i] == l2[j]:
                if i == j:
                    NbRightPlace += 1
                else:
                    NbWrongPlace += 1
                l_aux[j] = True
                break
    return NbRightPlace, NbWrongPlace


####### grille principale ############
HEIGHT_canvas_principal = 500
WIDTH_canvas_principal = 200

c_2_canvas_principal=tk.Canvas(frame2, height=HEIGHT_canvas_principal, width=WIDTH_canvas_principal, bg = "grey")
c_2_canvas_principal.grid(row = 2, column = 3, rowspan = 11, columnspan = 4)

#on rajoute la grille 
for i in range(4) :
    c_2_canvas_principal.create_line(((WIDTH_canvas_principal/4)*i, 0), ((WIDTH_canvas_principal/4)*i, HEIGHT_canvas_principal), fill = "black")
    
for j in range(10) :
    c_2_canvas_principal.create_line((0, (HEIGHT_canvas_principal/10)*j), (HEIGHT_canvas_principal, (HEIGHT_canvas_principal/10)*j), fill = "black")

#et les ronds
liste=[]
for i in range(0, HEIGHT_canvas_principal, 50):
    for j in range (0, WIDTH_canvas_principal, 50):
        rond=c_2_canvas_principal.create_oval(j+10, i+10, j+40, i+40, fill = "grey")
        liste.append(rond)

########### grille solution #############
HEIGHT_canvas_solutions=500
WIDTH_canvas_solutions=100

c_2_canvas_solutions=tk.Canvas(frame2, height = HEIGHT_canvas_solutions, width = WIDTH_canvas_solutions, bg = "pink")
c_2_canvas_solutions.grid(row = 2, column = 8, columnspan=2, rowspan=10)
#permet de mettre les reponses dans la grille
liste_sol=[] # id des texte canvas rose
for i in range(0, HEIGHT_canvas_solutions, 50):
    for j in range(0, WIDTH_canvas_solutions, 50):
        sol=c_2_canvas_solutions.create_text(j+25,i+25, text = "")
        liste_sol.append(sol)

#on rajoute la grille
for i in range(2) :
    c_2_canvas_solutions.create_line(((WIDTH_canvas_solutions/2)*i, 0), ((WIDTH_canvas_solutions/2)*i, HEIGHT_canvas_solutions), fill = "black")
    
for j in range(10) :
    c_2_canvas_solutions.create_line(((0, (HEIGHT_canvas_solutions/10)*j), (HEIGHT_canvas_solutions, (HEIGHT_canvas_solutions/10)*j)), fill = "black")
   
# variable global joueur 2
cpt_b_m_place = 0

b_2_replay=tk.Button(frame2, text = "replay", command = f_2_replay, bg = "green")
b_2_replay.grid(row = 2, column = 1)

b_2_proposition=tk.Button(frame2, text = "proposition", command = f_2_proposition, bg = "green")
b_2_proposition.grid(row = 3, column = 1)

b_2_sauvergarde=tk.Button(frame2, text = "sauvergarde", command = f_2_sauvergarde, bg = "green")
b_2_sauvergarde.grid(row = 4, column = 1)

b_2_menu=tk.Button(frame2, text = "menu", command = f_2_menu, bg = "green")
b_2_menu.grid(row = 5, column = 1)

b_2_blue=tk.Button(frame2, text = "blue", command = f_2_blue)
b_2_blue.grid(row = 16, column = 3)

b_2_red=tk.Button(frame2, text = "red", command = f_2_red)
b_2_red.grid(row = 16, column = 4)

b_2_yellow=tk.Button(frame2, text = "yellow", command = f_2_yellow)
b_2_yellow.grid(row = 16, column = 5)

b_2_brown=tk.Button(frame2, text = "brown", command = f_2_brown)
b_2_brown.grid(row = 16, column = 6)

b_2_pink=tk.Button(frame2, text = "pink", command = f_2_pink)
b_2_pink.grid(row = 15, column = 3)

b_2_green=tk.Button(frame2, text = "green", command = f_2_green)
b_2_green.grid(row = 15, column = 4)

b_2_purple=tk.Button(frame2, text = "purple", command = f_2_purple)
b_2_purple.grid(row = 15, column = 5)

b_2_orange=tk.Button(frame2, text = "orange", command = f_2_orange)
b_2_orange.grid(row = 15, column = 6)

b_2_effacer=tk.Button(frame2, text = "effacer", command = f_2_effacer)
b_2_effacer.grid(row = 16, column = 8, columnspan=2)

b_5_valider=tk.Button(frame5, text = "valider", command = f_5_valider)
b_5_valider.grid(row = 0, column = 0)

############################### creation racine 3 ################################

def f_3_0() :
    global cpt_sol, chiffre
    if vg_phase == 2 :
        cpt_sol += 1
        chiffre = "0"
        c_2_canvas_solutions.itemconfigure(liste_sol[cpt_sol-1], text = chiffre)
        return chiffre

def f_3_1() :
    global cpt_sol, chiffre
    if vg_phase == 2 :
        cpt_sol += 1
        chiffre = "1"
        c_2_canvas_solutions.itemconfigure(liste_sol[cpt_sol-1], text = chiffre)
        return chiffre


def f_3_2() :
    global cpt_sol, chiffre
    if vg_phase == 2 :
        cpt_sol += 1
        chiffre = "2"
        c_2_canvas_solutions.itemconfigure(liste_sol[cpt_sol-1], text = chiffre)
        return chiffre

def f_3_3() :
    global cpt_sol, chiffre
    if vg_phase == 2 :
        cpt_sol += 1
        chiffre = "3"
        c_2_canvas_solutions.itemconfigure(liste_sol[cpt_sol-1], text = chiffre)
        return chiffre

def f_3_4() :
    global cpt_sol, chiffre
    if vg_phase == 2 :
        cpt_sol += 1
        chiffre = "4"
        c_2_canvas_solutions.itemconfigure(liste_sol[cpt_sol-1], text = chiffre)
        return chiffre

def f_3_effacer() :
    global cpt_sol, chiffre
    if vg_phase == 2 :
        chiffre = ""
        if cpt_sol>0:
            cpt_sol=cpt_sol-1    
        c_2_canvas_solutions.itemconfigure(liste_sol[(cpt_sol)], text = chiffre)
        return chiffre

def f_3_valider() :
    global vg_phase, cpt_sol, vg_frame4_existe
    if vg_phase == 2 and cpt_sol//2 != 0:
        frame4.grid_forget()
        vg_phase = 1
        vg_frame4_existe = False

b_3_0 = tk.Button(frame3, text = "0", command = lambda : f_3_0())
b_3_0.grid(row = 0, column = 1)
b_3_1 = tk.Button(frame3, text = "1", command = lambda : f_3_1())
b_3_1.grid(row = 1, column = 1)
b_3_2 = tk.Button(frame3, text = "2", command = lambda : f_3_2())
b_3_2.grid(row = 2, column = 1)
b_3_3 = tk.Button(frame3, text = "3", command = lambda : f_3_3())
b_3_3.grid(row = 3, column = 1)
b_3_4 = tk.Button(frame3, text = "4", command = lambda : f_3_4())
b_3_4.grid(row = 4, column = 1)

b_3_effacer = tk.Button(frame3, text = "effacer", command = f_3_effacer)
b_3_effacer.grid(row = 6, column = 1)
b_3_valider = tk.Button(frame3, text = "valider", command = f_3_valider)
b_3_valider.grid(row = 7, column = 1)


racine.mainloop()