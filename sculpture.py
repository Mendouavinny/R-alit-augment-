import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401  # needed for projection='3d'

class ImplicitSurface:
    """Représente une surface implicite définie par une fonction F(x, y, z)."""

    def __init__(self, func):
        self.func = func

    def __call__(self, x, y, z):
        """Evaluate the implicit function."""
        return self.func(x, y, z)

    def sample(self, bounds, resolution=50):
        """Retourne un nuage de points appartenant à la surface."""
        x = np.linspace(bounds[0][0], bounds[0][1], resolution)
        y = np.linspace(bounds[1][0], bounds[1][1], resolution)
        z = np.linspace(bounds[2][0], bounds[2][1], resolution)
        X, Y, Z = np.meshgrid(x, y, z)
        F = self.func(X, Y, Z)
        points = np.vstack((X[F <= 0], Y[F <= 0], Z[F <= 0])).T
        return points

    def plot(self, bounds, resolution=50, show=True, ax=None):
        """Affiche le nuage de points de la surface.

        Parameters
        ----------
        bounds : list
            Bornes [xmin,xmax], [ymin,ymax], [zmin,zmax].
        resolution : int, optional
            Nombre de points par axe.
        show : bool, optional
            Si True, appelle ``plt.show()``. Utile hors de Streamlit.
        ax : matplotlib Axes, optional
            Axe 3D existant dans lequel dessiner la surface.
        """
        points = self.sample(bounds, resolution)
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
        else:
            fig = ax.figure

        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Surface implicite')
        if show:
            plt.show()
        return fig


def sphere(radius=1.0, center=(0.0, 0.0, 0.0)):
    """Crée une surface implicite représentant une sphère."""
    def f(x, y, z):
        cx, cy, cz = center
        return (x - cx) ** 2 + (y - cy) ** 2 + (z - cz) ** 2 - radius ** 2
    return ImplicitSurface(f)


def cylinder(radius=0.5, height=1.0, center=(0.0, 0.0, 0.0)):
    """Crée une surface implicite représentant un cylindre vertical."""

    def f(x, y, z):
        cx, cy, cz = center
        radial = np.sqrt((x - cx) ** 2 + (y - cy) ** 2) - radius
        height_val = np.abs(z - cz) - height / 2
        return np.maximum(radial, height_val)

    return ImplicitSurface(f)


def union(surf1: ImplicitSurface, surf2: ImplicitSurface) -> ImplicitSurface:
    """Return the union of two implicit surfaces."""

    def f(x, y, z):
        return np.minimum(surf1(x, y, z), surf2(x, y, z))

    return ImplicitSurface(f)


def intersection(surf1: ImplicitSurface, surf2: ImplicitSurface) -> ImplicitSurface:
    """Return the intersection of two implicit surfaces."""

    def f(x, y, z):
        return np.maximum(surf1(x, y, z), surf2(x, y, z))

    return ImplicitSurface(f)


def difference(surf1: ImplicitSurface, surf2: ImplicitSurface) -> ImplicitSurface:
    """Return the difference of two implicit surfaces (surf1 minus surf2)."""

    def f(x, y, z):
        return np.maximum(surf1(x, y, z), -surf2(x, y, z))

    return ImplicitSurface(f)


def human_figure() -> ImplicitSurface:
    """Approximation grossière d'une silhouette humaine."""

    head = sphere(radius=0.25, center=(0, 0, 1.7))
    torso = cylinder(radius=0.3, height=1.0, center=(0, 0, 1.1))
    arm_l = cylinder(radius=0.1, height=0.8, center=(-0.55, 0, 1.1))
    arm_r = cylinder(radius=0.1, height=0.8, center=(0.55, 0, 1.1))
    leg_l = cylinder(radius=0.12, height=1.1, center=(-0.2, 0, 0.25))
    leg_r = cylinder(radius=0.12, height=1.1, center=(0.2, 0, 0.25))

    figure = union(head, torso)
    for limb in (arm_l, arm_r, leg_l, leg_r):
        figure = union(figure, limb)
    return figure


if __name__ == "__main__":
    sphere1 = sphere(radius=1.0, center=(-0.5, 0, 0))
    sphere2 = sphere(radius=1.0, center=(0.5, 0, 0))
    combined = union(sphere1, sphere2)
    bounds = [(-1.5, 1.5), (-1.5, 1.5), (-1.5, 1.5)]
    combined.plot(bounds, resolution=60)
