import matplotlib.pyplot as plt
from sculpture import human_figure

if __name__ == "__main__":
    bounds = [(-1.0, 1.0), (-1.0, 1.0), (-0.2, 2.0)]
    fig = human_figure().plot(bounds, resolution=60)
    plt.show()
