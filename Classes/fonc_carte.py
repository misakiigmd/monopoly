from classe import *

def libere_prison(joueur):
    """Libère la prison du joueur"""
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.debloque()

def reculer_de_3(joueur):
    """Fait reculer le joueur de 3 cases"""
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.deplacer(-3)

def aller_prison(joueur):
    """Aller tout droit en prison"""
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.aller_prison()
    

def medecin(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.payer(50)

def prix_beaute(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billets(100,1)
    joueur.ajouter_billets(50,1)

def prison(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.allez_prison()

def huissier(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.payer(200)

def heritage(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billets(100,2)

def hopital(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.payer(300)
    
def erreur_banque25(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billet(20, 1)
    joueur.ajouter_billet(5, 1)
    
def erreur_banque75(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billet(50, 1)
    joueur.erreurbanque25(joueur)
    
def erreur_banque100(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billet(50, 2)
    
def erreur_banque50(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billet(50, 1)# code de chaque carte communauté


def frais_de_scolarite(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.payer(50)

def amende_pour_ivresse(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.payer(200)

def amende_exces_de_vitesse(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.payer(100)

def allez_gare_atefaices(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.emplacement = 7

def allez_gare_gamelle(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.emplacement = 16

def mots_croises(joueur):
    assert not isinstance(joueur,Joueur), "Il faut entrer un joueur"
    joueur.ajouter_billets(50,1)
    
def anniversaire(joueur):
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    liste_joueurs = Joueur.liste_joueurs
    for j in liste_joueurs:
        j.payer(10)
    joueur.ajouter_billets(10, len(liste_joueurs))
    
def taxe25(joueur):
    assert not isinstance(joueur, Joueur),"Il faut entrer un joueur"
    if len(joueur.terrains) == 0:
        return "Vous n'avez pas de maison, il n'y a donc rien à payer" 
    else:
        liste_terrains = joueur.terrains
        for _ in liste_terrains:
            joueur.payer(25)

def taxe50(joueur):
    assert not isinstance(joueur, Joueur),"Il faut entrer un joueur"
    if len(joueur.terrains) == 0:
        return "Vous n'avez pas de maison, il n'y a donc rien à payer" 
    else:
        liste_terrains = joueur.terrains
        for _ in liste_terrains:
            joueur.payer(50)