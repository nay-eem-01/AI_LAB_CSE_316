import matplotlib.pyplot as plt

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature = [22, 24, 25, 23, 26, 28, 27]

plt.figure(figsize=(8, 5))
plt.plot(days, temperature, marker='o', linestyle='-', color='b', label='Temperature (°C)')

plt.xlabel('Day of the Week')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Variations Over a Week')
plt.grid(True)
plt.legend()

plt.show()