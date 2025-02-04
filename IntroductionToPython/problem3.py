
# • Write a python program to find the sum of all numbers between 50 and 100, which are divisible by 3 and not divisible by 5.

sumOfNumbers = 0
for i in range(50, 101):
    if i % 3 == 0 and i % 5 != 0:
        sumOfNumbers += i

print("The sum of numbers between 50 and 100 divisible by 3 and not divisible by 5 is: " + str(sumOfNumbers))
