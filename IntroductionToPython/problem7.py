# • Write a python program to find the largest number between two numbers using function
def findLargest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
largest = findLargest(num1, num2)

print("The largest number between " + str(num1) + " and " + str(num2) + " is: " + str(largest))
