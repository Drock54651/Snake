import customtkinter as ctk
import tkinter as tk
from settings import *
from random import randint

#NOTE: for the tuple positions of the snake, its col,row
#NOTE: not row, col
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
                      (START_POS[0] - 1, START_POS[1]), #! each tuple takes in col and row
                      (START_POS[0] - 2, START_POS[1])] #! so each tuple represents a segment of the snake
                                                       
        self.direction = DIRECTIONS['right']
        self.bind('<Key>', self.get_input)


        #* Apple
        self.place_apple()

        #*Draw logic
        self.draw_frames = []
        self.animate()


        #*Run
        self.mainloop()

    def get_input(self, event): 
        #print(event) #! can get the keycode for arrow input
        match event.keycode:
            # case 37: print('left')
            # case 38: print('up')
            # case 39: print('right')
            # case 40: print('down')
            case 37: self.direction = DIRECTIONS['left']
            case 38: self.direction = DIRECTIONS['up']
            case 39: self.direction = DIRECTIONS['right']
            case 40: self.direction = DIRECTIONS['down']
        #print(self.direction)



    def animate(self):#! create new head = old head + direction, remove last segment of the snake
        #NOTE: remember is col,row

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]) #! self.snake[0][0] get the first tuple, then the col, and adds col from input
        self.snake.insert(0, new_head)

        #* Removing last part of snake
        self.snake.pop()

        self.draw()

        self.after(250, self.animate)


    def place_apple(self): #! creates a random column and row position for the apple

        self.apple_pos = (randint(0, FIELDS[0] - 1), randint(0, FIELDS[1] - 1)) #! -1 as ranint includes the number
                                                                                #! since theres 20 columns, apple should be placed from 0-19
        

    def draw(self):

        #TODO: clear current placed frames and clear the draw frames list
        if self.draw_frames:

            for frame, pos in self.draw_frames:
                frame.grid_forget()
                
            self.draw_frames.clear() 


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


        


Game()