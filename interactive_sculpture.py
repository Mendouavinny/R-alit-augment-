import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

from sculpture import sphere, union


def update(val):
    r1 = slider1.val
    r2 = slider2.val
    s1 = sphere(radius=r1, center=(-0.5, 0, 0))
    s2 = sphere(radius=r2, center=(0.5, 0, 0))
    combined = union(s1, s2)
    points = combined.sample(bounds, resolution=50)
    scatter._offsets3d = (points[:, 0], points[:, 1], points[:, 2])
    fig.canvas.draw_idle()


if __name__ == "__main__":
    bounds = [(-1.5, 1.5), (-1.5, 1.5), (-1.5, 1.5)]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    plt.subplots_adjust(bottom=0.25)

    s1 = sphere(radius=1.0, center=(-0.5, 0, 0))
    s2 = sphere(radius=1.0, center=(0.5, 0, 0))
    combined = union(s1, s2)
    points = combined.sample(bounds, resolution=50)
    scatter = ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
    ax.set_title("Union interactive de deux sph\xE8res")

    axcolor = 'lightgoldenrodyellow'
    ax_r1 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
    ax_r2 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

    slider1 = Slider(ax_r1, 'Rayon 1', 0.1, 1.5, valinit=1.0)
    slider2 = Slider(ax_r2, 'Rayon 2', 0.1, 1.5, valinit=1.0)

    slider1.on_changed(update)
    slider2.on_changed(update)

    plt.show()
