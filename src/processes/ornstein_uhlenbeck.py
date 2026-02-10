import numpy as np

class OrnsteinUhlenbeck:
    """
    Ornstein–Uhlenbeck (OU) Process
    dX = theta * (mu - X) dt + sigma dW

    Parameters:
    - mu: long-term mean
    - theta: speed of mean reversion
    - sigma: volatility
    - dt: time step (default = 1/252 for daily)
    """

    def __init__(self, mu=0.0, theta=0.7, sigma=0.1, dt=1/252):
        self.mu = mu
        self.theta = theta
        self.sigma = sigma
        self.dt = dt

    def simulate_path(self, steps, X0=0.0):
        X = np.zeros(steps)
        X[0] = X0

        for t in range(1, steps):
            noise = np.random.normal(0, np.sqrt(self.dt))
            X[t] = (
                X[t-1]
                + self.theta * (self.mu - X[t-1]) * self.dt
                + self.sigma * noise
            )

        return X