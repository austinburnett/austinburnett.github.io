"""Plots the relationship between z_eye and the depth buffer z-value."""

import matplotlib.pyplot as plt
import numpy as np

# The near and far plane boundaries.
n = 0.1
f = 100.0

def z_eye_to_depth_buffer_value(z_eye: float):
    z_eye = -z_eye

    z_ndc = (z_eye * (-f - n) - 2 * f * n) / (-z_eye * (f - n))
    depth_buffer_value = (z_ndc + 1) / 2.0

    return depth_buffer_value

def main():
    z_eye_values = np.arange(0.1, 100.0, 0.1)
    function = np.vectorize(z_eye_to_depth_buffer_value)
    depth_buffer_values = function(z_eye_values)

    fig, ax = plt.subplots()

    slope, = ax.plot(z_eye_values, depth_buffer_values, linewidth=2)
    slope.set_label("Depth Buffer Value")

    ax.set(
        xlim=(0.1, 100),
        ylim=(0, 1),
        xlabel="Eye Space Depth",
        ylabel="Depth Buffer Values",
        title="Depth Buffer Values vs. Eye Space Depth"
    )
    ax.set_yticks(np.arange(depth_buffer_values.min(), depth_buffer_values.max() + 0.1, 0.1))

    ax.set_xscale("log")
    #ax.set_xticks(np.arange(z_eye_values.min(), z_eye_values.max() + 10, 100))
    ax.set_xticks(np.arange(0.1, 100 + 10, 10))
    ax.minorticks_off()

    ax.grid()
    ax.legend()


    plt.show()

if __name__ == "__main__":
    main()
