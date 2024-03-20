import sqlite3 as sql

def terrain():
    def creer_terrains():
        terrains = sql.connect("Databases/terrains.db")
        cursor = terrains.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Terrains(
            id_terrain INTEGER PRIMARY KEY AUTOINCREMENT,
            nom VARCHAR(50),
            prix INTEGER,
            loyer INTEGER);
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
    
terrain()