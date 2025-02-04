# • Write a python program to find the sum of odd and even numbers from a set of numbers.

num = int(input("Enter range: "))
startingNum =int(input('Enter where do you want to start from: '))
sumOfOdd=0
sumOfEven=0
for i in range(startingNum,num+1):
    if i%2 == 0:
        sumOfEven = sumOfEven+i
    else:
        sumOfOdd = sumOfOdd+i


print("Sum of odd numbers in the range: " + str(sumOfOdd))
print("Sum of even numbers in the range: " + str(sumOfEven))