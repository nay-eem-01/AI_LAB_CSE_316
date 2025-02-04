# Write a python program to find the smallest number from a set of numbers.

num = int(input("Enter the number of elements in the set: "))
smallest = float('inf')

for i in range(1, num+1):
    current = int(input("Enter number " + str(i) + ": "))
    if  current < smallest:
        smallest = current

print("The smallest number in the set is: " + str(smallest))
