class Rectangle:
    """
    A Rectangle shape that can be drawn on a Canvas object
    """
    def __init__(self, x, y, height, width, color):
        self.width = width
        self.height = height
        self.y = y
        self.x = x
        self.color = color

    def draw(self, canvas):
        """ Draws itself into the canvas"""
        # changes a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.width] = self.color


class Square:
    """A square shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # changes a slice of the array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.side] = self.color
