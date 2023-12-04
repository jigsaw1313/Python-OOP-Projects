from canvas import Canvas
from shapes import Rectangle, Square

# get canvas width and height from user
canvas_width = int(input("Enter canvas width: "))
canvas_height = int(input('Enter canvas height: '))

# make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input('Enter canvas color (white/black): ')

# create a canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    print("What do you like to draw?\nEnter quit to quit from program")
    shape_type = input()
    # Ask for rectangle data and create rectangle if user enter 'rectangle'
    if shape_type.lower() == 'rectangle':
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter width of the rectangle: "))
        rec_height = int(input("Enter height of the rectangle: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    # as for square data and create square if user entered 'square'
    if shape_type.lower() == "square":
        sqr_x = int(input("Enter x of the square: "))
        sqr_y = int(input("Enter y of the square: "))
        sqr_side = int(input("Enter side of the square: "))
        red = int(input("How much red should the rectangle have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # create the Square
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side, color=(red, green, blue))
        s1.draw(canvas)

    # Break the loop if user entered 'quit'
    if shape_type == 'quit':
        break

canvas.make('canvas.png')
