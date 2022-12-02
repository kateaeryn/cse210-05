from game.scripting.action import Action

class MoveActorsAction(Action):
    """
    An output that moves the actors in the game.
    
    The responsibility of MoveActorsAction is to perform the prescribed movment 
    for each different type of actor
    """

    def execute(self, cast, script):
        """Executes the movment of the actors

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
         """
        actors = cast.get_all_actors()

        for actor in actors:
            actor.move_next()


