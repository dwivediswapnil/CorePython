#List,set,dictionary comprehensions
#########################################################################
#LIST
my_list = [char for char in 'hello']
print(my_list)

my_list2 = [num for num in range(10)]
print(my_list2)

my_list3 = [num**2 for num in range(10) if num>=4]
print(my_list3)
############################################################################
#SET
my_list = {char for char in 'hello'}
print(my_list)

my_list2 = {num for num in range(10)}
print(my_list2)

my_list3 = {num**2 for num in range(10) if num>=4}
print(my_list3)
############################################################################
#DICTIONARY
my_dict = {
    'a':1,
    'b':2,
    'c':3
}

output_dict = {key:value**2 for key,value in my_dict.items()}
print(output_dict)

output_dict2 = {key:value**2 for key,value in my_dict.items() if value%2==0}
print(output_dict2)

#If we do not have a dictionary 
my_dict = {num:num*9 for num in [1,2,3,4,5]}
print(my_dict)

###################################################
#duplicates
some_list = ['a','b','c','d','e','f','f','e','g']
# duplicates = []
# for i in some_list:
#     if some_list.count(i)>1:
#         if(i not in duplicates):
#             duplicates.append(i)

# print(duplicates)  

duplicates = set([num for num in some_list if some_list.count(num)>1])
print(duplicates)
