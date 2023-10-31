# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
'''
Given:

# number of terms
n = 5
Expected output:

24690
'''

n = 5
a = 2
sum_seq = 0

for i in range(0,n):
    print(a, end="+")
    sum_seq += a
    a = a * 10 + 2

print(f"\n{sum_seq}")
