import matplotlib.pyplot as plt

regions = ['North', 'South', 'East', 'West']
revenue = [50000, 60000, 45000, 70000]

plt.figure(figsize=(8, 5))
plt.bar(regions, revenue, color='skyblue', label='Revenue ($)')

plt.xlabel('Region')
plt.ylabel('Sales Revenue ($)')
plt.title('Sales Revenue Across Different Regions')
plt.legend()


plt.show()