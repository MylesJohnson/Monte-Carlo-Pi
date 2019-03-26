import random

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

iterations = 100


inside_count = 0


def animate(i):
    global inside_count

    # Do 50 per frame
    xy_subset = xy[:, 50*i:50*(i+1)]
    in_marker = np.hypot(*xy_subset) <= 1
    in_xy = xy_subset[:, in_marker]
    out_xy = xy_subset[:, ~in_marker]

    inside_count += np.sum(in_marker)
    pi = inside_count / (50 * (i + 1)) * 4
    
    ax.set_title('Pi Estimate: {:.4f}'.format(pi))
    ax.scatter(*in_xy, c='g', s=15)
    ax.scatter(*out_xy, c='r', s=15)


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)

    xy = np.random.uniform(-1, 1, (2, 50 * iterations))

    anim = animation.FuncAnimation(fig, animate, frames=iterations)
    anim.save('demoanimation.gif', writer='imagemagick', fps=10)
