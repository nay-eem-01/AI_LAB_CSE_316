import numpy as np

randomValue = np.random.rand(100)
print("Before Normalization")
print(randomValue)

normalizedValues = (randomValue - np.min(randomValue)) / (np.max(randomValue) - np.min(randomValue))
print("After Normalization")
print(f"Min of normalized values: {np.min(normalizedValues)}")
print(f"Max of normalized values: {np.max(normalizedValues)}")