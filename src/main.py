from blackscholes import BlackScholes
from weiner import Weiner

def run():
    mu = 0.75
    sigma = 0.3
    steps = 50
    delta = 0.3
    initial = 0
    realisation = Weiner(steps, delta)
    eqn = BlackScholes(mu, sigma, steps, delta, initial)
    eqn.run(realisation)

if __name__ == "__main__":
    run()
