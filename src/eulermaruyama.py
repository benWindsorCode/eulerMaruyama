from typing import Callable, List
import numpy as np


# For approximation of equations of the form dX = a(t,X)dt + b(t,X)dW
class EulerMaruyama:
    def __init__(self, a_func: Callable[[float, float], float], b_func: Callable[[float, float], float], steps: int, delta: float, initial: float) -> None:
        self.a_func: Callable[[float, float], float] = a_func
        self.b_func: Callable[[float, float], float] = b_func
        self.steps: int = steps
        self.delta: float = delta
        self.initial: float = initial
        self.simulation: List[float] = []

    # simulation of a solution calculated via the Euler-Maruyama method
    def simulate(self, brownian: List[float] = None) -> List[float]:
        self.simulation = []
        current = self.initial
        print(len(brownian))
        print(self.steps)
        for i in range(self.steps-1):
            print(i)
            self.simulation.append(current)
            normal = np.random.normal(0,1)
            if (brownian == None):
                delta_w = normal*np.sqrt(self.delta)
            else: 
                delta_w = brownian[i+1] - brownian[i]
            current = current + self.a_func(i*self.delta, current)*self.delta + self.b_func(i*self.delta, current)*delta_w
        
        return self.simulation

