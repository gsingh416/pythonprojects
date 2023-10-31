# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be
'''
2
4
6
8
10
12
14
16
18
20
'''

num = int(input("Enter the number for which you want the table:- "))

print(f"The multiplication table for {num} is as follows: \n")

for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
    print("\n")
