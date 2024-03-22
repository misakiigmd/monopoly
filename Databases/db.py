import os
import sqlite3 as sql

# Suppression des anciens fichiers (si ils existent) pour éviter l'insertion de la même rue plusieurs fois
def delete_old_files():
    if os.path.exists('Databases/cartes_communauté.db'):
        os.remove('Databases/cartes_communauté.db') 
    if os.path.exists('Databases/cartes_chance.db'):
        os.remove('Databases/cartes_chance.db') 
    if os.path.exists('Databases/joueurs.db'):
        os.remove('Databases/joueurs.db')
    if os.path.exists('Databases/terrains.db'):
        os.remove('Databases/terrains.db')

# Création et insertion des données dans la table CartesChance
def carte_chance():
        # Fonction pour créer la table
        def creer_cartes_chance():
            cartes_chance = sql.connect('Databases/cartes_chance.db')
            cursor = cartes_chance.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS CartesChance(
                id_carte INTEGER PRIMARY KEY AUTOINCREMENT,
                nom VARCHAR(50),
                effet VARCHAR(255));
            """)

            cartes_chance.commit()

            cursor.close()
            cartes_chance.close()
        
        # Fonction pour insérer les données dans la table
        def remplir_cartes_chance():
            cartes_chance = sql.connect('Databases/cartes_chance.db')
            cursor = cartes_chance.cursor()
            
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
            
            for i in liste_cartes_chance:
                nom_carte_chance = list(i.keys())[0]
                effet_carte_chance = list(i.values())[0]
                cursor.execute("""
                INSERT INTO CartesChance(nom, effet)
                VALUES(?, ?);
                """, (nom_carte_chance, effet_carte_chance))
                
            cartes_chance.commit()
            
            cursor.close()
            cartes_chance.close()
        
        # Exécution des deux sous-fonctions
        creer_cartes_chance()
        remplir_cartes_chance()
        
# Création et insertion des données dans la table CartesCommunauté
def carte_communauté():
        # Fonction pour créer la table
        def creer_cartes_communauté():
            cartes_communautés = sql.connect('Databases/cartes_communauté.db')
            cursor = cartes_communautés.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS CartesCommunauté(
                id_carte INTEGER PRIMARY KEY AUTOINCREMENT,
                nom VARCHAR(50),
                effet VARCHAR(255));
            """)

            cartes_communautés.commit()

            cursor.close()
            cartes_communautés.close()
        
        # Fonction pour insérer les données dans la table
        def remplir_cartes_communauté():
            carte_communautés = sql.connect('Databases/cartes_communauté.db')
            cursor = carte_communautés.cursor()
            
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
            
            for i in liste_cartes_communauté:
                nom_carte_communauté = list(i.keys())[0]
                effet_carte_communauté = list(i.values())[0]
                cursor.execute("""
                INSERT INTO CartesCommunauté(nom, effet)
                VALUES(?, ?);
                """, (nom_carte_communauté, effet_carte_communauté))
                
            carte_communautés.commit()
            
            cursor.close()
            carte_communautés.close()
        
        # Exécution des deux sous-fonctions
        creer_cartes_communauté()
        remplir_cartes_communauté()
    
# Création et insertion des données dans la table Joueurs
def joueur():
    # Fonction pour créer la table
    def creer_joueurs():
        joueurs = sql.connect('Databases/joueurs.db')
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
        
    # Fonction pour insérer les données dans la table
    def remplir_joueurs():
        joueurs = sql.connect('Databases/joueurs.db')
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
        
    # Exécution des deux sous-fonctions
    creer_joueurs()
    remplir_joueurs()
        
# Création et insertion des données dans la table Terrains
def terrain():
    # Fonction pour créer la table
    def creer_terrains():
        terrains = sql.connect('Databases/terrains.db')
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
        
    # Fonction pour insérer les données dans la table
    def remplir_terrains():
        terrains = sql.connect('Databases/terrains.db')
        cursor = terrains.cursor()
        
        # {"nom": (prix, loyer)}
        # Le loyer correspond au loyer de base (il dépend du nombre de maisons)
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
        
    # Exécution des deux sous-fonctions
    creer_terrains()
    remplir_terrains()
    
if __name__ == "__main__":
    delete_old_files()
    carte_communauté()
    carte_chance()
    joueur()
    terrain()