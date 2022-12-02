from game.casting.actor import Actor
from game.shared.point import Point
import constants

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, color):
        super().__init__()
        self._points = 0
        self.add_points(0)
        self._color = color
        self._position = Point(0,0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")
    
    def set_color(self, color):
        self._color = color

    def set_position(self, position):
        self._position = position

    def get_position(self):
        if self._color == constants.RED:
            self._position = Point(25,0)
        if self._color == constants.GREEN:
            self._position = Point(800,0)
        return self._position
    
    def get_color(self):
        return self._color

    
