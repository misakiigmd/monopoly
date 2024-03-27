# code de chaque carte chance
from classe import *

def libere_prison(joueur):
    """Libère la prison du joueur"""
    assert not isinstance(joueur, Joueur), "Il faut entrer un joueur"
    joueur.debloque()

def reculer_de_3(joueur):
    """Fait reculer le joueur de 3 cases"""
    assert not isinstance(joueur, Joueur), "Il fait entrer un joueur"
    joueur.deplacer(-3)

def erreur_banque50(joueur):
    """Erreur banque, le joueur reçoit 50€"""
    assert not isinstance(joueur, Joueur), "Il fait entrer un joueur"
    joueur.ajout