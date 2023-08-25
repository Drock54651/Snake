import customtkinter as ctk
import tkinter as tk
from settings import *
from random import randint
from sys import exit
import time
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

    def get_input(self, event): #! arrow key input
        print(event)
        match event.keycode: #! each keycode is mapped to a specific arrow key
           
            case 37: #! left
                if self.direction != DIRECTIONS['right']: #! prevent snake from going backwards into itself
                    self.direction = DIRECTIONS['left']
                else:
                    self.direction
                    
            case 38: #! up
                if self.direction != DIRECTIONS['down']:
                    self.direction = DIRECTIONS['up']
                else:
                    self.direction

            case 39: #! right
                if self.direction != DIRECTIONS['left']:
                    self.direction = DIRECTIONS['right']
                else:
                    self.direction

            case 40: #! down
                if self.direction != DIRECTIONS['up']:
                    self.direction = DIRECTIONS['down']
                else:
                    self.direction



    def animate(self):#! create new head = old head + direction, remove last segment of the snake
        #NOTE: remember is col,row

        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1]) #! self.snake[0][0] get the first tuple(head), then the col/row, and adds col/row from input
        self.snake.insert(0, new_head)



        #* Apple collision

        if self.snake[0] == self.apple_pos:
            self.place_apple()
       
        else: #! Removing last part of snake
            self.snake.pop()

        self.check_game_over()

        #* Drawing
        self.draw()
        self.after(250, self.animate)

    def check_game_over(self): #! hits border or its tail
        snake_head = self.snake[0]
        
        if snake_head[0] >= RIGHT_LIMIT or snake_head[0] <= LEFT_LIMIT or snake_head[1] < TOP_LIMIT \
            or snake_head[1] > BOTTOM_LIMIT or snake_head in self.snake[1:]:

            print('Game Over!')
            
            self.destroy()
            exit()



    def place_apple(self): #! creates a random column and row position for the apple

        self.apple_pos = (randint(0, FIELDS[0] - 1), randint(0, FIELDS[1] - 1)) #! -1 as randint includes the number
                                                                                #! since theres 20 columns, apple should be placed from 0-19
        

    def draw(self):

    
        if self.draw_frames:

            for frame, pos in self.draw_frames:
                frame.grid_forget()
                
            self.draw_frames.clear() 


        apple_frame = ctk.CTkFrame(self, fg_color = APPLE_COLOR)
        self.draw_frames.append((apple_frame, self.apple_pos))

        for index, pos in enumerate(self.snake): 
        
            if index != 0:
                color = SNAKE_BODY_COLOR
            else:
                color = SNAKE_HEAD_COLOR

            snake_frame = ctk.CTkFrame(self, fg_color = color, corner_radius = 0)
            self.draw_frames.append((snake_frame, pos))
            
        for frame, pos in self.draw_frames: #! self.draw_frames is a list of tuples, each tuple containing a frame and its position
            frame.grid(column = pos[0], row = pos[1])


        


Game()