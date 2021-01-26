"""CS 108 Final Project

Tile object used in minesweeper.py

@author: Nathan Vrieland (nlv26)
@date: fall, 2020
"""

import random
import Images

class Tile:
    
    def __init__(self, x, y, width, height, canvas):
        '''initializes tile object'''
        self.row = x
        self.column = y
        self.canvas = canvas
        self.width = width
        self.height = height
        self.center_x = (x * width/20) + (width/20)/2
        self.center_y = (y * height/20) + (height/20)/2
        bomb_chance = 10 # % chance of a tile being a mine
        
        # randomint to determine if tile is a mine
        self.state = random.randint(0, 100)
        if self.state < 100 - bomb_chance:
            self.state = 0
        else:
            self.state = 9
        # bianary tile states (self.searched is only used in minesweeper.search method)
        self.flag_state = 0
        self.hidden_state = 1
        self.searched = 0
        Images.draw_boarder(canvas, self.center_x, self.center_y, self.width/20)
        
        
        
    def click(self, x, y):
        '''detects click and changes hidden state'''
        if (self.center_x - (self.width/20)/2) < x < (self.center_x + (self.width/20)/2) and (self.center_y - (self.height/20)/2) < y < (self.center_y + (self.height/20)/2):
            if self.flag_state == 0:
                self.hidden_state = 0
                return True
        return False
    
    def flag(self, x, y):
        '''detects right-click and changes flag state'''
        if (self.center_x - (self.width/20)/2) < x < (self.center_x + (self.width/20)/2) and (self.center_y - (self.height/20)/2) < y < (self.center_y + (self.height/20)/2):
            if self.hidden_state == 1:
                if self.flag_state == 0:
                    self.flag_state = 1
                elif self.flag_state == 1:
                    self.flag_state = 0
                    
    def reveal(self):
        '''changes hidden state'''
        self.hidden_state = 0
            
    def tile_check(self):
        '''returns the tile state'''
        return self.state
            
    def render(self):
        '''determines the tile state and draws the tile on the canvas'''
        Images.draw_boarder(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.flag_state == 1:
            Images.draw_flag(self.canvas, self.center_x, self.center_y, self.width/20)
        elif self.hidden_state == 0:
            self.draw_state()
            
    
    def draw_state(self):
        '''draws the tile on the canvas'''
        if self.hidden_state == 0:
            Images.draw_dug(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 1:
            Images.draw_1(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 2:
            Images.draw_2(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 3:
            Images.draw_3(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 4:
            Images.draw_4(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 5:
            Images.draw_5(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 6:
            Images.draw_6(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 7:
            Images.draw_7(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 8:
            Images.draw_8(self.canvas, self.center_x, self.center_y, self.width/20)
        if self.state == 9:
            Images.draw_mine(self.canvas, self.center_x, self.center_y, self.width/20)
        