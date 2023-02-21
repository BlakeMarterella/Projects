import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

# Define the line
line = ax.axvline(0.5, color='red', linewidth=2)

# Define the animation function
def animate(frame):
    x = 0.5 + 0.4 * frame/100  # Update the x-coordinate of the line
    line.set_xdata([x, x])  # Set the new x-coordinate of the line
    return line,

# Define the animation
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

plt.xlim(0, 1)  # Set the x-limits of the plot
plt.ylim(0, 1)  # Set the y-limits of the plot

plt.show()