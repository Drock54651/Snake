import customtkinter as ctk
import tkinter as tk
from settings import *
from random import randint

class Game(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')
        self.title('Snake')

        #* Layout
        columns = list(range(FIELDS[0])) #! list from 0 to 19
        self.columnconfigure(columns, weight = 1, uniform = 'a')
        
        row = list(range(FIELDS[1]))
        self.rowconfigure(row, weight = 1, uniform = 'a')
        
        #TODO
        #* Snake
        self.snake = [START_POS, 
                      (START_POS[0] - 1, START_POS[1]), 
                      (START_POS[0] - 2, START_POS[1])] #! each tuple takes in col and row
                                                        #! so each tuple represents a segment of the snake


        #* Apple
        self.place_apple()

        #*Draw logic
        self.draw_frames = []
        self.draw()

    def place_apple(self): #! creates a random column and row position for the apple

        self.apple_pos = (randint(0, FIELDS[0] - 1), randint(0, FIELDS[1] - 1)) #! -1 as ranint includes the number
                                                                                #! since theres 20 columns, apple should be placed from 0-19
        

    def draw(self):

        apple_frame = ctk.CTkFrame(self, fg_color = APPLE_COLOR)
        self.draw_frames.append((apple_frame, self.apple_pos))

        for index, pos in enumerate(self.snake): #! enumerate gets index for where i am in the loop
        
            if index != 0:
                color = SNAKE_BODY_COLOR
            else:
                color = SNAKE_HEAD_COLOR

            snake_frame = ctk.CTkFrame(self, fg_color = color, corner_radius = 0)
            self.draw_frames.append((snake_frame, pos))
            
        for frame, pos in self.draw_frames: #! self.draw_frames is a list of tuples, each tuple containing a frame and its position
            frame.grid(column = pos[0], row = pos[1])


        #*Run
        self.mainloop()


Game()