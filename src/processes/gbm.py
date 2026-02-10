import numpy as np

class GeometricBrownianMotion:
    """
    Geometric Brownian Motion (GBM)
    dS = μS dt + σS dW

    Parameters:
    - mu: drift
    - sigma: volatility
    - dt: time step (default = 1/252 for daily steps)
    """

    def __init__(self, mu=0.05, sigma=0.2, dt=1/252):
        self.mu = mu
        self.sigma = sigma
        self.dt = dt

    def simulate_path(self, steps, S0=100):
        prices = np.zeros(steps)
        prices[0] = S0

        for t in range(1, steps):
            noise = np.random.normal(0, np.sqrt(self.dt))
            prices[t] = prices[t-1] * np.exp(
                (self.mu - 0.5 * self.sigma**2) * self.dt +
                self.sigma * noise
            )

        return prices