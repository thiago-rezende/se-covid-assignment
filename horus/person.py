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
    def __init__(self, position, state: State = State.HEALTHY):
        self.position = np.array(position)
        self.state = state

    def update(self, max_step):
        if self.state == State.INFECTED:
            self.state = random.choices(
                list(State), weights=[0.0, 0.85, 0.05, 0.1])[0]

        if self.state != State.DEAD:
            self.move(np.random.uniform(max_step) *
                      np.random.uniform(-1.0, 1.0, size=2) * 2 - 1)

    def move(self, displacement):
        self.position += displacement
