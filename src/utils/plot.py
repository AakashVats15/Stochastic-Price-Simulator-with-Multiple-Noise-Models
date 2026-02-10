import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def plot_price_path(prices, title="Price Simulation", figsize=(10, 4)):
    """
    Plot a single simulated price path.
    """
    plt.figure(figsize=figsize)
    plt.plot(prices, linewidth=1.5)
    plt.title(title)
    plt.xlabel("Time Step")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()


def plot_multiple_paths(paths, title="Multiple Price Simulations", figsize=(10, 4)):
    """
    Plot multiple simulated price paths on the same figure.
    paths: list of arrays
    """
    plt.figure(figsize=figsize)
    for p in paths:
        plt.plot(p, alpha=0.6, linewidth=1)
    plt.title(title)
    plt.xlabel("Time Step")
    plt.ylabel("Price")
    plt.tight_layout()
    plt.show()


def plot_return_distribution(returns, title="Return Distribution", bins=50, figsize=(8, 4)):
    """
    Plot histogram of returns with KDE overlay.
    """
    plt.figure(figsize=figsize)
    sns.histplot(returns, bins=bins, kde=True, stat="density")
    plt.title(title)
    plt.xlabel("Return")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.show()