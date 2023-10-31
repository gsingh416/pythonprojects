# Exercise 15: Use a loop to display elements from a given list present at odd index positions
'''
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Note: list index always starts at 0

Expected output:

20 40 60 80 100
'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

l = len(my_list)

odd_my_list = my_list[1::2]
print(odd_my_list)

# for item in range(l,1,2):
    # print(my_list[item])

for item in my_list[1::2]:
    print(item,end = "   ")

