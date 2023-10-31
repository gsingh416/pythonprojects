# Exercise 13: Find the factorial of a given number
'''
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
Expected output:

120
'''

num = int(input("Enter the number for which you want the factorial:- "))
fact = 1

if num < 0:
    print("Factorials do not exist for numbers less than 0.")

elif num == 0:
    print("Factorial for 0 is 1.")

else:
    for i in range(1,num+1):
        fact = fact * i

print(f"The factorial of {num} is {fact}.")

