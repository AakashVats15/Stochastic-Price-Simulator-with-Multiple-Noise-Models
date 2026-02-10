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
