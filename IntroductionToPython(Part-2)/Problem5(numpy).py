import numpy as np

matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

rowNum = 1

for i in matrix:
    sumOfRow = 0
    for j in i:
        sumOfRow = sumOfRow + j
    print(f"Sum of row {rowNum}: {sumOfRow}")
    print("End of row\n")
    rowNum += 1


