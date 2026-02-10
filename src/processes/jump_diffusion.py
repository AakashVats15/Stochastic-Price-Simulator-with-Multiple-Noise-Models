import numpy as np

class JumpDiffusion:
    """
    Merton Jump Diffusion Model

    dS/S = (mu - 0.5*sigma^2 - lambda*kappa) dt + sigma dW + J dN

    Where:
    - mu: drift
    - sigma: diffusion volatility
    - lambda_: jump intensity (expected number of jumps per unit time)
    - mu_j: mean of jump size (in log space)
    - sigma_j: volatility of jump size (in log space)
    - dt: time step

    J ~ lognormal(mu_j, sigma_j)
    N ~ Poisson(lambda_ * dt)
    """

    def __init__(self, mu=0.05, sigma=0.2, lambda_=0.3, mu_j=-0.2, sigma_j=0.3, dt=1/252):
        self.mu = mu
        self.sigma = sigma
        self.lambda_ = lambda_
        self.mu_j = mu_j
        self.sigma_j = sigma_j
        self.dt = dt

        # Compensation term so that drift is adjusted for jumps
        self.kappa = np.exp(self.mu_j + 0.5 * self.sigma_j**2) - 1

    def simulate_path(self, steps, S0=100):
        prices = np.zeros(steps)
        prices[0] = S0

        for t in range(1, steps):
            # Diffusion part
            dW = np.random.normal(0, np.sqrt(self.dt))

            # Jump part: number of jumps in this interval
            N_t = np.random.poisson(self.lambda_ * self.dt)

            # If jumps occur, sum their lognormal sizes
            if N_t > 0:
                jumps = np.random.lognormal(mean=self.mu_j, sigma=self.sigma_j, size=N_t)
                J_t = np.prod(1 + jumps)  # multiplicative effect
            else:
                J_t = 1.0

            drift = (self.mu - 0.5 * self.sigma**2 - self.lambda_ * self.kappa) * self.dt
            diffusion = self.sigma * dW

            prices[t] = prices[t-1] * np.exp(drift + diffusion) * J_t

        return prices
