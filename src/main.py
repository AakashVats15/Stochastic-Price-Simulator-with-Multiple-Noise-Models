"""
Main runner for the Stochastic Price Simulator.
Switch between models by changing the `model_name` variable.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.processes.gbm import GeometricBrownianMotion
from src.processes.ornstein_uhlenbeck import OrnsteinUhlenbeck
from src.processes.jump_diffusion import JumpDiffusion
from src.processes.student_t_noise import StudentTNoiseModel

from src.utils.plot import plot_price_path, plot_return_distribution


def run_model(model_name="gbm", steps=1000, S0=100):
    """
    Runs the selected stochastic model and plots the results.
    """

    if model_name.lower() == "gbm":
        model = GeometricBrownianMotion(mu=0.05, sigma=0.2)
        prices = model.simulate_path(steps, S0)
        returns = None

    elif model_name.lower() == "ou":
        model = OrnsteinUhlenbeck(mu=0.0, theta=1.0, sigma=0.2)
        prices = model.simulate_path(steps, X0=0.5)
        returns = None

    elif model_name.lower() == "jump":
        model = JumpDiffusion(mu=0.05, sigma=0.2, lambda_=0.4, mu_j=-0.2, sigma_j=0.3)
        prices = model.simulate_path(steps, S0)
        returns = None

    elif model_name.lower() == "student_t":
        model = StudentTNoiseModel(df=4, scale=0.03)
        prices, returns = model.simulate_path(steps, S0)

    else:
        raise ValueError(f"Unknown model: {model_name}")

    # Plot price path
    plot_price_path(prices, title=f"{model_name.upper()} Price Simulation")

    # Plot return distribution if available
    if returns is not None:
        plot_return_distribution(returns, title=f"{model_name.upper()} Return Distribution")


if __name__ == "__main__":
    # Change this to switch models:
    # Options: "gbm", "ou", "jump", "student_t"
    run_model(model_name="gbm")