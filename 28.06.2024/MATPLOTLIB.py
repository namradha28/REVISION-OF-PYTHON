#Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.
#  It is widely used for its flexibility and ease of use, enabling the creation of a wide range of plots, from simple line graphs to complex multi-plot layouts.

#Here are some key features of Matplotlib:

#Variety of Plots: Supports numerous types of plots such as line plots, scatter plots, bar charts, histograms, pie charts, error bars, box plots, and more.
#Customization: Offers extensive customization options for plots, including color, line style, markers, labels, and annotations.
#Interactive Figures: Allows for the creation of interactive plots that can be zoomed, panned, and updated in real time.
#Integration: Works well with other libraries such as NumPy, pandas, and seaborn. It also integrates with GUI toolkits like Tkinter, Qt, and wxPython.
#Publication Quality: Capable of producing high-quality figures suitable for publication.
#Subplots: Supports complex layouts with multiple subplots in a single figure. 

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y, label='Line 1', color='blue', marker='o')

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Show the plot
plt.show()

#ADVANCED FEATURES 
#1.3D Plotting:
#Using the mpl_toolkits.mplot3d module, you can create 3D plots.
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs)

2.#Animations:
#Matplotlib can create animations using the FuncAnimation class from matplotlib.animation.
from matplotlib.animation import FuncAnimation
def update(frame):
    # Update plot for the given frame
    pass
anim = FuncAnimation(fig, update, frames=range(100))

#3.Customizing Styles:
#Use plt.style.use('style_name') to change the appearance of plots.
plt.style.use('ggplot')
