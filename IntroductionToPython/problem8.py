# • Write a python program to find the sum of the numbers passed as parameters.

def findSum(*numbers):
    totalSum = 0
    for num in numbers:
        totalSum += num
    return totalSum

numCount = int(input("Enter the number of elements to sum: "))
numbers = []

for i in range(1, numCount + 1):
    currentNum = int(input("Enter number " + str(i) + ": "))
    numbers.append(currentNum)

sumOfNumbers = findSum(*numbers)

print("The sum of the numbers is: " + str(sumOfNumbers))
