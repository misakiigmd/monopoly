class Propriété:
    def __init__(self, case) -> None:
        self.case = case
        self.prix = ...
        self.proprietaire = None
        self.loyer = ...
    
    def est_achete(self):
        return self.proprietaire != None

class Joueur:
    def __init__(self, nom, db) -> None:
        self.nom = nom
        self.billet = {500 :..., 100:..., 50:..., 20:..., 10:..., 5:..., 1:...}
        self.argents = self.billet[500]*500 + self.billet[100]*100 + self.billet[50]*50 + self.billet[20]*20 + self.billet[10]*10
        self.emplacement = 0
        self.proprietes = {} # set de propriété que le joueur achete
        
    def deplacer(self, nombre_de_case):
        """Déplacer un joueur de n case(s)"""
        self.emplacement += nombre_de_case
        # Case prison 
        if self.emplacement == 15: # si case police 
            self.emplacement == 5 #mettre à la prison

    def payer(self, somme):
        if somme < self.argents:
            return -1
        elif somme == self.argents:
            self.billets = {x : 0 for x in self.billets}
        else: 
            
            for billet in self.billets:
                if billet > somme:
                    pass
                else:
                    self.billets[billet] -= somme//billet
                    somme = somme - (somme//billet)*billet
    
    def acheter(self, propriete):
        if propriete.est_achete():
            return f'Cette propriété appartient déjà à {propriete.proprietaire()}'
        elif propriete in self.proprietes:
            return 'Cette maison vous appartient déjà ! '
        else:
            #récupération de billet en mode glouton
            if propriete.prix < self.argent:
                return 'Vous n\'avez pas assez d\'argent pour vous payer cette propriété !'
            else:
                self.payer()
                self.proprietes.add(propriete)
                propriete.proprietaire = self.nom
                return f'Cette propriété appartient désormais à {self.nom}'