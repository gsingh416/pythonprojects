#   WAP to print a triangle pattern
'''
* * * * * * * * *
  * * * * * * *
    * * * * * 
      * * * 
        *
'''

n = 5

for a in range(n):
    for b in range(a+1):
        print(" ",end = " ")
    for c in range(a,n):
        print("*",end = " ")
    for d in range(a,n-1):
        print("*",end = " ")
    print()