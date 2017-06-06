import turtle

"""
Project 1: Make a circle of squares using what I've learned so far
"""

my_turtle = turtle.Turtle()
my_turtle.speed(0) #increases speed turtle draws

#Define square
def square(length, angle):
	for z in range(4):
		my_turtle.forward(length)
		my_turtle.right(angle)
		#should always be 90 to be a square though


#Create for loop to draw squares in a rotation
for i in range(40):
	square(75, 90)
	my_turtle.right(10)#slight turn to as to not overlap