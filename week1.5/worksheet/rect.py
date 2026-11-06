# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        if not isinstance(width,int):
            raise TypeError("width should be an integer please")
        if not isinstance(height,int):
            raise TypeError("height should be an integer")
        if width <=0:
            raise ValueError("width should be greater than 0")
        if height <= 0:
            raise ValueError("height should be greater than 0")
        self.width = width
        self.height = height
    def is_square(self):
        """Return True if width and height are equal."""
        return self.width == self.height
    def area(self):
        """ return area of triangle """
        return self.width*self.height
    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

