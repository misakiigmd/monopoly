import os
import sqlite3 as sql

def delete_old_files():
    if os.path.exists('cartes_commu.db'):
        os.remove('cartes_commu.db') 
    if os.path.exists('cartes_chance.db'):
        os.remove('cartes_chance.db') 
    if os.path.exists('joueurs.db'):
        os.remove('joueurs.db')
    if os.path.exists('terrains.db'):
        os.remove('terrains.db') 
        
delete_old_files()
    
def joueur():
    def creer_joueurs():
        joueurs = sql.connect("Databases/joueurs.db")
        cursor = joueurs.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Joueurs(
            id_joueur INTEGER PRIMARY KEY AUTOINCREMENT,
            billets_500 INTEGER,
            billets_100 INTEGER,
            billets_50 INTEGER,
            billets_20 INTEGER,
            billets_10 INTEGER,
            billets_5 INTEGER,
            billets_1 INTEGER,
            cartes_prisons INTEGER);
        """)
        
        joueurs.commit()
        
        cursor.close()
        joueurs.close()
        
    def remplir_joueurs():
        joueurs = sql.connect("Databases/joueurs.db")
        cursor = joueurs.cursor()
        
        nombre_joueurs = 2
        
        for i in range(nombre_joueurs):
            cursor.execute("""
            INSERT INTO Joueurs(billets_500, billets_100, billets_50, billets_20, billets_10, billets_5, billets_1, cartes_prisons)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?);
            """, (1, 1, 1, 2, 3, 5, 5, 0))
            
        joueurs.commit()
        
        cursor.close()
        joueurs.close()
        
    creer_joueurs()
    remplir_joueurs()
        
def terrain():
    def creer_terrains():
        terrains = sql.connect("Databases/terrains.db")
        cursor = terrains.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Terrains(
            id_terrain INTEGER PRIMARY KEY AUTOINCREMENT,
            nom VARCHAR(50),
            prix INTEGER,
            loyer INTEGER,
            maisons INTEGER,
            appartenance INTEGER,
            FOREIGN KEY(appartenance) REFERENCES joueurs(id_joueur));
        """)

        terrains.commit()
        
        cursor.close()
        terrains.close()

    def remplir_terrains():
        terrains = sql.connect("Databases/terrains.db")
        cursor = terrains.cursor()
        
        # {"Nom": (Prix, Loyer)}
        liste_terrains = [{"Rue de Courcelles": (65, 550)},
                        {"Avenue de la République": (70, 600)},
                        {"Avenue de Noeuil": (105, 750)},
                        {"Rue de Paradis": (110, 900)},
                        {"Boulevard Saint-Michel": (160, 950)},
                        {"Place Pigalle": (165, 1050)},
                        {"Rue La Fayette": (215, 1200)},
                        {"Boulevard des Cramptés": (230, 1500)},
                        {"Avenue Fauché": (320, 1800)},
                        {"Avenue Champs-NSI": (330, 2000)}]
        
        for i in liste_terrains:
            nom_rue = list(i.keys())[0]
            valeurs_rue = list(i.values())[0]
            cursor.execute("""
            INSERT INTO Terrains(nom, prix, loyer, maisons)
            VALUES(?, ?, ?, ?);
            """, (nom_rue, valeurs_rue[0], valeurs_rue[1], 0))
            
        terrains.commit()
        
        cursor.close()
        terrains.close()
            
    creer_terrains()
    remplir_terrains()
    
joueur()
terrain()