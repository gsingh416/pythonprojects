# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
'''
For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55
'''


n = int(input("Enter the number upto which you want the sum:- "))

# Traditional Loop method

sum = 0

for a in range(1,n+1):
    sum = sum + a
    
print(sum)



# Using sum() function

total_sum = sum(range(1,n+1))
print(total_sum)
