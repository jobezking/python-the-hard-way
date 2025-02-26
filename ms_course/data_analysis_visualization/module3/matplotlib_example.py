import matplotlib.pyplot as plt
import numpy as np

# Create a figure with a specific size
fig = plt.figure(figsize=(10, 6))  # Width: 10 inches, Height: 6 inches

# Create a figure with 2 rows and 2 columns of subplots
fig, ax = plt.subplots(2, 2)

# Access individual subplots using indexing
ax[0, 0].plot([1, 2, 3], [4, 5, 6])  # Top-left subplot
ax[0, 1].bar(['A', 'B', 'C'], [7, 8, 9])  # Top-right subplot
ax[1, 0].scatter([10, 20, 30], [11, 12, 13])  # Bottom-left subplot
ax[1, 1].hist([1, 1, 2, 3, 3, 3])  # Bottom-right subplot

plt.show()

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Plot Title')
plt.show()

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

# Set tick locations and labels for the x-axis
plt.xticks(np.arange(0, 11, 2), ['0', '2', '4', '6', '8', '10'])

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.show()

x = [1, 2, 3]
y1 = [4, 5, 6]
y2 = [7, 8, 9]

plt.plot(x, y1, label='Data Series 1')
plt.plot(x, y2, label='Data Series 2')

plt.legend()  # Automatically creates a legend based on labels
plt.show()