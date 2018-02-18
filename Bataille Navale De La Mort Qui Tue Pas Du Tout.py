from tkinter import *
import string

def initFenetre(titre, couleur) :
    fenetre = Tk()
    fenetre.title(titre)
    colonne = string.ascii_uppercase[:10]
    for numéroRangée in range(11):
    	for numéroColonne in range(11):
    		if numéroColonne == 0 and numéroRangée == 0:
    			carré = Button(fenetre,width=6,height=3,text=numéroRangée,bg="black")
    			carré.grid(row=numéroRangée,column=numéroColonne)
    		elif numéroColonne == 0 and numéroRangée != 0:
    			carré = Button(fenetre,width=6,height=3,text=numéroRangée,bg=couleur)
    			carré.grid(row=numéroRangée,column=numéroColonne)
    		elif numéroRangée == 0 and numéroColonne != 0:
    			carré = Button(fenetre,width=6,height=3,text=colonne[numéroColonne-1],bg=couleur)
    			carré.grid(row=numéroRangée,column=numéroColonne)
    		else:
    			carré = Button(fenetre,width=6,height=3,bg="#4271f4")
    			carré.grid(row=numéroRangée,column=numéroColonne)

fenetre1 = initFenetre("Mes bateaux","#ccff66")
fenetre2 = initFenetre("Tes bateaux - albatar","#f44141")

mainloop()
