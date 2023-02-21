import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Define the initial positions of the dots
dots = ax.plot([0.2, 0.2, 0.8, 0.8], [0.2, 0.8, 0.2, 0.8], 'ro')

# Define the animation function
def animate(frame):
    if frame < 50:
        # Move the dots to the top right corner
        dots[0].set_xdata([0.2 + 0.012 * frame, 0.8 - 0.012 * frame, 0.2 + 0.012 * frame, 0.8 - 0.012 * frame])
        dots[0].set_ydata([0.2 + 0.012 * frame, 0.8 - 0.012 * frame, 0.8 - 0.012 * frame, 0.2 + 0.012 * frame])
    else:
        # Move the dots back to their initial positions
        dots[0].set_xdata([0.2 + 0.012 * (100 - frame), 0.8 - 0.012 * (100 - frame), 0.2 + 0.012 * (100 - frame), 0.8 - 0.012 * (100 - frame)])
        dots[0].set_ydata([0.2 + 0.012 * (100 - frame), 0.8 - 0.012 * (100 - frame), 0.8 - 0.012 * (100 - frame), 0.2 + 0.012 * (100 - frame)])
    return dots

# Define the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.xlim(0, 1)  # Set the x-limits of the plot
plt.ylim(0, 1)  # Set the y-limits of the plot

plt.show()
