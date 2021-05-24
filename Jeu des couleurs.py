# Membre du groupe 1 - MPC1-TD05
# AABIRATE Adam 22007525
# ASMAOUI Amine 22016409
# BENZAKINE Arthur 22006970
# MENNOUR Thomas 22004146
# WASBAUER Anna 21900086


#Import des librairies tkinter et random 
import tkinter as tk
import random as rd


#Constantes
compteur = 30
score = 0
demarrer = False
couleurs = ["blue", "red", "green", "yellow", "pink", "orange", "white"]
mots = ['Bleu', 'Rouge', 'Vert', 'Jaune', 'Rose', 'Orange', 'Blanc', 'Violet', 'Noir', 'Marron', 'Gris', 'Beige']


# Définition des fonctions
def réinitialiser():
    """Réinitialiser le compte à rebours pour recommencer le jeu"""
    global demarrer, score, compteur
    compteur = 30
    compteur_lbl['text'] = "Temps restant : " + str(compteur)
    score = 0
    label_score["text"] = "Score : " + str(score)
    demarrer = False
    canvas.after_cancel(repeat)

def incremente():
    """Définit le compte à rebours"""
    global compteur, demarrer, repeat
    demarrer = True
    if compteur > 0:
        compteur -= 1
        compteur_lbl['text'] = "Temps restant : " + str(compteur)
        repeat = canvas.after(1000, incremente)
    else:
        demarrer = False

def changement(color):
    """Change aléatoirement la couleur du mot en jeu"""
    global label_title, score
    if demarrer is True:
        if label_title["fg"] == color:
            score += 1
            label_score["text"] = "Score : " + str(score)
        label_title["text"] = rd.choice(mots)
        label_title["fg"] = rd.choice(couleurs)
        print(label_title["fg"], color)


##################

racine = tk.Tk()
racine.title("Jeu des couleurs")
racine.geometry("950x325")
racine.config(background="lavender")
canvas = tk.Canvas(racine, width=700, height=900, bg="lavender",cursor="plus", relief="raised")

# Ajout du mot en jeu
compteur_lbl = tk.Label(canvas, text="Temps restant : " + str(compteur), font=("", 16), bg="lavender")

label_title = tk.Label(canvas, text=rd.choice(mots), font=("lavender", 40), fg=rd.choice(couleurs), bg='lavender')

label_text = tk.Label(canvas, text="Cliquez sur le bouton correspondant à la couleur du mot affiché !", bg="lavender", font=("lavender", 20))
label_text2 = tk.Label(canvas, text="Bonne chance 😊", bg="lavender", font=("lavender", 20))
label_score = tk.Label(canvas, text="Score : " + str(score), bg="lavender", font=("lavender", 16))


# Ajout des boutons et de la commande qu'ils executent 
first_button = tk.Button(canvas, text="Démarrer", command=incremente)
second_button = tk.Button(canvas, text="Réinitialiser", command=réinitialiser)
third_button = tk.Button(canvas, text='Bleu', bg=couleurs[0], command=lambda: changement("blue"))
fourth_button = tk.Button(canvas, text='Rouge', bg=couleurs[1], command=lambda: changement("red"))
fifth_button = tk.Button(canvas, text='Vert', bg=couleurs[2], command=lambda: changement("green"))
sixth_button = tk.Button(canvas, text='Jaune', bg=couleurs[3], command=lambda: changement("yellow"))
seventh_button = tk.Button(canvas, text='Rose', bg=couleurs[4], command=lambda: changement("pink"))
eighth_button = tk.Button(canvas, text='Orange', bg=couleurs[5], command=lambda: changement("orange"))
ninth_button = tk.Button(canvas, text='Blanc', bg=couleurs[6], command=lambda: changement("white"))


# Affichage des différents éléments

label_text.pack()
label_text2.pack()
compteur_lbl.pack()
label_score.pack()
label_title.pack()

first_button.pack(side=tk.LEFT, pady=50)
second_button.pack(side=tk.RIGHT, pady=50)
third_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
fourth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
fifth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
sixth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
seventh_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
eighth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
ninth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
canvas.pack()


racine.mainloop()