#   WAP to print a triangle pattern
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

for a in range(n):
    for b in range(a,n):
        print(" ",end = " ")
    for c in range(a):
        print("*",end = " ")
    print()

m = 5

for i in range(m):
    for j in range(i):
        print(" ",end = " ")
    for k in range(i,m):
        print("*",end = " ")
    print()