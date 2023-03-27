t=(1,2,3,4,5)
print(type(t))

t1 = ("sudh",12,3,'d',2+8j,True) #Tuple
print (t1)

l1=[12,23,"we"] #List
print(l1)

print(l1[0:2])
print(t1[0:2])

#printing tuple in reverse
print(t1[::-1])
print(t1[-1])
#with a jump of 2
print(t1[0::2])

l1=[2,3,4,5]
l1[0]="Karan"
print(l1)

# List is demnoted by [] and tuple is denoted by ()
# In list , elements can be re-assigned whereas not in Tuple.

# t1=(1,2,3,4,5)
# t1[0]="AB"
# print(t1) #won't be possible since its immutable just like string. 

t1=(1,2,3,4,5)
t2=(6,7,8,9)
print(t1+t2)#appending tuple and similarly for List

print(t1*2) #Repeating and adding
#methods related to Tuple are limited uinlike List.
print(t1.count(1))#number of occurrences
print(t1.index(2))#first occurences.

#When we do not want other want to make changes , then we use tuple as its immutable.

t2=((1,2),(3,4),(6,7))#We can hold tuple inside a tuple
print(t2)

t3=([1,2,3],4,5)#also list inside a tuple
print(t3)

t3[0][1]="Swapnil" #reasiigning a value inside a list which is present inside a tuple.
print(t3)