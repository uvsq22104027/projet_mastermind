import tkinter as tk

racine=tk.Tk()

################################ création label 1 /accueil #######################

canva1=tk.Canvas(racine, width=500, height=500, bg="orange")
canva1.grid(row=1, column=1)

#fonctions pour les commandes des boutons
def bouton_1_joueur():
    pass

def bouton_multi_joueur():
    pass

def bouton__reprendre():
    pass

#création des boutons
bouton_1joueur=tk.Button(canva1, text="1 joueur", command=bouton_1_joueur)
bouton_1joueur.grid(row=2, column=2)
bouton_multijoueur=tk.Button(canva1, text="multijoueur", command=bouton_multi_joueur)
bouton_multijoueur.grid(row=3, column= 2)
bouton_reprendre=tk.Button(canva1, text="reprendre", command=bouton__reprendre)
bouton_reprendre.grid(row=4, column=2)

racine.mainloop()




