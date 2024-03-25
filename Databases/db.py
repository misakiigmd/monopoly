import os
import sqlite3 as sql

# Suppression de l'ancien fichier (si il existe) pour éviter l'insertion de la même donnée plusieurs fois
def delete_old_file():
    if os.path.exists('Databases/main.db'):
        os.remove('Databases/main.db')
        
# Création et insertion des données dans les différentes tables
def main():
    delete_old_file()
    
    # Connection au fichier de base de données
    db = sql.connect('Databases/main.db')
    cursor = db.cursor()

    # Création de la table CartesChance
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CartesChance(
        id_carte INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(50),
        effet VARCHAR(255));
    """)
    
    # {"nom": "effet"}
    liste_cartes_chance = [{"CCH1": ""},
                    {"CCH2": ""},
                    {"CCH3": ""},
                    {"CCH4": ""},
                    {"CCH5": ""},
                    {"CCH6": ""},
                    {"CCH7": ""},
                    {"CCH8": ""},
                    {"CCH9": ""},
                    {"CCH10": ""},
                    {"CCH11": ""},
                    {"CCH12": ""},
                    {"CCH13": ""},
                    {"CCH14": ""},
                    {"CCH15": ""}]
    
    # Insertion des données définies au dessus
    for i in liste_cartes_chance:
        nom_carte_chance = list(i.keys())[0]
        effet_carte_chance = list(i.values())[0]
        cursor.execute("""
        INSERT INTO CartesChance(nom, effet)
        VALUES(?, ?);
        """, (nom_carte_chance, effet_carte_chance))
        
    # Création de la table CartesCommunauté
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CartesCommunauté(
        id_carte INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(50),
        effet VARCHAR(255));
    """)
    
    # {"nom": "effet"}
    liste_cartes_communauté = [{"CCO1": ""},
                    {"CCO2": ""},
                    {"CCO3": ""},
                    {"CCO4": ""},
                    {"CCO5": ""},
                    {"CCO6": ""},
                    {"CCO7": ""},
                    {"CCO8": ""},
                    {"CCO9": ""},
                    {"CCO10": ""},
                    {"CCO11": ""},
                    {"CCO12": ""},
                    {"CCO13": ""},
                    {"CCO14": ""},
                    {"CCO15": ""}]
    
    # Insertion des données définies au dessus
    for i in liste_cartes_communauté:
        nom_carte_communauté = list(i.keys())[0]
        effet_carte_communauté = list(i.values())[0]
        cursor.execute("""
        INSERT INTO CartesCommunauté(nom, effet)
        VALUES(?, ?);
        """, (nom_carte_communauté, effet_carte_communauté))
            
    # Création de la table Joueurs
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
    
    nombre_joueurs = 2
    
    # Insertion du nombre de billets et de carte prisons de base autant de fois qu'il y a de joueurs
    for i in range(nombre_joueurs):
        cursor.execute("""
        INSERT INTO Joueurs(billets_500, billets_100, billets_50, billets_20, billets_10, billets_5, billets_1, cartes_prisons)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?);
        """, (1, 1, 1, 2, 3, 5, 5, 0))

    # Création de la table Terrains
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
    
    # {"nom": (prix, loyer)}
    # Le loyer correspond au loyer de base (il dépend du nombre de maisons)
    liste_terrains = [{"Rue de Courcelles": (65, 30)},
                    {"Avenue de la République": (70, 40)},
                    {"Avenue de Noeuil": (105, 50)},
                    {"Rue de Paradis": (110, 60)},
                    {"Boulevard Saint-Michel": (160, 70)},
                    {"Place Pigalle": (165, 80)},
                    {"Rue La Fayette": (215, 120)},
                    {"Boulevard des Cramptés": (230, 130)},
                    {"Avenue Fauché": (320, 170)},
                    {"Avenue Champs-NSI": (330, 180)}]
    
    # Insertion des données définies au dessus, ainsi que le nombre de maisons de base (0)
    for i in liste_terrains:
        nom_rue = list(i.keys())[0]
        valeurs_rue = list(i.values())[0]
        cursor.execute("""
        INSERT INTO Terrains(nom, prix, loyer, maisons)
        VALUES(?, ?, ?, ?);
        """, (nom_rue, valeurs_rue[0], valeurs_rue[1], 0))
        
    db.commit()
    
    cursor.close()
    db.close()
        
if __name__ == "__main__":
    main()