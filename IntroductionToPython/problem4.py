# Write a python program to find the second highest number from a set of numbers.

num = int(input("Enter the number of elements in the set: "))
largest = -float('inf')
secondLargest = -float('inf')

for i in range(1, num+1):
    current = int(input("Enter number " + str(i) + ": "))
    if  current > largest:
        secondLargest = largest
        largest = current
    elif current > secondLargest:
        secondLargest = current

print("The second highest number in the set is: " + str(secondLargest))
