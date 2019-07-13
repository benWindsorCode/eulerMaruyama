from typing import Callable, List
from eulermaruyama import EulerMaruyama


class BlackScholes:
    def __init__(self, mu: float, sigma: float, steps: int, delta: float, initial: float):
        self.mu: float = mu
        self.sigma: float = sigma
        self.steps: int = steps
        self.delta: float = delta
        self.initial: float = initial
        self.a_func: Callable[[float, float], float] = lambda t, w : self.mu*w
        self.b_func: Callable[[float, float], float] = lambda t, w : self.sigma*w
        self.solver: EulerMaruyama = EulerMaruyama(self.a_func, self.b_func, self.steps, self.delta, self.initial)
        self.simulation: List[float] = []

    def run(self, brownian: List[float] = None) -> None:
        if brownian == None: 
            self.simulation = self.solver.simulate()
        else:
            self.simulation = self.solver.simulate(brownian)