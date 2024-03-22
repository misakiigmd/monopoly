import tkinter as tk
from tkinter import messagebox
from time import sleep

class MonopolyPlateau(tk.Tk):
    def __init__(self, size=6):
        super().__init__()

        self.size = size

        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.destroy())
        
        # Empêcher le redimensionnement de la fenêtre
        self.resizable(False, False)

        # Calculer la taille de la fenêtre
        square_size = 100
        window_width = square_size * size + (size + 1) * 5 + 200  # Ajout de 200 pour les colonnes des joueurs
        window_height = square_size * size + (size + 1) * 5

        # Placer la fenêtre au milieu de l'écran
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        def recommencer():
            messagebox.askyesno("Souhaitez-vous recommencer la partie ?", "Bravo!")

        menubar = tk.Menu(self)

        menu1 = tk.Menu(menubar, tearoff=0)
        menu1.add_command(label="Recommencer", command=recommencer)
        menu1.add_separator()
        menu1.add_command(label="Quitter", command=self.quit)
        menubar.add_cascade(label="Paramètres", menu=menu1)

        menu2 = tk.Menu(menubar, tearoff=0)
        menubar.add_command(label="Quitter", command=self.quit)

        self.config(menu=menubar)
        
        # Créer la grille de carrés sur les côtés avec du texte
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    square = tk.Canvas(self, width=square_size, height=square_size, highlightthickness=0, bg="lightgray")
                    square.grid(row=i, column=j+1, padx=5, pady=5)
                    label = tk.Label(square, text=f"{i*size + j + 1}")
                    label.place(relx=0.5, rely=0.5, anchor="c")

        # Placer des pions déplaçables sur le plateau
        self.place_piece(size -1, size-1.5, "lightgreen")
        self.place_piece(size -0.5, size+0.5, "lightblue")

        # Créer les colonnes pour les joueurs 1 et 2
        player1_column = tk.Canvas(self, width=100, height=window_height, bg="lightblue")
        player1_column.grid(row=0, column=0, rowspan=size, padx=50, pady=50)
        player1_label = tk.Label(player1_column, bg="lightblue", text="Joueur 1\n\nArgent Total = $1000\n\nPropriétés: ")
        player1_label.pack(side="top")

        player2_column = tk.Canvas(self, width=100, height=window_height, bg="lightgreen")
        player2_column.grid(row=0, column=size+1, rowspan=size, padx=50, pady=5)
        player2_label = tk.Label(player2_column, bg="lightgreen", text="Joueur 2\n\nArgent Total = $1000\n\nPropriétés: ")
        player2_label.pack(side="top")

        # Créer une section pour les boutons à droite du joueur 2
        button_section = tk.Frame(self, width=200, height=window_height, bg="white")
        button_section.grid(row=0, column=size+2, rowspan=size, padx=5, pady=5)

       # Fonction pour ajouter des boutons à la section
        def add_button(text):
            button = tk.Button(button_section, text=text)
            button.pack(side="top", padx=5, pady=5)
            if text == "Acheter":
                button.config(command=lambda: remove_button(button))  # Configuration du bouton "Acheter" pour appeler remove_button

        # Fonc  tion pour retirer un bouton de la section
        def remove_button(button):
            button.pack_forget()

        # Exemple d'ajout de boutons
        add_button("Acheter")
        add_button("Passer")
        add_button("Lancer le dé")        

    def place_piece(self, row, col, color):
        square_size = 100
        piece = tk.Canvas(self, width=30, height=30, highlightthickness=0, bg="white")
        piece.create_oval(5, 5, 25, 25, fill=color)
        piece.place(x=col * square_size + square_size / 2 + 5 * (col + 1), y=row * square_size + square_size / 2 + 5 * (row + 1), anchor="c")

if __name__ == "__main__":
    app = MonopolyPlateau(size=6)
    app.mainloop()
    sleep(10)
    app
