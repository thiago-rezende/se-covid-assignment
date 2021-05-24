# Application class

import matplotlib.pyplot as plt

from .area import Area


class Application:
    def __init__(self):
        self.area = Area(n_persons=50, n_infected=5, max_step=5,
                         size=100, infection_radius=10, update_interval=250)

    def run(self):
        self.area.plot()
