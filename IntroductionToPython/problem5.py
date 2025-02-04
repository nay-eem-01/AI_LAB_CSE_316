# • Write a python program to find the factorial of a number using for loop.

num = int(input("Enter a number to find its factorial: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i

print("The factorial of " + str(num) + " is: " + str(factorial))
