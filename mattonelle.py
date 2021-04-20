import turtle
from turtle import  Screen
import random

from colorutils import Color


turtle.setup(500,500) # size of the window
board = turtle.Turtle()

screen = Screen()
screen.tracer(0, 0)
screen.colormode(255)
#board.tracer(0)
 

# to generate different shades of the same color, hue
def colorArray(hue):
  arr=[]
  for i in range(9): # pick the number of shades
     c=Color(hsv=(hue, random.randint(22,100)/100, random.randint(22,100)/100)) # 0 would include black too
     arr.append((int(c.red),int(c.green), int(c.blue))) 
  return arr



# draws a rectangle given top left position of a rectangle
def draw_tile(board,x,y,tilesize,bordersize,hue):
  #arraycolory=["#7CFC00","#228B22","#006400","#9ACD32","#8FBC8F","#556B2F","#6B8E23","#00FA9A","#008000","#228B22"] # a series of nice greens, to use it remove colormode
  arraycolory=colorArray(hue)
  
  fill=arraycolory[random.randint(0,len(arraycolory)-1)]
  board.fillcolor(fill[0],fill[1],fill[2])
  board.pencolor('white') # color between the tiles
  board.pensize(bordersize)
  board.setheading(0)
 
  board.begin_fill()
  board.up()
  board.goto(x,y)
  board.down()
  # draw top
  board.forward(tilesize)
  # draw right
  board.right(90)
  board.forward(tilesize)
  # draw bottom
  board.right(90)
  board.forward(tilesize)
  # draw left
  board.right(90)
  board.forward(tilesize)
  board.end_fill()

# size of the canvas and of the tiles
canvasx=21
canvasy=21
tilesize=21
linesize=2

randomhue=random.randint(0,359)
for x in range(0,canvasx):
  for y in range(0,canvasy):
    draw_tile(board,-220+x*tilesize,-200 +y*tilesize,tilesize,linesize,randomhue)
 
turtle.done()
