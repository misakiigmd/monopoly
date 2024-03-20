import sqlite3 as sql

def creer_terrains():
    terrains = sql.connect("terrains.db")
    cursor = terrains.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Terrains(
        id_terrain INTEGER AUTO_INCREMENT,
        nom VARCHAR(50),
        prix INTEGER,
        loyer INTEGER,
        PRIMARY KEY(id_terrain));
    """)

    terrains.commit()

def remplir_terrains():
    ...