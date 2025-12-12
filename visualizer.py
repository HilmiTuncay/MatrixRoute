import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional


class Visualizer:
    def visualize(self,
                  grid: List[List[int]],
                  start: Tuple[int, int],
                  end: Tuple[int, int],
                  path: Optional[List[Tuple[int, int]]] = None):

        grid_np = np.array(grid)

        plt.figure(figsize=(7, 7))
        plt.imshow(grid_np, cmap="gray_r")

        # Başlangıç
        plt.scatter(start[0], start[1], color="green", s=100, label="Start")

        # Bitiş
        plt.scatter(end[0], end[1], color="red", s=100, label="End")

        # Yol
        if path:
            xs = [p[0] for p in path]
            ys = [p[1] for p in path]
            plt.plot(xs, ys, linewidth=2, label="Path")

        plt.title("MatrixRoute Visualization")
        plt.legend()
        plt.gca().invert_yaxis()
        plt.show()
        input("Görsel kapatmak için Enter'a bas...")


