import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


##Test1 : Plot function

from src.utils.plot import plot_price_path
from src.processes.gbm import GeometricBrownianMotion


gbm = GeometricBrownianMotion()
prices = gbm.simulate_path(1000)
plot_price_path(prices)

## Test2: OU Process simulation

from src.processes.ornstein_uhlenbeck import OrnsteinUhlenbeck
from src.utils.plot import plot_price_path

ou = OrnsteinUhlenbeck(mu=0.0, theta=1.0, sigma=0.2)
path = ou.simulate_path(1000, X0=1.0)

plot_price_path(path, title="Ornstein–Uhlenbeck Simulation")

##Test3: Jump Diffusion simulation

from src.processes.jump_diffusion import JumpDiffusion
from src.utils.plot import plot_price_path

if __name__ == "__main__":
    jd = JumpDiffusion(mu=0.05, sigma=0.2, lambda_=0.5, mu_j=-0.2, sigma_j=0.4)
    prices = jd.simulate_path(1000, S0=100)
    plot_price_path(prices, title="Jump Diffusion Price Simulation")


##Test4: Student T-Noise simulation
from src.processes.student_t_noise import StudentTNoiseModel
from src.utils.plot import plot_price_path, plot_return_distribution

if __name__ == "__main__":
    model = StudentTNoiseModel(df=4, scale=0.03)
    prices, returns = model.simulate_path(1000, S0=100)

    plot_price_path(prices, title="Student T Noise Price Simulation")
    plot_return_distribution(returns, title="Student T Return Distribution")