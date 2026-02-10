# Stochastic-Price-Simulator-with-Multiple-Noise-Models
*A modular simulation engine for generating synthetic financial price series using multiple stochastic processes.*

This repository implements a stochastic price simulation framework used to study financial time‑series behavior under different noise and diffusion assumptions.
It includes:

Geometric Brownian Motion (GBM) for log‑normal price evolution

Ornstein–Uhlenbeck (OU) for mean‑reverting dynamics

Merton Jump Diffusion for sudden price shocks

Student‑t Noise Model for fat‑tailed return distributions

Visualization utilities for price paths and return histograms

A clean, extensible project structure

A full Wiki with mathematical derivations and usage examples

The goal of this project is to provide a research‑grade, modular, and extensible foundation for exploring stochastic processes in quantitative finance — bridging theory, simulation, and visualization in a single, well‑structured codebase.


This repository implements a stochastic price simulation framework used to study financial time‑series behavior under different noise and diffusion assumptions.
It includes:

Geometric Brownian Motion (GBM) for log‑normal price evolution

Ornstein–Uhlenbeck (OU) for mean‑reverting dynamics

Merton Jump Diffusion for sudden price shocks

Student‑t Noise Model for fat‑tailed return distributions

Visualization utilities for price paths and return histograms

A clean, extensible project structure

A full Wiki with mathematical derivations and usage examples

The goal of this project is to provide a research‑grade, modular, and extensible foundation for exploring stochastic processes in quantitative finance — bridging theory, simulation, and visualization in a single, well‑structured codebase.

---

## 📈 Overview
This project implements a collection of stochastic models commonly used in quantitative finance to simulate asset prices, returns, and noise behavior.  
It is designed as a research‑grade toolkit for:

- Exploring market dynamics  
- Understanding stochastic processes  
- Testing trading ideas on synthetic data  
- Studying noise models and fat‑tailed behavior  
- Building intuition for volatility, drift, and mean‑reversion  

The simulator is modular, extensible, and written with clean engineering structure.

---

## 🚀 Features
- **Geometric Brownian Motion (GBM)**  
- **Ornstein–Uhlenbeck (OU)**  
- **Jump Diffusion (Merton Model)**  
- **Student‑t Noise Model**  
- Visualization utilities  
- Statistical analysis tools  
- Jupyter notebook demos  

---

## 🧩 Project Structure
```
stochastic-price-simulator/
│
├── src/
│   ├── processes/
│   │   ├── gbm.py
│   │   ├── ornstein_uhlenbeck.py
│   │   ├── jump_diffusion.py
│   │   ├── student_t_noise.py
│   │   └── __init__.py
│   │
│   ├── utils/
│   │   ├── plot.py
│   │   └── stats.py
│   │
│   └── main.py
│
├── notebooks/
│   └── demo.ipynb
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## 📦 Installation
```bash
git clone https://github.com/<your-username>/stochastic-price-simulator.git
cd stochastic-price-simulator
pip install -r requirements.txt
```

---

## 🧠 Usage Example
```python
from src.processes.gbm import GeometricBrownianMotion
from src.utils.plot import plot_price_path

gbm = GeometricBrownianMotion(mu=0.05, sigma=0.2)
prices = gbm.simulate_path(1000, S0=100)

plot_price_path(prices, title="GBM Price Simulation")
```

---

## 📘 Notebook Demo
See `notebooks/demo.ipynb` for examples and visualizations.

---

## 🎯 Roadmap
- Add Heston stochastic volatility model  
- Add regime‑switching models  
- Add calibration tools  
- Add portfolio‑level simulations  

---

## 📄 License
MIT License.
