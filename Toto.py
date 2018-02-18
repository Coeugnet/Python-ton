from tkinter import *

fenetre = Tk()
for numéroRangée in range(11):
	for numéroColonne in range(11):
		carré = Button(fenetre,width=6,height=3,bg="white")
		carré.grid(row=numéroRangée,column=numéroColonne)


mainloop()