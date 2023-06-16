#Lambda functions: Also known as one time anonymous function.
from functools import reduce

#a normal func
my_list = [1,2,3,4,5,6,7,8]

def multiply_by2(item):
    return item *2

print(list(map(multiply_by2,my_list)))
print(list(map(lambda item:item*2,my_list)))
print(my_list)

# #filter with lambda
result = list(filter(lambda item:item %2==0,my_list))
print(result)
# print(my_list)

# #reduce with lambda
# print(reduce(lambda acc, item:acc+item > 1,my_list))
# #####################################################
# #exe
# my_list = [5,4,3]
# print(list(map(lambda item: item **2,my_list)))

# a=[(0,2),(4,3),(9,9),(10,-1)]
# #key will always be the 2nd one in the tuple.
# print(a.sort(key=lambda x:x[1]))
# print(a)

