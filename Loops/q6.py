# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.

num = int(input("Enter the number for which you need to count the digits: "))
counter = 0

while num > 0:
    num = num // 10
    counter = counter + 1

print(counter)

