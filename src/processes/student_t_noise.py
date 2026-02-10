import numpy as np
from scipy.stats import t

class StudentTNoiseModel:
    """
    Student‑t Noise Model for Fat‑Tailed Returns

    Returns are drawn from a Student‑t distribution with:
    - df: degrees of freedom (lower df = heavier tails)
    - scale: volatility scaling factor
    - dt: time step

    Price evolves multiplicatively:
    S[t] = S[t-1] * exp(return_t)
    """

    def __init__(self, df=5, scale=0.02, dt=1/252):
        self.df = df
        self.scale = scale
        self.dt = dt

    def simulate_path(self, steps, S0=100):
        prices = np.zeros(steps)
        prices[0] = S0

        # Student‑t returns
        returns = t.rvs(df=self.df, size=steps-1) * self.scale * np.sqrt(self.dt)

        for t_idx in range(1, steps):
            prices[t_idx] = prices[t_idx - 1] * np.exp(returns[t_idx - 1])

        return prices, returns