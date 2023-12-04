import numpy as np
from PIL import Image


class Canvas:

    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

        # create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.height, 3), dtype=np.uint8)

        # create [0,0,0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        """
        Converts the current array into an image file
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
