#   WAP to print a diamond pattern
'''
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * * 
      * * * 
        *
'''

n = 5

for a in range(n-1):
    for b in range(a,n):
        print(" ",end = " ")
    for c in range(a):
        print("*",end = " ")
    for d in range(a+1):
        print("*",end = " ")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end = " ")
    for k in range(i,n):
        print("*",end = " ")
    for l in range(i,n-1):
        print("*",end = " ")

    print()
