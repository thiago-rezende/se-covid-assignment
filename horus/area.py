# Area class

import random

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.animation as manim
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

from .person import Person, State


class Area:
    def __init__(self, n_persons, n_infected, max_step, size, infection_radius, update_interval):
        self.persons = [Person(np.random.uniform(size, size=2))
                        for p in range(n_persons)]

        self.update_interval = update_interval
        self.infection_radius = infection_radius
        self.max_step = max_step
        self.size = size

        for i in range(n_infected):
            self.persons[i].state = State.INFECTED

        self.legend_elements = [
            Line2D([0], [0], marker='o', color='w', label='Healthy',
                   markerfacecolor="#00ff00", markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Infected',
                   markerfacecolor="#ff0000", markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Recovered',
                   markerfacecolor="#0000ff", markersize=10),
            Line2D([0], [0], marker='o', color='w', label='Dead', markerfacecolor="#000000", markersize=10)]

    def update(self):
        for p in self.persons:
            p.update(self.max_step)
            if p.state == State.INFECTED:
                for other in self.persons:
                    if np.linalg.norm(p.position - other.position) < self.infection_radius and id(p) != id(other):
                        if other.state == State.HEALTHY:
                            other.state = random.choices(
                                list(State), weights=[0.0, 1.0, 0, 0])[0]
                        elif other.state == State.RECOVERED:
                            other.state = random.choices(
                                list(State), weights=[0, 0.1, 0.8, 0])[0]

    def color(self, state: State) -> str:
        if state == State.HEALTHY:
            return "#00ff00"  # green
        elif state == State.INFECTED:
            return "#ff0000"  # red
        elif state == State.RECOVERED:
            return "#0000ff"  # blue
        elif state == State.DEAD:
            return "#000000"  # black

    def plot(self):
        fig, ax = plt.subplots()
        ax.set_title("Covid-19 Progression Simulation")
        ax.set_xlabel("X Position")
        ax.set_ylabel("Y Position")

        x_values = np.array([])
        y_values = np.array([])
        color_values = np.array([])

        for p in self.persons:
            x_values = np.append(x_values, p.position[0])
            y_values = np.append(y_values, p.position[1])
            color_values = np.append(color_values, self.color(p.state))

        colors = ["green", "red", "blue", "black"]

        scatter = ax.scatter(x_values, y_values,
                             c=color_values, vmin=0, vmax=100)

        ax.legend(handles=self.legend_elements, loc='upper right')

        self.anim = manim.FuncAnimation(
            fig, self.animate, interval=self.update_interval, fargs=(self, ax, scatter))

        plt.tight_layout()
        plt.show()

    def animate(self, frame, area, ax, scatter):
        self.update()

        x_values = np.array([])
        y_values = np.array([])
        color_values = np.array([])

        n_infected = 0

        for p in self.persons:
            if p.state == State.INFECTED:
                n_infected += 1

            x_values = np.append(x_values, p.position[0])
            y_values = np.append(y_values, p.position[1])
            color_values = np.append(color_values, self.color(p.state))

        ax.cla()
        ax.scatter(x_values, y_values,
                   c=color_values, vmin=0, vmax=100)

        ax.legend(handles=self.legend_elements, loc='upper right')

        if n_infected == 0:
            self.anim.event_source.stop()

        return scatter
