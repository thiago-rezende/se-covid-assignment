# Person class

import random
import numpy as np
from enum import Enum


class State(Enum):
    """Infection State

    Represents the infection state
    """
    HEALTHY = 0
    INFECTED = 1
    RECOVERED = 2
    DEAD = 3


class Person:
    """Person class

    Represents an behave like a person in the simulation
    """

    def __init__(self, position, state: State = State.HEALTHY):
        """Person constructor

        Constructs a Person object

        Args:
            position (numpy.ndarray): Person's position
            state (State, optional): Person's current state. Defaults to State.HEALTHY.
        """
        self.position = np.array(position)
        self.state = state

    def update(self, max_step):
        """Person update

        Updates the state based on some arbitrary ratio and move it's self

        Args:
            max_step (float): Move step modifier
        """
        if self.state == State.INFECTED:
            self.state = random.choices(
                list(State), weights=[0.0, 0.85, 0.05, 0.1])[0]

        if self.state != State.DEAD:
            self.move(np.random.uniform(max_step) *
                      np.random.uniform(-1.0, 1.0, size=2) * 2 - 1)

    def move(self, displacement):
        """Person move

        Moves it's self by a displacement value

        Args:
            displacement (numpy.ndarray): Displacement
        """
        self.position += displacement
