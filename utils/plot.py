# Simple helper for consistent plotting
import matplotlib.pyplot as plt

def basic_map(ax=None, title=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    if title:
        ax.set_title(title)
    ax.set_axis_off()
    return ax
