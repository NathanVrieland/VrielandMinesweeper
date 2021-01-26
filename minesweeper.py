"""CS 108 Final Project

Minesweeper using Tkinter canvas
this is exactly what Billy Gates would call "slick, tight code" as he referenced on stage with Dwane "The Rock" Johnson
when unveiling the X-box to the public in 2001

@author: Nathan Vrieland (nlv26)
@date: fall, 2020
"""

import tkinter
from tile import Tile

class Minesweeper:
    
    def __init__(self, window, width, height):
        '''initializes the minesweeper board'''
        self.lost = 0
        self.window = window
        self.height = height
        self.width = width
        self.canvas = tkinter.Canvas(width = width, height = height, bg = 'white')
        self.canvas.pack()
        self.button_list = []
        
        # initialize all tile objects
        cycles = 0
        rw = 0
        cm = 0
        for i in range(20):
            self.button_list.append([])
            for c in range(20):
                self.button_list[rw].append(Tile(x = rw,
                                                 y = cm,
                                                 width = width,
                                                 height = height,
                                                 canvas = self.canvas))
                cm += 1
                cycles += 1
            cm = 0
            rw += 1
            
        # check proximity for all tiles and add it to the tile.state value
        current_row = 0
        current_tile = 0
        for rows in self.button_list:
            for tile in rows:
                if tile.state != 9:
                    check_row = -1
                    check_tile = -1
                    for i in range(3):
                        for c in range(3): # is that a triple nested loop?
                            if 0 <= current_row + check_row <= 20 and 0 <= current_tile + check_tile <= 20:
                                try:
                                    if self.button_list[current_row + check_row][current_tile + check_tile].tile_check() == 9:                           
                                        tile.state += 1
                                except IndexError:
                                    'this is fine'
                            check_tile += 1
                        check_tile = -1
                        check_row += 1
#                 tile.draw_state() # for testing comment out when finished
                current_tile += 1
            current_row += 1
            current_tile = 0
                
        # click binds
        self.canvas.bind('<Button-1>', self.left_click)
        self.canvas.bind('<Button-3>', self.right_click)
    

    
    def left_click(self, event):
        '''method called when the canvas is clicked'''
        self.canvas.delete(tkinter.ALL)
        for x in self.button_list:
            for i in x:
                if i.click(event.x, event.y) == True: # Condition for the clicked tile
                    if i.state == 9: # condition for a mine being clicked
                        self.lose()                        
                    self.search(i)
                i.render()
        if self.win_check() == True:
            self.win()
    
    def right_click(self, event):
        '''method called when the canvas in right-clicked'''
        self.canvas.delete(tkinter.ALL)
        for x in self.button_list:
            for i in x:
                i.flag(event.x, event.y)
                i.render()
    
    def search(self, tile):
        '''recursive function for searching all nearby tiles to automatically clear blank'''
        if tile.state == 0:
            for x in range(-1,2):
                for i in range(-1,2):
                    if 0 <= tile.row + x <= 20 and 0 <= tile.column + i <= 20:
                        try:
                            current_tile = self.button_list[tile.row + x][tile.column + i]
                            if (x != 0) or (i != 0):
                                if current_tile.state == 0 and current_tile.searched == 0:
                                    current_tile.searched = 1
                                    self.search(current_tile)
                            current_tile.reveal()
                            current_tile.render()
                        except IndexError:
                            "where we're going we dont need IndexErrors"
    
    def lose(self):
        '''method called when a mine is clicked, reveals all tiles'''
        self.lost = 1
        for x in self.button_list:
            for i in x:
                i.reveal()
                i.render()
                
    def win_check(self):
        for x in self.button_list:
            for i in x:
                if (i.state != 9) and (i.hidden_state == 1):
                    return False
        return True
    
    def win(self):
        if self.lost == 0:
            self.lose()
            self.canvas.create_text(self.width/2,self.height/2, font=('', 70), text='You win!', fill='red')
        

root_window = tkinter.Tk()
root_window.title('Minesweeper')
game = Minesweeper(root_window, 500, 500)