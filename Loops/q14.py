# Exercise 14: Reverse a given integer number
'''
Given:

76542

Expected output:

24567
'''

num = int(input("Enter the number which you want to reverse:- "))
num_rev = 0

while num > 0:
    remainder = num % 10
    num_rev = (num_rev * 10) + remainder
    num = num // 10

print(f"Reverse for the entered number is {num_rev}.")
