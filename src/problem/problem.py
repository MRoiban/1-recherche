from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from lle import World, Action, WorldState


S = TypeVar("S", bound=WorldState)


class SearchProblem(ABC, Generic[S]):
    """
    A Search Problem is a problem that can be solved by a search algorithm.

    The generic parameter S is the type of the problem state.
    """

    def __init__(self, world: World):
        self.world = world
        world.reset()
        self.initial_state = world.get_state()

    @abstractmethod
    def is_goal_state(self, problem_state: S) -> bool:
        """Whether the given state is the goal state"""

    def get_successors(self, state: S) -> list[tuple[WorldState, Action]]:
        """
        Returns  all possible states that can be reached from the given world state.

        Note that if an agent dies, the game is over and there is no successor to that state.
        """
        # 1. get_all_possible_actions for current state
        # 2. loop over actions:
            # 1. apply per iteration an action
            # 2. add (state + action) in a tuple then append to list
            # reset state to before action
        # return list[tuple[state, action]]
        raise NotImplementedError()

    def heuristic(self, problem_state: S) -> float:
        # types:
            # Manhattan distance
            # Diagonal distance
            # Euclidian distance
            # constant
        return 1
