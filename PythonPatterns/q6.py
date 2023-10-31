#   WAP to print a triangle pattern
'''
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
'''

n = 5
for h in range(n):
    for i in range(h,n):
        print(" ",end=" ")
    for j in range(h):
        print("*", end = " ")
    for k in range(h+1):
        print("*", end = " ")
    print()