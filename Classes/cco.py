# code de chaque carte communauté
from classe import*

def medecin(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.payer(50)

def prix_beauté(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.ajouter_billets(100,1)
    joueur.ajouter_billets(50,1)

def prison(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.allez_prison()

def huissier(joueur):
    assert not isinstance(joueur, Joueur)
    joueur.payer(200)

def héritage(joueur):
    assert not isinstance(joueur, Joueur)
    joueur.ajouter_billets(100,2)

def hopital(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.payer(300)
    
def erreur_banque25(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.ajouter_billets(20, 1)
    joueur.ajouter_billets(5, 1)
    
def erreur_banque75(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.ajouter_billets(50, 1)
    joueur.erreurbanque25(joueur)
    
def erreur_banque100(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.ajouter_billets(50, 2)
    
def erreur_banque50(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.ajouter_billets(50, 1)

def mots_croises(joueur):
    assert not isinstance(joueur,Joueur)
    joueur.ajouter_billets(50,1)
