import tkinter as tk
from tkinter import messagebox, PhotoImage
from time import sleep
import sqlite3 as sql
from coordonnées import coord, noms
from classe import *

db_name = 'Databases/main.db'


class MonopolyPlateau(tk.Tk):
    def __init__(self, size=6):
        super().__init__()

        self.size = size
        self.pieces = []  # Liste pour stocker les références aux pièces créées
        self.piece1_case = {0: (4.5, 7), 1: (4.5, 6), 2: (4.5, 5), 3: (4.5, 4), 4: (4.5, 3), 5: (4.5, 2.25), 6: (3.6, 2.25), 7: (2.6, 2.25), 8: (1.7, 2.25), 9: (0.8, 2.25), 10: (-0.3, 2.25), 11: (-0.3, 3), 12: (-0.3, 4), 13: (-0.3, 5), 14: (-0.3, 6), 15: (-0.3, 7.2), 16: (0.8, 7.2), 17: (1.7, 7.2), 18: (2.6, 7.2), 19: (3.6, 7.2), 20: (4.5, 7)}
        self.piece2_case = {0: (5.1, 7), 1: (5.1, 6), 2: (5.1, 5), 3: (5.1, 4), 4: (5.1, 3), 5: (5.1, 2.25), 6: (4.1, 2.25), 7: (3.1, 2.25), 8: (2.2, 2.25), 9: (1.2, 2.25), 10: (0.2, 2.25), 11: (0.2, 3), 12: (0.2, 4), 13: (0.2, 5), 14: (0.2, 6), 15: (0.2, 7.2), 16: (1.2, 7.2), 17: (2.3, 7.2), 18: (3.2, 7.2), 19: (4.1, 7.2), 20: (5.1, 7)}
        self.piece1_number = 1
        self.piece2_number = 1
        self.joueur1 = Joueur("Morgan")
        self.joueur2 = Joueur("Yanis")
        self.attributes('-fullscreen', True)
        self.bind('<Escape>', lambda e: self.destroy())

        self.resizable(False, False)

        square_size = 100
        window_width = square_size * size + (size + 1) * 5 + 200
        window_height = square_size * size + (size + 1) * 5

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
        menu1.add_command(label="Quitter", command=self.destroy)
        menubar.add_cascade(label="Paramètres", menu=menu1)

        menu2 = tk.Menu(menubar, tearoff=0)
        menubar.add_command(label="Quitter", command=self.destroy)

        self.config(menu=menubar)

        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    square = tk.Canvas(self, width=square_size, height=square_size, highlightthickness=0, bg="lightgray")
                    square.grid(row=i, column=j+1, padx=2, pady=1)
                    label = tk.Label(square, bg="lightgray", text=f"{noms[coord[i*size + j + 1]]}")
                    label.place(relx=0.5, rely=0.5, anchor="c")

        self.place_piece(size - 1.5, size + 1, "lightgreen")
        self.place_piece(size - 0.9, size + 1, "lightblue")

        player1_column = tk.Canvas(self, width=100, height=window_height, bg="lightblue")
        player1_column.grid(row=0, column=0, rowspan=size, padx=50, pady=50)
        player_billets = self.joueur1.billets
        player1_label = tk.Label(player1_column, bg="lightblue", text=f"Joueur 1\n\nArgent Total = {self.joueur1.argent}D\n\nBillets:\n {self.joueur1.format_billets()}\n\nPropriétés: ")
        player1_label.pack(side="top")

        player2_column = tk.Canvas(self, width=100, height=window_height, bg="lightgreen")
        player2_column.grid(row=0, column=size+1, rowspan=size, padx=50, pady=5)
        player2_label = tk.Label(player2_column, bg="lightgreen", text=f"Joueur 2\n\nArgent Total = {self.joueur1.argent}D\n\nBillets:\n {self.joueur2.format_billets()}\n\nPropriétés: ")
        player2_label.pack(side="top")

        button_section = tk.Frame(self, width=200, height=window_height, bg="white")
        button_section.grid(row=0, column=size+2, rowspan=size, padx=5, pady=5)
        
        # Load the image
        self.board_image = PhotoImage(file="Images\Logo.png").subsample(2, 2)  # Replace "your_image_file.png" with your image file path

        # Create a label to display the image
        self.image_label = tk.Label(self, image=self.board_image)

        # Place the label in the middle of the board
        middle_row = size // 2
        middle_col = size // 2
        self.image_label.place(x=157.5 + middle_col * square_size + square_size / 2 + 5 * (middle_col + 1),
                               y=middle_row * square_size + square_size / 2 + 5 * (middle_row + 1) - 65,
                               anchor="c")

        def add_button(text):
            button = tk.Button(button_section, text=text)
            button.pack(side="top", padx=5, pady=5)
            if text == "Acheter":
                button.config(command=lambda: move_piece(1))
            if text == "Passer":
                button.config(command=lambda: move_piece(0))
            

        @staticmethod 
        def move_piece(piece_num): 
            piece_case = self.piece1_case
            piece_number = self.piece1_number
            if (piece_num == 1):
                piece_case = self.piece2_case
                piece_number = self.piece2_number
    
                if (self.piece2_number == 19):
                    self.piece2_number = 0
                else:
                    self.piece2_number += 1
            else:
                if (self.piece1_number == 19):
                    self.piece1_number = 0
                else:
                    self.piece1_number += 1
                
            square_size = 100
            piece, old_row, old_col = self.pieces[piece_num]
            new_row, new_col = piece_case[piece_number]
            piece.place(x=new_col * square_size + square_size / 2 + 5 * (new_col + 1), y=new_row * square_size + square_size / 2 + 5 * (new_row + 1), anchor="c")
            self.pieces[piece_num] = [piece, new_row, new_col]
            print(new_row, new_col)

        def remove_button(button):
            button.pack_forget()

        add_button("Acheter")
        add_button("Passer")
        add_button("Lancer le dé")        

    def place_piece(self, row, col, color):
        square_size = 100
        piece = tk.Canvas(self, width=30, height=30, highlightthickness=0, bg="lightgray")
        piece.create_oval(5, 5, 25, 25, fill=color)
        piece.place(x=col * square_size + square_size / 2 + 5 * (col + 1), y=row * square_size + square_size / 2 + 5 * (row + 1), anchor="c")
        self.pieces.append([piece, row, col])  # Ajouter la référence à la liste des pièces

    
if __name__ == "__main__":
    app = MonopolyPlateau(size=6)
    app.mainloop()
    sleep(10)