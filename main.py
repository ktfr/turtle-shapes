from turtlesetup import *

#STEP 1: Show an example of a square, triangle, pentagon, and star.
#This draws a square using turtle.
turtle.down()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.up()

#This draws a triangle using turtle at another coordinate to avoid overlap.
turtle.goto(-100,0)

turtle.down()
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(45)
turtle.backward(141)
turtle.right(45)
turtle.up()

#This draws a star using turtle at another coordinate to avoid overlap.
turtle.goto(-200,-100)
turtle.right(90) #Resets the angle of the turtle to ensure the shape is upright

turtle.down()
for i in range(5):
    turtle.forward(100)
    turtle.right(144)

turtle.left(90) #Resets the angle of the turtle to ensure the shape is upright
turtle.up()

#This draws a pentagon using turtle at another coordinate to avoid overlap
turtle.goto(20,-160)
turtle.right(270) #Resets the angle of the turtle to ensure the shape is upright

turtle.down()
for i in range(5):
    turtle.backward(60)
    turtle.left(72)

turtle.up()
turtle.left(270) #Resets the angle of the turtle to ensure the shape is upright

turtle.goto(-50,-50)

#STEP 2: Outputs "Here are a square, triangle, a pentagon, and a star!"
print("Here are a square, a triangle, a pentagon, and a star!")

#STEP 3: Asking the user which shape they want to draw
user_shape = input("What would you like to draw? ")

#STEPS 4-9:
#In the event a user would like to draw a triangle:
if user_shape == "Triangle":
    print("Great, show me a triangle!")
    triangle_x1 = float(input("Enter x coordinate of the first point: "))
    triangle_y1 = float(input("Enter y coordinate of the first point: "))
    triangle_x2 = float(input("Enter x coordinate of the second point: "))
    triangle_y2 = float(input("Enter y coordinate of the second point: "))
    triangle_x3 = float(input("Enter x coordinate of the third point: "))
    triangle_y3 = float(input("Enter y coordinate of the third point: "))

    #This draws the triangle based on user's coordinates
    turtle.goto(triangle_x1,triangle_y1)
    turtle.down()
    turtle.goto(triangle_x2,triangle_y2)
    turtle.goto(triangle_x3,triangle_y3)
    turtle.goto(triangle_x1,triangle_y1)
    turtle.up()

    #Validating the triangle: This determines the length between each coordinate/length of triangle sides.
    turtle.goto(triangle_x1, triangle_y1)
    distance_A = turtle.distance(triangle_x2, triangle_y2)
    turtle.goto(triangle_x2, triangle_y2)
    distance_B = turtle.distance(triangle_x3, triangle_y3)
    turtle.goto(triangle_x3, triangle_y3)
    distance_C = turtle.distance(triangle_x1, triangle_y1)
    turtle.goto(triangle_x1, triangle_y1)

    #Validating the triangle: This determines whether the user's coordinates satisfy a triangle's
    #property of having the sum of 2 sides greater than 1.
    if (distance_A + distance_B <= distance_C) or (distance_A + distance_C <= distance_B) or (distance_B + distance_C <= distance_A):
        print("Sorry, that is not a triangle.")
        turtle.exitonclick()
    else:
        print("You got it right!")
        turtle.exitonclick()

#In the event a user would like to draw a square:
elif user_shape == "Square":
    print("Great, show me a square!")
    square_x1 = float(input("Enter x coordinate of the first point: "))
    square_y1 = float(input("Enter y coordinate of the first point: "))
    square_x2 = float(input("Enter x coordinate of the second point: "))
    square_y2 = float(input("Enter y coordinate of the second point: "))
    square_x3 = float(input("Enter x coordinate of the third point: "))
    square_y3 = float(input("Enter y coordinate of the third point: "))
    square_x4 = float(input("Enter x coordinate of the fourth point: "))
    square_y4 = float(input("Enter x coordinate of the fourth point: "))

    #This draws the square based on user's coordinates
    turtle.goto(square_x1, square_y1)
    turtle.down()
    turtle.goto(square_x2, square_y2)
    turtle.goto(square_x3, square_y3)
    turtle.goto(square_x4, square_y4)
    turtle.goto(square_x1, square_y2)
    turtle.up()

    #Validating the square: This determines the length between each coordinate/length of square's sides.
    turtle.goto(square_x1, square_y1)
    side_A = turtle.distance(square_x2, square_y2)
    turtle.goto(square_x2, square_y2)
    side_B = turtle.distance(square_x3, square_y3)
    turtle.goto(square_x3, square_y3)
    side_C = turtle.distance(square_x4, square_y4)
    turtle.goto(square_x4, square_y4)
    side_D = turtle.distance(square_x1, square_y1)

    #This stores diagonal lengths of opposite points.
    turtle.goto(square_x1, square_y1)
    diagonal_A = turtle.distance(square_x4, square_y4)
    turtle.goto(square_x2, square_y2)
    diagonal_B = turtle.distance(square_x3,square_y3)

    #Validating the square: This determines whether the user's coordinates satisfy two properties
    #of a square. First, if  all four sides equal eachother. Second, if the the diagonal lengths
    #of opposite points equal eachother.
    if side_A == side_B == side_C == side_D and diagonal_A == diagonal_B:
        print("You got it right!")
        turtle.exitonclick()
    else:
        print("Sorry, that is not a square.")
        turtle.exitonclick()

#In the event a user would like to draw a pentagon or a star, the program ends as the user
#clicks on the turtle screen. The program also ends if the user enters anything outside
#of the 4 shape options.
elif user_shape == "Pentagon":
    turtle.exitonclick()
elif user_shape == "Star":
    turtle.exitonclick()
else:
    turtle.exitonclick()