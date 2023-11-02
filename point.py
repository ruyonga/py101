class Point:

    """Point class represents and manipulates x, y"""

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute my distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def to_string(self):
        return f"({self.x}, {self.y})"

    def __str__(self):

        return f"({self.x}, {self.y})"

    def halfway(self, target):
        """Return the halfway point between myself and the target"""

        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2

        return Point(mx, my)


class Rectangle:
    """ A Class to manufacture rectangle objects"""
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h
        
        
    def __str__(self):
        return f"{self.corner}m {self.width}, {self.height}"
    
    