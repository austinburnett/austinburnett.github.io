"""Plots the relationship between z_eye and the depth buffer z-value."""

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np

# The near and far plane boundaries.
near = 0.1
far = 100.0

def z_eye_to_depth_buffer_value(z_eye: float):
    z_eye = -z_eye

    z_ndc = (z_eye * (-far - near) - 2 * far * near) / (-z_eye * (far - near))
    depth_buffer_value = (z_ndc + 1) / 2.0

    return depth_buffer_value

def main():
    z_eye_values = np.arange(near, far, 0.1)
    function = np.vectorize(z_eye_to_depth_buffer_value)
    depth_buffer_values = function(z_eye_values)

    fig, ax = plt.subplots()

    slope, = ax.plot(z_eye_values, depth_buffer_values, linewidth=2)
    slope.set_label("Depth Buffer Value")

    ax.set(
        xlim=(0.1, 100),
        ylim=(0, 1),
        xlabel=f"Eye Space Depth (near = {near}, far = {far})",
        ylabel="Depth Buffer Value",
        title="Depth Buffer Value vs. Eye Space Depth"
    )

    ax.set_yticks(np.arange(depth_buffer_values.min(), depth_buffer_values.max() + 0.1, 0.1))

    # Setting the x-axis to logscale helps with visualizing the relationship between the axes.
    ax.set_xscale("log")

    if ax.get_xscale() == "log":
        ax.set_xticks([0.1, 0.2, 5, 10, 50, 100])

    ax.xaxis.set_major_formatter(ScalarFormatter())

    ax.ticklabel_format(style='plain')
    ax.minorticks_off()
    ax.grid()
    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()
