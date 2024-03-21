import tkinter as tk

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

        # Créer la grille de carrés sur les côtés avec du texte
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    square = tk.Canvas(self, width=square_size, height=square_size, highlightthickness=0, bg="lightgray")
                    square.grid(row=i, column=j+1, padx=5, pady=5)
                    label = tk.Label(square, text=f"{i*size + j + 1}")
                    label.place(relx=0.5, rely=0.5, anchor="c")

        # Placer des pions déplaçables sur le plateau
        self.place_piece(size -1, size-1.5, "red")
        self.place_piece(size -0.5, size+0.5, "blue")

        # Créer les colonnes pour les joueurs 1 et 2
        player1_column = tk.Canvas(self, width=100, height=window_height, bg="lightblue")
        player1_column.grid(row=0, column=0, rowspan=size, padx=5, pady=5)

        player2_column = tk.Canvas(self, width=100, height=window_height, bg="lightgreen")
        player2_column.grid(row=0, column=size+1, rowspan=size, padx=5, pady=5)

    def place_piece(self, row, col, color):
        square_size = 100
        piece = tk.Canvas(self, width=30, height=30, highlightthickness=0, bg="white")
        piece.create_oval(5, 5, 25, 25, fill=color)
        piece.place(x=col * square_size + square_size / 2 + 5 * (col + 1), y=row * square_size + square_size / 2 + 5 * (row + 1), anchor="c")

if __name__ == "__main__":
    app = MonopolyPlateau(size=6)
    app.mainloop()
