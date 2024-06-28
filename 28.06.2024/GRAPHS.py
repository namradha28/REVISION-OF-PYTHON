#Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations. It is highly customizable and can produce a wide range of plot types.

#BASIC LINE PLOT
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

#SCATTERPLOT
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y, color='red')

# Add title and labels
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()

#BAR CHART 
# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 24, 36, 40]

# Create a bar chart
plt.bar(categories, values, color='green')

# Add title and labels
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show the plot
plt.show()

#PIE CHART
import matplotlib.pyplot as plt

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode the 1st slice (A)

# Create a pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')

# Add title
plt.title('Simple Pie Chart')

# Show the plot
plt.show()
