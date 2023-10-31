# WAP to print a triangle pattern
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

n = 5
for i in range(n):
    for j in range(i):
        print("*",end = " ")   
    print()

for h in range(n):
    for k in range(h,n):
        print("*",end=" ")
    print()