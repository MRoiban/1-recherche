from lle import WorldState
from .problem import SearchProblem


class ExitProblem(SearchProblem[WorldState]):
    """
    A simple search problem where the agents must reach the exit **alive**.
    """

    def is_goal_state(self, state: WorldState) -> bool:
        # todo: implementation
        # if 
            # 1. the robot is on the exit cell
            # 2. the robot is alive
        # then
            # return true
        # else
            # return false
         
        raise NotImplementedError()
