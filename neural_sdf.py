import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt

from sculpture import sphere


def generate_dataset(surface_func, bounds, n_samples=10000):
    """Generate random points and signed values using the given surface."""
    x = np.random.uniform(bounds[0][0], bounds[0][1], n_samples)
    y = np.random.uniform(bounds[1][0], bounds[1][1], n_samples)
    z = np.random.uniform(bounds[2][0], bounds[2][1], n_samples)
    X, Y, Z = np.stack([x, y, z], axis=1).T
    values = surface_func(X, Y, Z)
    points = np.vstack([x, y, z]).T
    return points.astype(np.float32), values.astype(np.float32)[:, None]


class SDFNetwork(nn.Module):
    """Simple fully connected network."""

    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(3, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.net(x)


class ComplexSDFNetwork(nn.Module):
    """Deeper network for more complex shapes."""

    def __init__(self):
        super().__init__()
        layers = []
        in_dim = 3
        for _ in range(5):
            layers.append(nn.Linear(in_dim, 128))
            layers.append(nn.ReLU())
            in_dim = 128
        layers.append(nn.Linear(128, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)


def train_sdf(surface_func, bounds, epochs=100, lr=1e-3, complex_model=False):
    points, values = generate_dataset(surface_func, bounds)
    model_cls = ComplexSDFNetwork if complex_model else SDFNetwork
    model = model_cls()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()
    inputs = torch.from_numpy(points)
    targets = torch.from_numpy(values)

    for epoch in range(epochs):
        optimizer.zero_grad()
        preds = model(inputs)
        loss = loss_fn(preds, targets)
        loss.backward()
        optimizer.step()
        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

    return model


def plot_sdf(model, bounds, resolution=50):
    x = np.linspace(bounds[0][0], bounds[0][1], resolution)
    y = np.linspace(bounds[1][0], bounds[1][1], resolution)
    z = np.linspace(bounds[2][0], bounds[2][1], resolution)
    X, Y, Z = np.meshgrid(x, y, z)
    pts = np.vstack([X.ravel(), Y.ravel(), Z.ravel()]).T
    with torch.no_grad():
        sdf_vals = model(torch.from_numpy(pts.astype(np.float32))).numpy().reshape(X.shape)
    mask = sdf_vals <= 0
    points = np.vstack((X[mask], Y[mask], Z[mask])).T
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=1)
    ax.set_title('Neural SDF surface')
    plt.show()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Train a neural SDF")
    parser.add_argument("--complex", action="store_true", help="use a deeper network")
    args = parser.parse_args()

    surf = sphere(radius=1.0)
    bounds = [(-1.5, 1.5), (-1.5, 1.5), (-1.5, 1.5)]
    model = train_sdf(surf.func, bounds, epochs=200, complex_model=args.complex)
    plot_sdf(model, bounds, resolution=60)
