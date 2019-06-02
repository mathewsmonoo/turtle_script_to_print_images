import turtle
import PIL 
from PIL import Image

imloc = "PATH\colorspectrum.png"
	
def create_ttle(x,y):
	ttuga = turtle.Turtle()
	ttuga.speed('fastest')
	turtle.screensize(x,y)
	screen = turtle.Screen()

	# ttuga.setpos(0,0)
	return ttuga

def test_turtle(myturtle,r,g,b,x,y,i,j):
	turtle.colormode(255)
	myturtle.color(r,g,b)
	myturtle.pencolor(r,g,b)
	turtle.delay(0)
	myturtle.forward(1)
	xposnow = (myturtle.pos()[0])

	myturtle.up()
	myturtle.setpos(j+1,i+1)
	myturtle.down()

	if (xposnow > y):
		myturtle.up()
		myturtle.setpos(j+1,i+1)
		myturtle.down()

if__name__=="__main__":
	screen = turtle.Screen()
	img = Image.open(imloc)
	x,y = img.size
	ttuga1 = create_ttle(x,y)
	for j in range (x):
		for i in range (y):
			r, g, b = img.getpixel((j, i))
			test_turtle(ttuga1,r,g,b,x,y,i,j)
	
