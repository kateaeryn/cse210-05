import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        cycle = cast.get_actors("cycles")
        cycle1 = cycle[0]       
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            cycle1.grow_tail(1)
            cycle1.turn_head(self._direction)  

        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            cycle1.grow_tail(1)
            cycle1.turn_head(self._direction)
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            cycle1.grow_tail(1)
            cycle1.turn_head(self._direction) 
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            cycle1.grow_tail(1)
            cycle1.turn_head(self._direction)
        
        cycle2 = cycle[1]
        
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            cycle2.grow_tail(1)
            cycle2.turn_head(self._direction)
        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)
            cycle2.grow_tail(1)
            cycle2.turn_head(self._direction)
        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)
            cycle2.grow_tail(1)
            cycle2.turn_head(self._direction)
        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)
            cycle2.grow_tail(1)
            cycle2.turn_head(self._direction)
       