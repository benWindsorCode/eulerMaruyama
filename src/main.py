from weiner import Weiner
from blackscholes import BlackScholes
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from typing import List
import numpy as np

def exact_soln(mu: float, sigma: float, delta: float, initial: float, brownian: List[float]):
    exact = []
    for i in range(len(brownian)-1):
        exact.append(initial*np.exp((mu-sigma*sigma*0.5)*i*delta + sigma*brownian[i]))
    return exact

def run() -> None:
    mu = 0.75
    sigma = 0.3
    steps = 50
    delta = 0.2
    initial = 307.65
    realisation = Weiner(steps, delta)
    realisation.simulate()
    eqn = BlackScholes(mu, sigma, steps, delta, initial)
    eqn.run(realisation.simulation)
    exact = exact_soln(mu, sigma, initial, delta, realisation.simulation)
    time = [ n*delta for n in range(steps-1) ]
    smooth = interp1d(time, exact)
    plt.plot(time, smooth(time))

    plt.scatter(time, eqn.simulation, s=0.5)


    plt.show()

if __name__ == "__main__":
    run()