import tkinter as tk

racine=tk.Tk()

################################ création racine 1 /menu #######################

#fonctions pour les commandes des boutons
def bouton_1_joueur():
    for widget in frame1.winfo_children():
        widget.grid_forget()
        frame2.grid()

frame1=tk.Frame(racine)
frame1.grid()
frame2=tk.Frame(racine)
frame3=tk.Frame(frame2)

def bouton_multi_joueur():
    for widget in frame1.winfo_children():
        widget.grid_forget()
        frame2.grid()
        frame3.grid(row=7, column=1)

def bouton__reprendre():
    pass

#création des boutons
bouton_1joueur=tk.Button(frame1, text="1 joueur", command=bouton_1_joueur)
bouton_1joueur.grid(row=2, column=2)
bouton_multijoueur=tk.Button(frame1, text="multijoueur", command=bouton_multi_joueur)
bouton_multijoueur.grid(row=3, column= 2)
bouton_reprendre=tk.Button(frame1, text="reprendre", command=bouton__reprendre)
bouton_reprendre.grid(row=4, column=2)



############################### creation racine 2 ################################

#fonctions pour les boutons
def f_2_replay():
    pass

def f_2_proposition():
    pass

def f_2_sauvergarde():
    pass

def f_2_menu():
    pass

def f_2_blue():
    pass

def f_2_red():
    pass

def f_2_yellow():
    pass

def f_2_brown():
    pass

def f_2_pink():
    pass

def f_2_green():
    pass

def f_2_purple():
    pass

def f_2_orange():
    pass

def f_2_effacer():
    pass

def f_2_valider():
    pass

####### grille principale ############
HEIGHT_canvas_principal=300
WIDTH_canvas_principal=300

c_2_canvas_principal=tk.Canvas(frame2, height=HEIGHT_canvas_principal, width=WIDTH_canvas_principal, bg="orange")
c_2_canvas_principal.grid(row=2, column=3, rowspan=11, columnspan=4)

#on rajoute la grille
for i in range (4) :
    c_2_canvas_principal.create_line(((WIDTH_canvas_principal/4)*i, 0), ((WIDTH_canvas_principal/4)*i, WIDTH_canvas_principal), fill="black")
    
for j in range(10):
    c_2_canvas_principal.create_line((0, (HEIGHT_canvas_principal/10)*j), (HEIGHT_canvas_principal, (HEIGHT_canvas_principal/10)*j), fill="black")


########### grille solution #############
HEIGHT_canvas_solutions=300
WIDTH_canvas_solutions=300

c_2_canvas_solutions=tk.Canvas(frame2, height=HEIGHT_canvas_solutions, width=WIDTH_canvas_solutions, bg="blue")
c_2_canvas_solutions.grid(row=2, column=8, columnspan=2, rowspan=10)

#on rajoute la grille
for i in range (2) :
    c_2_canvas_solutions.create_line(((WIDTH_canvas_solutions/2)*i, 0), ((WIDTH_canvas_solutions/2)*i, WIDTH_canvas_solutions), fill="black")
    
for j in range(10):
    c_2_canvas_solutions.create_line((0, (HEIGHT_canvas_solutions/10)*j), (HEIGHT_canvas_solutions, (HEIGHT_canvas_solutions/10)*j), fill="black")

b_2_replay=tk.Button(frame2, text="replay", command=f_2_replay)
b_2_replay.grid(row=2, column=1)

b_2_proposition=tk.Button(frame2, text="proposition", command=f_2_proposition)
b_2_proposition.grid(row=3, column=1)

b_2_sauvergarde=tk.Button(frame2, text="sauvergarde", command=f_2_sauvergarde)
b_2_sauvergarde.grid(row=4, column=1)

b_2_menu=tk.Button(frame2, text="menu", command=f_2_menu)
b_2_menu.grid(row=5, column=1)

b_2_blue=tk.Button(frame2, text="blue", command=f_2_blue)
b_2_blue.grid(row=14, column=3)

b_2_red=tk.Button(frame2, text="red", command=f_2_red)
b_2_red.grid(row=14, column=4)

b_2_yellow=tk.Button(frame2, text="yellow", command=f_2_yellow)
b_2_yellow.grid(row=14, column=5)

b_2_brown=tk.Button(frame2, text="brown", command=f_2_brown)
b_2_brown.grid(row=14, column=6)

b_2_pink=tk.Button(frame2, text="pink", command=f_2_pink)
b_2_pink.grid(row=15, column=3)

b_2_green=tk.Button(frame2, text="green", command=f_2_green)
b_2_green.grid(row=15, column=4)

b_2_purple=tk.Button(frame2, text="purple", command=f_2_purple)
b_2_purple.grid(row=15, column=5)

b_2_orange=tk.Button(frame2, text="orange", command=f_2_orange)
b_2_orange.grid(row=15, column=6)

b_2_effacer=tk.Button(frame2, text="effacer", command=f_2_effacer)
b_2_effacer.grid(row=14, column=8, columnspan=2)

b_2_valider=tk.Button(frame2, text="valider", command=f_2_valider)
b_2_valider.grid(row=15, column=8, columnspan=2)

############################### creation racine 3 ################################
def f_3_1():
    pass

def f_3_2():
    pass

def f_3_3():
    pass

def f_3_4():
    pass

def f_3_effacer():
    pass

def f_3_valider():
    pass

b_3_1=tk.Button(frame3, text="1", command=f_3_1)
b_3_1.grid(row=1, column=1)
b_3_2=tk.Button(frame3, text="2", command=f_3_2)
b_3_2.grid(row=2, column=1)
b_3_3=tk.Button(frame3, text="3", command=f_3_3)
b_3_3.grid(row=3, column=1)
b_3_4=tk.Button(frame3, text="4", command=f_3_4)
b_3_4.grid(row=4, column=1)

b_3_effacer=tk.Button(frame3, text="effacer", command=f_3_effacer)
b_3_effacer.grid(row=6, column=1)
b_3_valider=tk.Button(frame3, text="valider", command=f_3_valider)
b_3_valider.grid(row=7, column=1)

racine.mainloop()