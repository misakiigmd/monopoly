from Classes.classe import *
from Classes.interface import *
from Classes.db import *

j1 = Joueur("Marouan")
j2 = Joueur('Anaël')

app = MonopolyPlateau(size=6, joueur1=j1, joueur2=j2)
app.mainloop()