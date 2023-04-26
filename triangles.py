import random
import math
import turtle

def work_out(angles, lengths):
    # work out missing angle 
    missing_ang = abs(angles[1]-angles[0])
    angles.append(missing_ang)
    
    # use sine rule to figure out appropriate lengths of other sides
    B = lengths[0]*math.sin(angles[1])
    print(B)

def triangle(displacement, angle):
  # initialise turtles
  wn = turtle.Screen()  # Set up the window and its attributes

  # This just makes the screen full screen without the user having to touch the maximize button repeatedly
  wn.setup(width=1.0, height=1.0, startx=None, starty=None)
  wn.bgcolor("lightgreen")
  wn.title("Triangle")
  
  tess = turtle.Turtle()  # Create tess and set some attributes
  tess.color("black")
  tess.pensize(5)
  turtle.write('A', font = 'style', move = True, align = 'right')
  tess.forward(displacement[0] * 10)  # Make tess draw a triangle
  tess.left(180 - angle[0])
  turtle.setpos(displacement[1] * 10, 0)	
  turtle.write('B', font = 'style', align = 'left')	
  turtle.setpos(displacement[1]*10, 0)	
  tess.forward(displacement[1] * 10)	
  tess.left(180 - angle[1])	
  turtle.setpos(math.cos(math.radians(angle[2])) * displacement[2] * 10, math.sin(math.radians(angle[0])) * displacement[1] * 10) # y-axis is vertical height, x is half of line AB, need to function to find y (constantly changes)	
  turtle.write('C', move = True, font = 'style', align = 'center')	
  tess.forward(displacement[2] * 10)
   # Complete the triangle


# lists to store side and angles
two_angles = []
one_side = []

# randomly select two angles between 30 and 90
ang_1 = random.randint(30, 90)
ang_2 = random.randint(30, 89)
two_angles.append(ang_1)
two_angles.append(ang_2)

# generate a length between 5 and 15
side_a = random.randint(5, 15)
one_side.append(side_a)

# workout all lengths and angles
work_out(two_angles, side_a)



