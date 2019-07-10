import numpy as np
import matplotlib.pyplot as plt
from typing import List

class Weiner:
    def __init__(self, steps: int, delta: float) -> None:
        self.simulation: List[float] = []
        self.steps: int = steps
        self.delta: float = delta
        self.mu: float = 0
        self.sigma: float = self.delta

    def simulate(self) -> List[float]:
        self.simulation = []
        current: float = 0
        for i in range(self.steps):
            self.simulation.append(current)
            current = current + np.random.normal(self.mu, self.sigma)

        return self.simulation

    def plot(self) -> None:
        if len(self.simulation) == 0:
            raise Exception("Can't plot with no data")

        plt.scatter([ n*self.delta for n in range(self.steps)], self.simulation)
        plt.show()



