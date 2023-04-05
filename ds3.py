# def test():
#     print("Hey , how are you ?")
# test() 
# print(type(test()))   
# print(test()+"Swapnil") #Error: unsupported operand type(s) for +: 'NoneType' and 'str'

# def test2():
#     return "This is my function"
# print(test2())
# print(test2()+" Swap")
# print(type(test2()))

# def test3():
#     return "This is my function",4,3,[1,2,3,44]
# print(test3())#will return a tuple containing everything 
# b=test3()
# print(b[1])
# x,v,u,i=test3()
# print(x)
# print(v)
# print(u)
# print(i)

# l=[1,2,3,4,4,"sudh",[1,2,3,4]]
# def test5(a):
#     n=[]
#     if type(a)==list:
#         for i in a:
#             if type(i)==int:
#                 n.append(i)
#     return n            

# print(test5(l))

# def test6(c):
#     if type(c)==dict:
#         return c.keys()
#     else:
#         return "You haven't passed a dictionary"

# print(test6("ksdjbfksdjf"))

# def test7(a,b):
#     if type(a)==list and type(b)==list:
#         a.extend(b)
#         return a
#     else:
#         return "either of your data is not a list"
    
# print(test7(232,"ss")) 
# print(test7([1,2,3,4],[5,2,3,48]))   

# def starPattern(n):
#     """This function help to create a triangle with any number of rows"""
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("+",end="")
#         print("\r")    
# starPattern(6)   
# help(starPattern)    

# When we have to pass large numberof arguments

# def test1(*args):# We can send any number of arguments 
#     return args

# print(test1(1,2,3,4,45,54,5,5,"drgsgs",55,22))#will return a tuple with the elements (Heterogeneous supported)


# def test1(*args,a):# We can send any number of arguments 
#     return args,a

# print(test1(1,2,2,3,a=23))

#If a has been passed in the beginning/first parameter , 
# the it will consider the very first value been passed to it while function calling.
#after *args , whatever the arguments will bnbe passed has to be binded like a=23   

# def test7(**kwargs):# "**" means any numberof arguments but should be in key value pair format.
#     return kwargs

# print(test7(a=1,b=[1,2,3,4,5]))#will return a dictionary 

# def test8(a,**kwargs):
#     return kwargs,a

# print(test8(11,b=2,c=3))

# def test8(a,**kwargs,*args):#We cannot use **,* in a sequence together(** then *)
#     return kwargs,a,args

# def test9(a,*args,**kwargs):#We cannot use **,* in a sequence together(** then *)
#     return a,args,kwargs#args should be placed before kwargs


# print(test9(12,123,124,125,126,l=1,b=2,c=8))

#lambda function: Anonymous function(function without the name)
# a=lambda a,b:a*b
# print(a(12,12))

# a=lambda a,b:(a*b,a+b)
# print(a(12,13))

# a=lambda *a:a
# print(a(1,2,3))

# v=lambda *i:i**2
# v(1,2,3) #won't work as tuples can't be squared
 
a=lambda a,b:(a*b,a+b)
print(a(4,5))

#iterable,iterator
#iterable means an element which we can access in a sequential manner individually.
# s="Swapnil"
# b=iter(s)#converting iterable object to iterator so that we can access individual element
# print(b)
# print(next(b))
# print(next(b))
# print(next(b))

# s="fsds"
# for i in s:#for loop is trying to convert the string internally using iter function to an iterator then by using next function 
#     #it is giving element
#     print(i)

# s=iter(s)

# print(next(s))

l=[1,2,3,4,5]
#list is iterable
p=iter(l)
print(next(p))

#All iterables are iterator.

#Generator
