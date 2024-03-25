import os
import random
import sqlite3 as sql
db_path = 'Databases\main.db'


# Suppression de l'ancien fichier (si il existe) pour éviter l'insertion de la même donnée plusieurs fois
def delete_old_file():
    if os.path.exists(db_path):
        os.remove(db_path)
        
# Création et insertion des données dans les différentes tables
def main():
    delete_old_file()
    
    # Connection au fichier de base de données
    db = sql.connect(db_path)
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
        chemin VARCHAR(50));
    """)
    
    # {"nom": "chemin"}
    liste_cartes_communauté = [{"CCO1": "Images/cco1.png"},
                    {"CCO2": "Images/cco2.png"},
                    {"CCO3": "Images/cco3.png"},
                    {"CCO4": "Images/cco4.png"},
                    {"CCO5": "Images/cco5.png"},
                    {"CCO6": "Images/cco6.png"},
                    {"CCO7": "Images/cco7.png"},
                    {"CCO8": "Images/cco8.png"},
                    {"CCO9": "Images/cco9.png"},
                    {"CCO10": "Images/cco10.png"},
                    {"CCO11": "Images/cco11.png"},
                    {"CCO12": "Images/cco12.png"},
                    {"CCO13": "Images/cco13.png"}]
    
    # Insertion des données définies au dessus
    for i in liste_cartes_communauté:
        nom_carte_communauté = list(i.keys())[0]
        chemin_carte_communauté = list(i.values())[0]
        cursor.execute("""
        INSERT INTO CartesCommunauté(nom, chemin)
        VALUES(?, ?);
        """, (nom_carte_communauté, chemin_carte_communauté))
            
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
        id_terrain INTEGER PRIMARY KEY,
        nom VARCHAR(50),
        prix INTEGER,
        loyer INTEGER,
        maisons INTEGER,
        appartenance INTEGER,
        FOREIGN KEY(appartenance) REFERENCES joueurs(id_joueur));
    """)
    
    # {"nom": (prix, loyer)}
    # Le loyer correspond au loyer de base (il dépend du nombre de maisons)
    liste_terrains = [{"Rue de Courcelles": (1, 65, 30)},
                    {"Avenue de la République": (2, 70, 40)},
                    {"Avenue de Noeuil": (4, 105, 50)},
                    {"Rue de Paradis": (6, 110, 60)},
                    {"Boulevard Saint-Michel": (8, 160, 70)},
                    {"Place Pigalle": (9, 165, 80)},
                    {"Rue La Fayette": (12, 15, 120)},
                    {"Boulevard des Cramptés": (13, 230, 130)},
                    {"Avenue Fauché": (17, 320, 170)},
                    {"Avenue Champs-NSI": (18, 330, 180)}]
    
    # Insertion des données définies au dessus, ainsi que le nombre de maisons de base (0)
    for i in liste_terrains:
        nom_rue = list(i.keys())[0]
        valeurs_rue = list(i.values())[0]
        cursor.execute("""
        INSERT INTO Terrains(id_terrain, nom, prix, loyer, maisons)
        VALUES(?, ?, ?, ?, ?);
        """, (valeurs_rue[0], nom_rue, valeurs_rue[1], valeurs_rue[2], 0))
        
    db.commit()
    
    cursor.close()
    db.close()
    
def billets(id):
    db = sql.connect(db_path)
    cursor = db.cursor()
    
    cursor.execute("""
    SELECT billets_500, billets_100, billets_50, billets_20, billets_10, billets_5, billets_1 FROM Joueurs
    WHERE id_joueur = ?""", (str(id)))
    
    result = cursor.fetchone() 
    
    # Transformation du tuple en liste
    result_list = list(result)
    
    cursor.close()
    db.close()
    
    print(result_list)
        
def carteco_random():
    db = sql.connect(db_path)
    cursor = db.cursor()
    
    cursor.execute("""
    SELECT id_carte, chemin FROM CartesCommunauté""")
    
    results = cursor.fetchall()
    carte = random.randint(0, len(results) - 1)
        
    print(results[carte])
    
    cursor.close()
    db.close()
    
def cartech_random():
    db = sql.connect(db_path)
    cursor = db.cursor()
    
    cursor.execute("""
    SELECT id_carte, chemin FROM CartesChance""")
    
    results = cursor.fetchall()
    carte = random.randint(0, len(results) - 1)
        
    print(results[carte])
    
    cursor.close()
    db.close()
    
if __name__ == "__main__":
    main()