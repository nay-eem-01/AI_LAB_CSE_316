import pandas as pd
import numpy as np

data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, 5],
    'C': [1, 2, 3, np.nan, 5]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

df_filled = df.fillna(df.mean())

print("\nDataset after filling missing values with column-wise means:")
print(df_filled)