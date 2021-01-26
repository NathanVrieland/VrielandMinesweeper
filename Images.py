"""CS 108 Final Project

drawing functions used in tile.py

@author: Nathan Vrieland (nlv26)
@date: fall, 2020
"""


num_font = ''

def draw_dug(canvas, center_x, center_y, size):
    x1 = center_x - size / 2
    x2 = center_x + size / 2
    y1 = center_y - size / 2
    y2 = center_y + size / 2
    canvas.create_rectangle(x1, y1, x2, y2, fill='light gray')

def draw_boarder(canvas, center_x, center_y, size):
    x1 = center_x - size / 2
    x2 = center_x + size / 2
    y1 = center_y - size / 2
    y2 = center_y + size / 2
    canvas.create_rectangle(x1, y1, x2, y2, outline='black')
    
def draw_mine(canvas, center_x, center_y, size):
    x1 = center_x - size / 2
    x2 = center_x + size / 2
    y1 = center_y - size / 2
    y2 = center_y + size / 2 
    canvas.create_oval(x1, y1, x2, y2, fill='black')
    canvas.create_oval(x1 + size / 3, y1 + size / 3, x2 - size / 3, y2 - size / 3, fill = 'light gray')
    
def draw_flag(canvas, center_x, center_y, size):
    x1 = center_x - size / 2
    x2 = center_x + size / 2
    y1 = center_y - size / 2
    y2 = center_y + size / 2
    canvas.create_rectangle(x1 + size / 2.5, y1, x2 - size / 2.5, y2, fill = 'red', outline = 'red')
    canvas.create_rectangle(x1, y1 + size / 1.5, x2, y2, fill = 'black', outline = 'black')
    canvas.create_rectangle(x1, y1, x2 - size / 2.5, y2 - size / 1.5, fill = 'red', outline = 'red')
    canvas.create_rectangle(x1, y1, x2, y2, outline='black')
    
def draw_1(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '1', fill = 'blue')
def draw_2(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '2', fill = 'green')
def draw_3(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '3', fill = 'red')
def draw_4(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '4', fill = 'dark blue')
def draw_5(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '5', fill = 'maroon')
def draw_6(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '6', fill = 'teal')
def draw_7(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '7', fill = 'black')
def draw_8(canvas, center_x, center_y, size):
    canvas.create_text(center_x, center_y, font = (num_font, int(size * .75)), text = '8', fill = 'gray')



if __name__ == "__main__":
    import tkinter
    mine_window = tkinter.Tk()
    mine_window.title('mine')
    mine_canvas = tkinter.Canvas(mine_window, width = 300, height = 300, bg = 'white')
    mine_canvas.pack()
    draw_flag(mine_canvas, 150, 150, 300)
    