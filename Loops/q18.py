# Exercise 18: Print the following pattern
# Write a program to print the following start pattern using the for loop
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''

for i in range(6):
    print("*"*i)

for j in range(6,1,-1):
    print("*"*j)
    