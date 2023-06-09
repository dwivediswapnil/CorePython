# Functional Programming: map,filter,zip,reduce
from functools import reduce

# map (action,[1,2,3])
#map(multily_by_2,[1,2,4])
my_list = [1,2,3,4,5]
def multiply_by_2(item):
    return item *2        

#List has to be applied to print the value otherwise it will print the object 
print(list(map(multiply_by_2,my_list)))
#returns a new list 

#=============================================================================#
#filter
my_list2 = [1,2,3,4,5]
    
def only_odd(item):
    return item %2 !=0  

#List has to be applied to print the value otherwise it will print the object 
print(list(filter(only_odd,my_list2)))
#original list won't be  modified

print(my_list2)
#============================================================================#
#Zip
my_list3 = [1,2,3]
my_list4 = [10,20,30]
my_list5 = [40,50,60]

print(list(zip(my_list3,my_list4,my_list5)))
#original list won't be  modified

print(my_list3)    
#=============================================================================#
#Reduce
my_list= [1,2,3]
def multiply_by2(item):
    return item*2

def accumulator(acc , item):
    print(acc,item)
    return (acc+item)

print(reduce(accumulator,my_list,0))
print(my_list)

#####################################################################################
# Assignment
from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalizeTheListItems(string):
    return string.upper()

print(list(map(capitalizeTheListItems, my_pets)))  


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def only50Percent(item):
    return item>50

print(list(filter(only50Percent,scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accumulato(acc , item):
    # print(acc,item)
    return (acc+item)

print(reduce(accumulato,(my_numbers + scores),0))