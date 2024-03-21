import sqlite3 as sql

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
            cartes_prison INTEGER);
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
            INSERT INTO Joueurs(billets_500, billets_100, billets_50, billets_20, billets_10, billets_5, billets_1, cartes_prison)
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
        liste_terrains = [{"Rue de Courcelles": (100, 550)},
                        {"Avenue de la République": (120, 600)},
                        {"Avenue de Noeuil": (140, 750)},
                        {"Rue de Paradis": (160, 900)},
                        {"Boulevard Saint-Michel": (180, 950)},
                        {"Place Pigalle": (200, 1050)},
                        {"Rue La Fayette": (250, 1200)},
                        {"Boulevard des Cramptés": (300, 1500)},
                        {"Avenue Fauché": (350, 1800)},
                        {"Avenue Champs-NSI": (400, 2000)}]
        
        for i in liste_terrains:
            nom_rue = list(i.keys())[0]
            valeurs_rue = list(i.values())[0]
            cursor.execute("""
            INSERT INTO Terrains(nom, prix, loyer)
            VALUES(?, ?, ?);
            """, (nom_rue, valeurs_rue[0], valeurs_rue[1]))
            
        terrains.commit()
        
        cursor.close()
        terrains.close()
            
    creer_terrains()
    remplir_terrains()
    
# def cartes_commu():    
#     def creer_carte_commu():
#         cartes_commu = sql.connect("Databases/cartes_commu.db")
#         cursor = cartes_commu.cursor()
        
#         cursor.execute("""
#         CREATE TABLE IF NOT EXISTS cartes_communautes(
#            id_cartes INTEGER PRIMARY KEY AUTOINCREMENT,
#            nom VARCHAR(50),
#            effet VARCHAR(255));
#         """)
#         cartes_commu.commit()

#         cursor.close()
#         cartes_commu.close()

#     def remplir_cartes_commu():
#         cartes_commu = sql.connect("Databases/cartes_commu.db")
#         cursor = cartes_commu.cursor()
        
#         #{"Nom": (effet)}
#         liste_cartes_commu = [
#             {}
#         ]
        
#         for i in liste_cartes_commu:
#             nom_cartes = list(i.keys())[0]
#             effet_commu = list(i.values())[0]
#             cursor.execute("""
#             INSERT INTO cartes_commu(nom,effet)
#             VALUES(?,?);
#                            """,(nom_cartes,effet_commu))
            
#         cartes_commu.commit()

#         cursor.close()
#         cartes_commu.close()
       
#     creer_carte_commu() 
#     remplir_cartes_commu()
    
joueur()
terrain()
# cartes_commu()