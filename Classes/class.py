class Propriete:
    def __init__(self, case, db) -> None:
        self.case = case
        self.prix = ...
        self.proprietaire = None
        self.loyer = ...
    
    liste_propriétés = {...}
    
    def est_achete(self):
        return self.proprietaire != None
    
    @staticmethod
    def est_propriete(num_case):
        return num_case in Propriete.liste_propriétés

class Joueur:
    def __init__(self, nom, db) -> None:
        self.nom = nom
        self.billets = {500 :..., 100:..., 50:..., 20:..., 10:..., 5:..., 1:...}
        self.argent = self.billets[500]*500 + self.billets[100]*100 + self.billets[50]*50 + self.billets[20]*20 + self.billets[10]*10
        self.emplacement = 0
        self.proprietes = {} # set de propriété que le joueur achete
        self.bloque = 0
        
    def deplacer(self, nombre_de_case):
        """Déplacer un joueur de n case(s)"""
        self.emplacement += nombre_de_case
        # Case prison 
        if self.emplacement == 15: # si case police 
            self.emplacement == 5 #mettre à la prison
            self.bloque = 2
        elif ... : 
            ...
    def payer(self, somme):
        if somme > self.argent:
            return -1
        elif somme == self.argent:
            self.billets  = {x : 0 for x in self.billets }
        else: 
            
            for billets in self.billets :
                if billets > somme:
                    pass
                else:
                    self.billets[billets] -= somme//billets             
                    somme = somme - (somme//billets) *billets     
    def acheter(self, propriete):
        assert len(self.proprietes) >= 3, 'Vous possedez déjà 3 propriétés'
        if propriete.est_achete():
            return f'Cette propriété appartient déjà à {propriete.proprietaire()}'
        elif propriete in self.proprietes:
            return 'Cette maison vous appartient déjà !'
        else:
            #récupération de billets en mode glouton
            if propriete.prix < self.argent:
                return 'Vous n\'avez pas assez d\'argent pour vous payer cette propriété !'
            else:
                self.payer()
                self.proprietes.add(propriete)
                propriete.proprietaire = self.nom
                return f'Cette propriété appartient désormais à {self.nom}'


    def payer_loyer(self, propriete):
        if not propriete.est_achete():
            print('la propriété n\'est pas encore achetée')
            r = input('Voulez-vous l\'acheter ? [Y/N] : ')
            if  r.upper()[0] == "Y":
                self.acheter(propriete)
            else:
                return 'Cette propriété ne vous appartient pas et vous ne voulez pas l\'acheter'
        elif self.nom == propriete.proprietaire:
            return 'Cette propriété vous appartient'
        else:
            somme = propriete.prix
            if somme > self.argent:
                return f'{self.name} a perdu la partie'
            
            elif somme == self.argent:
                for i in self.billets:
                    temp = self.billets[i]
                    self.billets[i] = 0
                    propriete.proprietaire.billets[i] += temp
            
            else:
                ...