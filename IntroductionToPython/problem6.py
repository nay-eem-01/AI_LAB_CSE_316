# • Write a python program to generate Fibonacci series.

num = int(input("Enter the number of terms for the Fibonacci series: "))
first = 0
second = 1

print("Fibonacci series:")
for i in range(1, num+1):
    print(first, end=" ")
    nextNum = first + second
    first = second
    second = nextNum

