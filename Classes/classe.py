"""
tache : 
    changer payer pour qu'elle rendent de la monnaie si on doit payer 10e mais qu'il a ni des 10, ni des 5 ni des 1 
"""
from Classes.db import billets

class Terrain:    
    liste_terrain = set() # set emplacement de propriété
    
    def __init__(self, case, prix, loyer) -> None:
        """Terrain du jeu DuoPili"""
        self.case = case
        self.prix = prix
        self.proprietaire = None
        self.loyer = loyer
        Terrain.liste_terrain.add(self) # ajoute le terrain dans 'liste_terrain'
    
    
    def est_achete(self):
        """
        Renvoie : 
            True -> le terrain est acheté 
            False -> le terrain n'appartient à personnes
        """
        return self.proprietaire != None 
    
    @staticmethod
    def est_terrain(num_case):
        """
        Renvoie:
            True, Si la case est une case terrain
            False, Si la case n'est pas une case terrain
        """
        for terrain in Terrain.liste_terrain:
            if terrain.case == num_case:
                return True
        return False
    
    @staticmethod
    def terrain(num_case):
        """Renvoie le terrain présent à l'emplacement indiqué par 'num_case'"""
        for terrain in Terrain.liste_terrain:
            if terrain.case == num_case:
                return terrain
        raise Exception("Erreur : Aucun terrain trouvé pour cette case")


class Gare:
    
    liste_gare = set() # set emplacement des gares
    
    def __init__(self, case, prix, billet) -> None:
        """Terrain du jeu DuoPili"""
        self.case = case
        self.prix = prix
        self.proprietaire = None
        self.billet = billet
        Terrain.liste_terrain.add(self) # ajoute le terrain dans 'liste_terrain'
    
    
    def est_achete(self):
        """
        Renvoie : 
            True -> le terrain est acheté 
            False -> le terrain n'appartient à personnes
        """
        return self.proprietaire != None 
    
    @staticmethod
    def est_gare(num_case):
        """
        Renvoie:
            True, Si la case est une case terrain
            False, Si la case n'est pas une case terrain
        """
        for terrain in Terrain.liste_gare:
            if terrain.case == num_case:
                return True
        return False
    
    @staticmethod
    def gare(num_case):
        """Renvoie le terrain présent à l'emplacement indiqué par 'num_case'"""
        for gare in Terrain.liste_gare:
            if gare.case == num_case:
                return gare
        raise Exception("Erreur : Aucun terrain trouvé pour cette case")


class Joueur:
    def __init__(self, nom, nbr_billets=billets(1)):
        """Joueur du jeu Duopili"""
        assert len(nbr_billets) !=6, 'Il manque un type de billet dans la liste'
        self.nom = nom
        self.billets = {500 :nbr_billets[0], 100:nbr_billets[1], 50:nbr_billets[2], 20:nbr_billets[3], 10:nbr_billets[4], 5:nbr_billets[5], 1:nbr_billets[6]}
        self.argent = self.billets[500]*500 + self.billets[100]*100 + self.billets[50]*50 + self.billets[20]*20 + self.billets[10]*10 + self.billets[5]*5 + self.billets[1]
        self.emplacement = 0 # numero de la case où se trouve le joueur
        self.terrains = set() # set -> terrain du joueur
        self.gares = set()  # set -> gare du joueur
        self.bloque = 0 # bloqué (en cas de mise en prison)
            
    def deplacer(self, nombre_de_case):
        """Déplacer un joueur de n case(s)"""
        if self.emplacement + nombre_de_case >= 20:
            self.ajouter_billets(100, 1) # On donne 100€ à un joueur qui revient à la case départ
        self.emplacement = (self.emplacement + nombre_de_case) %20 # Si il réalise un tour complet, il revient à zero (modulo 20 car il y a 20 case au total)
        # Case prison ---------------------------------------------------------------
        if self.emplacement == 15: # si case police 
            self.emplacement == 5 #mettre à la prison
            self.bloque = 2 # bloqué durant 2 tours
        # Case terrain --------------------------------------------------------------    
        elif Terrain.est_terrain(self.emplacemment): # si joueur se trouve dans une case terrain 
            terrain = Terrain.terrain(self.emplacement) # terrain correspondant à la case où se trouve le joueur 
            if terrain.est_achete():
                self.payer_loyer(terrain)
            else:
                r = input("Voulez-vous acheter ce terrain ? [O/N] ")
                if r.lower() == "o":
                    terrain.acheter()
                else:
                    print('vous ne voulez pas acheter ce terrain')
        # Case chance ----------------------------------------------------------------
        elif ...:
            ...
        # Case communauté ------------------------------------------------------------
        elif ...:
            ...
        # Case taxe ------------------------------------------------------------------
        elif self.emplacement == 19:
            self.payer(100) # La taxe est de 100€
        # Case gare ------------------------------------------------------------------
        elif  Gare.est_gare(self.emplacement):
            ...
        
    def aller_prison(self):
        """Aller en prison"""
        self.emplacement = 5
        self.bloque = 2
        
    def ajouter_billets(self, val, nombre_billets):
        """Ajoute n billets de N"""
        assert not val in self.billets, "La valeur du billet n'existe pas"    
        self.billets[val] += nombre_billets
    
    def retirer_billets(self, val, nombres_billets):
        """Retire n billets de N"""
        assert not val in self.billets, "La valeur du billet n'existe pas"
        if self.billets[val] < nombres_billets:
            raise ValueError("Le joueur ne possède pas suffisament de billets")
        else:
            self.billets[val] -= nombres_billets   
            
    def format_billets(self):
        """Renvoyer les billets en string pour l'affichage"""
        return '\n'.join([f"{value} x {key}" for key, value in self.billets.items() if value != 0])

    def debloquer(self):
        self.bloque = 0
    def est_bloque(self):
        """Renvoie:
            True, si le joueur est bloqué
            False , sinon
        """
        return self.bloque > 0

    def payer(self, somme):
        """Le joueur paye une somme N à la banque"""
        if somme > self.argent:
            print(f'{self.nom} n\'a pas assez d\'argent pour cette opération')
            print('Il a donc perdu !!!')
        elif somme == self.argent:
            self.billets  = {x : 0 for x in self.billets } # Le joueur n'a plus d'argent mais continue a jouer
        else: 
            for billet in self.billets :
                if billet > somme:
                    pass
                else:
                    self.retirer_billets(billet, somme//billet)             
                    somme = somme - (somme//billet) *billet
    def acheter(self, terrain):
        """Le joueur achète un terrain """
        assert len(self.terrains) >= 3, 'Vous possedez déjà 3 propriétés'
        if terrain.est_achete():
            return f'Cette propriété appartient déjà à {terrain.proprietaire}'
        elif terrain in self.terrains:
            return 'Cette maison vous appartient déjà !'
        else:
            #récupération de billets en mode glouton
            if terrain.prix > self.argent:
                return 'Vous n\'avez pas assez d\'argent pour vous payer cette propriété !'
            else:
                self.payer(terrain.prix)
                self.terrains.add(terrain)
                terrain.proprietaire = self.nom
                return f'Cette propriété appartient désormais à {self.nom}'

    def acheter_gare(self, gare):
        """Le joueur achète un terrain """
        if gare.est_achete():
            return f'Cette gare appartient déjà à {gare.proprietaire}'
        elif gare in self.gares:
            return 'Cette gare vous appartient déjà !'
        else:
            #récupération de billets en mode glouton
            if gare.prix > self.argent:
                return 'Vous n\'avez pas assez d\'argent pour vous payer cette propriété !'
            else:
                self.payer(gare.prix)
                self.terrains.add(gare)
                gare.proprietaire = self.nom
                return f'Cette propriété appartient désormais à {self.nom}'

    def payer_loyer(self, terrain):
        """Le joueur doit payer le loyer"""
        if not terrain.est_achete():
            print('la propriété n\'est pas encore achetée')
            r = input('Voulez-vous l\'acheter ? [Y/N] : ')
            if  r.upper()[0] == "Y":
                self.acheter(terrain)
            else:
                return 'Cette propriété ne vous appartient pas et vous ne voulez pas l\'acheter, il n\'y a donc rien à acheter'
        elif self.nom == terrain.proprietaire:
            return 'Cette propriété vous appartient'
        else:
            somme = terrain.prix
            if somme > self.argent:
                return f"{self.name} n'a assez pour réaliser cette opération Il a perdu la partie"
            
            elif somme == self.argent:
                for i in self.billets:
                    temp = self.billets[i]
                    self.billets[i] = 0
                    terrain.proprietaire.ajouter_billets(i, temp)
            
            else:
                for billet in self.billets:
                    if somme >= billet:
                        nbr_billets = somme // billet
                        self.retirer_billets(billet, nbr_billets)
                        terrain.proprietaire.ajouter_billets(billet, nbr_billets)
                        somme -= billet*nbr_billets

    def payer_billet(self, gare):
        """Le joueur doit payer le loyer"""
        if not gare.est_achete():
            print('la gare n\'est pas encore achetée')
            r = input('Voulez-vous l\'acheter ? [Y/N] : ')
            if  r.upper()[0] == "Y":
                self.acheter(gare)
            else:
                return 'Cette gare ne vous appartient pas et vous ne voulez pas l\'acheter, il n\'y a donc rien à payer'
        elif self.nom == gare.proprietaire:
            return 'Cette gare vous appartient'
        else:
            somme = gare.prix
            if somme > self.argent:
                return f"{self.name} n'a pas assez pour réaliser cette opération, Il a donc perdu la partie "
            
            elif somme == self.argent:
                for i in self.billets:
                    temp = self.billets[i]
                    self.billets[i] = 0
                    gare.proprietaire.billets[i] += temp
            
            else:
                for billet in self.billets:
                    if somme >= billet:
                        nbr_billets = somme // billet
                        self.retirer_billets(nbr_billets, billet)
                        gare.proprietaire.ajouter_billets(nbr_billets, billet)
                        somme -= billet*nbr_billets