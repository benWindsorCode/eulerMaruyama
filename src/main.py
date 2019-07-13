from weiner import Weiner
from blackscholes import BlackScholes
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

def run():
    mu = 0.75
    sigma = 0.3
    steps = 50
    delta = 0.3
    initial = 307.65
    realisation = Weiner(steps, delta)
    realisation.simulate()
    eqn = BlackScholes(mu, sigma, steps, delta, initial)
    eqn.run(realisation.simulation)

    time = [ n*delta for n in range(steps-1) ]
    # smooth = interp1d(time, eqn.simulation)
    plt.scatter(time, eqn.simulation, s=0.5)


    plt.show()

if __name__ == "__main__":
    run()
