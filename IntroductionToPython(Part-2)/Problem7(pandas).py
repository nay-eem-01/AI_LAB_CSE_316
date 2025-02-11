import pandas as pd

df = pd.read_csv('sales_data.csv')

print("Sales Data:")
print(df.head())

df['Revenue'] = df['Quantity'] * df['Price']

total_revenue_per_product = df.groupby('Product')['Revenue'].sum()

df.to_csv("sales_data_with_revenue.csv", index=False)

print("\nTotal Revenue per Product:")
print(total_revenue_per_product)