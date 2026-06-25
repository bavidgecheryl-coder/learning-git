# Make a simple chart with Matplotlib
# Run this code to see your plot!

import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [150, 180, 220, 200, 230]

# Create the chart
plt.figure(figsize=(8, 5))
plt.bar(months, sales, color='purple')

# Add labels
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')

# Show the plot
plt.show()
