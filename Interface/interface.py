import tkinter as tk
from tkinter import messagebox
from time import sleep
import sqlite3 as sql
from coordonnées import coord, noms

db_name = 'Databases/main.db'


class MonopolyPlateau(tk.Tk):
    def __init__(self, size=6):
        super().__init__()

        self.size = size
        self.pieces = []  # Liste pour stocker les références aux pièces créées
        self.piece1_case = {0: (4.5, 7), 1: (4.5, 6), 2: (4.5, 5), 3: (4.5, 4), 4: (4.5, 3), 5: (4.5, 2), 6: (3.5, 2), 7: (2.5, 2), 8: (1.5, 2), 9: (0.5, 2), 10: (-0.5, 2), 11: (-0.5, 3), 12: (-0.5, 4), 13: (-0.5, 5), 14: (-0.5, 6), 15: (-0.5, 7), 16: (0.5, 7), 17: (1.5, 7), 18: (2.5, 7), 19: (3.5, 7)}
        self.piece1_number = 0
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
        self.place_piece(size - 1, size + 1, "lightblue")

        player1_column = tk.Canvas(self, width=100, height=window_height, bg="lightblue")
        player1_column.grid(row=0, column=0, rowspan=size, padx=50, pady=50)
        player1_label = tk.Label(player1_column, bg="lightblue", text="Joueur 1\n\nArgent Total = $1000\n\nPropriétés: ")
        player1_label.pack(side="top")

        player2_column = tk.Canvas(self, width=100, height=window_height, bg="lightgreen")
        player2_column.grid(row=0, column=size+1, rowspan=size, padx=50, pady=5)
        player2_label = tk.Label(player2_column, bg="lightgreen", text="Joueur 2\n\nArgent Total = $1000\n\nPropriétés: ")
        player2_label.pack(side="top")

        button_section = tk.Frame(self, width=200, height=window_height, bg="white")
        button_section.grid(row=0, column=size+2, rowspan=size, padx=5, pady=5)

        def add_button(text):
            button = tk.Button(button_section, text=text)
            button.pack(side="top", padx=5, pady=5)
            if text == "Acheter":
                button.config(command=lambda: remove_button(button))
            if text == "Passer":
                button.config(command=lambda: move_piece(0))

        @staticmethod 
        def move_piece(piece_num): 
            print(self.piece1_number) 
            if (self.piece1_number == 18):
                self.piece1_number = 0
            else:
                self.piece1_number += 1
            square_size = 100
            piece, old_row, old_col = self.pieces[piece_num]
            new_row, new_col = self.piece1_case[self.piece1_number]
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
        piece = tk.Canvas(self, width=30, height=30, highlightthickness=0)
        piece.create_oval(5, 5, 25, 25, fill=color)
        piece.place(x=col * square_size + square_size / 2 + 5 * (col + 1), y=row * square_size + square_size / 2 + 5 * (row + 1), anchor="c")
        self.pieces.append([piece, row, col])  # Ajouter la référence à la liste des pièces

    
if __name__ == "__main__":
    app = MonopolyPlateau(size=6)
    app.mainloop()
    sleep(10)