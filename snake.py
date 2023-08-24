import customtkinter as ctk
import tkinter as tk
from settings import *

class Game(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')
        self.title('Snake')

        #* Layout
        columns = list(range(FIELDS[0]))
        self.columnconfigure(columns, weight = 1, uniform = 'a')
        
        row = list(range(FIELDS[1]))
        self.columnconfigure(row, weight = 1, uniform = 'a')
        



        #*Run
        self.mainloop()


Game()