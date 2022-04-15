projet_mastermind

# Plan d'action ##############

#### Repartition des tâches


#### Fonctionalitées principales

- Un menu qui affiche les objets Tkinter en fonctio du mode choisis
- Mastermind :
    - Joueur 2 donne un code secret
    - J1 fait une proposition de code (essaye de décodé)
    - J2 dit si bien placé et mal placé
    - J1 refet proposition jusqu'a gagner
- 2 mods :
    - 1 joueur : le J2 est l'ordi 
    - multi joueurs : le J2 est un joueur

- sauvegarde :
    - créé dans un fichier text les info de jeux
    - charger les info et maj la partie en fonction
- Proposition (triche) :
    - l'ordi propose une solution possible en fonction des indices


###### Fait ######
# Tkinter
- Frame
- canvas
- boutons
- labels

# MENU
- bouton 1 joueur et multi

###### A Faire ######

- Gerer un systeme de phase (dès qu'un validé est appuier, permet ou pas des actions)(a voir)

## Variables globales :

- code a déchiffré (aussi pr sauvegarde)
- possibilitées de codes : (a voir)
- proposition faite (pr sauvegarde)
- type de partie en cour (pr sauvegarde)

## Affichage :

- zone du code :
    - affichage ou non du code
    - zone noir si jamais

- Instructions : (Bonus)
    - bienvenu, jouez
    - Joueur 1 : proposer un code
    - Joueur 2 : voici le code, dites les quels st bon ou pas
    - J1 re proposez code
    ...
    - Gagné/perdu

## Fonctions à faire :

# Fonction global :

- Réinitialisation de l'affichage
- Réinitialisation des variables globales

# Tkinter

# MENU
- reprendre :
    - récupère les infos de sauvegarde

# Sous menu : (en haut à gauche)
- Replay : (relance une partie)
    - réinitialise les variables
    - // l'affichage
- Propositions :
    - regarde les indices donnés (bien/mal placé)
    - propose un code possible (au hasard si plus. possibilitées)
- Sauvegarde :
    (- créé un fichier si existe pas)
    - enregistre les info de jeu
- Menu : (Bonus) :
    - réinitialise les variables
    - retourne au menu

# Joueur 1 : (en bas)
- couleurs :
    - créé les carrés dans canvas
    - remplis la variable global
- effacer :
    - supprime le der carré posé (de l'essai)
    - // ds la var
- Validé :
    - Passe à la phase d'après

# Joueur 2 : (à gauche, en dessous du sous menu)
- 1/2/3/4 : affiche dans le canvas de droite les couleurs bien ou mal placé
    - si multi : J2, si 1 joueur : auto
- Effacer : (// que pr joueurs 1 mais pour les chiffres ds le canvas 2)
- Validé : //

## Sauvegrde :
    - info a enregistrer :
        - type de partie (1J ou multi)
        - code
        - essai fait
        (- pas besoin des bien/mal placé, ça ce recalcul)
    - mise en forme du fichier (où sont les infos)
