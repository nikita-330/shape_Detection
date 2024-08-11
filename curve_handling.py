import numpy as np
import matplotlib.pyplot as plt

def complete_curve(XY):
    if len(XY) < 3:
        return XY
    completed_XY = np.copy(XY)
    if not np.allclose(XY[0], XY[-1]):
        completed_XY = np.vstack([completed_XY, XY[0]])
    return completed_XY

def complete_curves(XYs):
    completed_curves = []
    for XY in XYs:
        completed_curve = complete_curve(XY)
        completed_curves.append(completed_curve)
    return completed_curves

def plot(paths_XYs, output_path):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    colours = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, XYs in enumerate(paths_XYs):
        c = colours[i % len(colours)]
        for XY in XYs:
            ax.plot(XY[:, 0], XY[:, 1], c=c, linewidth=2)
    ax.set_aspect('equal')
    plt.savefig(output_path, format='png')