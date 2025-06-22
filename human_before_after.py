import csv
import matplotlib.pyplot as plt
import numpy as np

from sculpture import human_figure, sphere, union


def load_points(path: str) -> np.ndarray:
    points = []
    with open(path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row or row[0].startswith("#"):
                continue
            points.append([float(x) for x in row])
    return np.array(points, dtype=float)


def main():
    before_points = load_points("dataset/human_before.csv")

    fig = plt.figure(figsize=(10, 5))
    ax1 = fig.add_subplot(121, projection="3d")
    ax1.scatter(before_points[:, 0], before_points[:, 1], before_points[:, 2], s=20)
    ax1.set_title("Avant la sculpture")

    base = human_figure()
    added = sphere(radius=0.3, center=(0, 0, 2.0))
    sculpted = union(base, added)

    bounds = [(-1.0, 1.0), (-1.0, 1.0), (-0.2, 2.4)]
    after_points = sculpted.sample(bounds, resolution=50)
    ax2 = fig.add_subplot(122, projection="3d")
    ax2.scatter(after_points[:, 0], after_points[:, 1], after_points[:, 2], s=1)
    ax2.set_title("Après la sculpture")
    plt.show()


if __name__ == "__main__":
    main()
