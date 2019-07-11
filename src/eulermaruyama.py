from typing import Callable, List
import numpy as np


# For approximation of equations of the form dX = a(t,X)dt + b(t,X)dW
class EulerMaruyama:
    def __init__(self, a_func: Callable[[float, float], float], b_func: Callabke[[float, float], float], steps: int, delta: float, initial: float) -> None:
        self.a_func: Callable[[float, float], float] = a_func
        self.b_func: Callable[[float, float], float] = b_func
        self.steps: int = steps
        self.delta: float = delta
        self.initial: float = initial
        self.simulation: List[float] = []

    # simulation of a solution calculated via the Euler-Maruyama method
    def simulate(self) -> List[float]:
        self.simulation = []
        current = self.initial

        for i in range(steps):
            self.simulation.append(current)
            normal = np.random.normal(0,1)
            delta_w = normal*np.sqrt(self.delta)
            current = current + self.a_func(i*self.delta, current)*self.delta + self.b_func(i*self.delta, current)*delta_w
        
        return self.simulation

    # A version of the simulation function which uses a provided realisation of the brownian motion
    def simulate(self, brownian: List[float]) -> List[float]:
        self.simulation = []
        current = self.initial

        for i in range(steps):
            self.simulation.append(current)
            normal = np.random.normal(0,1)
            delta_w = brownian[i+1]-brownian[i] 
            current = current + self.a_func(i*self.delta, current)*self.delta + self.b_func(i*self.delta, current)*delta_w

        return self.simulation

