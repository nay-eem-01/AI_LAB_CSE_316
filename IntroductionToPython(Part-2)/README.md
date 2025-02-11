# AI Lab CSE 316
# Lab Class 02
## **1. Generate a 5x5 Matrix of Random Integers and Compute Row-wise Sums**

### **Input:**
```python
import numpy as np
matrix = np.random.randint(0, 100, size=(5, 5))

Matrix:
[[12 34 56 78 90]
 [23 45 67 89 10]
 [11 22 33 44 55]
 [66 77 88 99  0]
 [ 1  2  3  4  5]]

```
### **Output:**
```python
Row-wise sums:
[270 234 165 330  15]
```




## **2.Create an Array of 100 Random Values and Normalize Them Between 0 and 1**
### **Input:**

```python

random_values = np.random.rand(100)
normalized_values = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))
```

### **Output:**
```python
Row-wise sums:
[270 234 165 330  15]
```
