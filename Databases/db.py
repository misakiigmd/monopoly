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
    # Connection au fichier de base de données
    db = sql.connect(db_path)
    cursor = db.cursor()

    # Création de la table CartesChance
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CartesChance(
        id_carte INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(50),
        chemin VARCHAR(50),
        effet VARCHAR(255));
    """)
    
    # {"nom": ("chemin", "effet")}
    liste_cartes_chance = [{"CCH1": ("Images/cch1.png", "Vous êtes libéré de prison. Cette carte peut être conservée jusqu'à ce qu'elle soit utilisée ou vendue.")},
                            {"CCH2": ("Images/cch2.png", "Reculez de 3 cases.")},
                            {"CCH3": ("Images/cch3.png", "Erreur de la banque en votre faveur, recevez 50D.")},
                            {"CCH4": ("Images/cch4.png", "Erreur de la banque en votre faveur, recevez 25D.")},
                            {"CCH5": ("Images/cch5.PNG", "Erreur de la banque en votre faveur, recevez 75D.")},
                            {"CCH6": ("Images/cch6.PNG", "Erreur de la banque en votre faveur, recevez 100D.")},
                            {"CCH7": ("Images/cch7.PNG", "Allez en prison. Avancez tout droit en prison.")},
                            {"CCH8": ("Images/cch8.PNG", "Allez en prison. Avancez tout droit en prison.")},
                            {"CCH9": ("Images/cch9.PNG", "Allez en prison. Avancez tout droit en prison.")},
                            {"CCH10": ("Images/cch10.PNG", "C'est votre anniversaire: chaque joueur doit vous donner 10D.")},
                            {"CCH11": ("Images/cch11.PNG", "Payez 50D pour des frais de scolarité.")},
                            {"CCH12": ("Images/cch12.PNG", "Amande pour ivresse: 200D.")},
                            {"CCH13": ("Images/cch13.PNG", "Amande pour excès de vitesse: 100D.")},
                            {"CCH14": ("Images/cch14.PNG", "Allez à la gare Atéfaiçes.")},
                            {"CCH15": ("Images/cch15.PNG", "Allez à la gare Gamelle.")}]
    
    # Insertion des données définies au dessus
    for i in liste_cartes_chance:
        nom_carte_chance = list(i.keys())[0]
        carte_chance = list(i.values())[0]
        cursor.execute("""
        INSERT INTO CartesChance(nom, chemin, effet)
        VALUES(?, ?, ?);
        """, (nom_carte_chance, carte_chance[0], carte_chance[1]))
        
    # Création de la table CartesCommunauté
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CartesCommunauté(
        id_carte INTEGER PRIMARY KEY AUTOINCREMENT,
        nom VARCHAR(50),
        chemin VARCHAR(50),
        effet VARCHAR(255));
    """)
    
    # {"nom": ("chemin", "effet")}
    liste_cartes_communauté = [{"CCO1": ("Images/cco1.png", "Vous êtes à l'hôpital, malheureusement on est aux USA donc pas de carte vitale. Payer 300D.")},
        {"CCO2": ("Images/cco2.png", "Vous êtes allé au médecin, malheureusement on est aux USA donc pas de carte vitale. Payer 50D.")},
        {"CCO3": ("Images/cco3.png", "C'est l'heure de payer le loyer. Si tu ne veux pas que les huissiers arrivent, payer 200D.")},
        {"CCO4": ("Images/cco4.png", "Erreur de la banque par un hasard de circonstance, la banque vous offre de l'argent. Vous avez de la chance. Recevez 25D.")},
        {"CCO5": ("Images/cco5.png", "Erreur de la banque par un hasard de circonstance, la banque vous offre de l'argent. Vous avez de la chance. Recevez 75D.")},
        {"CCO6": ("Images/cco6.png", "Erreur de la banque par un hasard de circonstance, la banque vous offre de l'argent. Vous avez de la chance. Recevez 100D.")},
        {"CCO7": ("Images/cco7.png", "Vous êtes arrivé premier au grand prix de beauté. Vous êtes magnifique. Recevez 150D.")},
        {"CCO8": ("Images/cco8.png", "Mamie est morte, c'est triste oui, mais rappelez-vous, l'héritage de Mamie est conséquent. Allez, fêtons votre nouvelle fortune. Recevez 200D.")},
        {"CCO9": ("Images/cco9.png", "Vous êtes arrivé premier au grand prix de mots croisés. Bravo. Recevez 50D.")},
        {"CCO10": ("Images/cco10.png", "Vous êtes un hors-la-loi. Allez en prison sans passer par la case départ.")},
        {"CCO11": ("Images/cco11.png", "Bonjour, nous sommes les taxes. Merci de bien vouloir payer 25D pour chaque maison et 50M pour chaque hôtel. Passez une bonne journée.")},
        {"CCO12": ("Images/cco12.png", "Bonjour, nous sommes les taxes. Merci de bien vouloir payer 50D pour chaque maison et 100M pour chaque hôtel. Passez une bonne journée.")},
        {"CCO13": ("Images/cco13.png", "Erreur de la banque par un hasard de circonstance, la banque vous offre de l'argent. Vous avez de la chance. Recevez 50D.")}]
    
    # Insertion des données définies au dessus
    for i in liste_cartes_communauté:
        nom_carte_communauté = list(i.keys())[0]
        carte_communauté = list(i.values())[0]
        cursor.execute("""
        INSERT INTO CartesCommunauté(nom, chemin, effet)
        VALUES(?, ?, ?);
        """, (nom_carte_communauté, carte_communauté[0], carte_communauté[1]))
            
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
        
def cartech_random():
    index = random.randint(1, 15)
    carte = f"cch{index}"
    return carte

def carteco_random():
    index = random.randint(1, 13)
    carte = f"cco{index}"
    return carte
    
if __name__ == "__main__":
    delete_old_file()
    main()
    cartech_random()