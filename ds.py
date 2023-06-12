#============================================================================================================
#TUPLE and LIST
t=(1,2,3,4,5)
print(type(t))

#tuple is heterogeneous.
t1 = ("sudh",12,3,'d',2+8j,True) #Tuple
print (t1)

#List is heterogeneous.
l1=[12,23,"we"] #List
print(l1)

print(l1[0:2])
print(t1[0:2])

# #printing tuple in reverse
print(t1[::-1])
print(t1[-1])
# #with a jump of 2
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
# #methods related to Tuple are limited uinlike List.
print(t1.count(1))#number of occurrences
print(t1.index(2))#first occurences.

# #When we do not want other want to make changes , then we use tuple as its immutable.

t2=((1,2),(3,4),(6,7))#We can hold tuple inside a tuple
print(t2)

t3=([1,2,3],4,5)#also list inside a tuple
print(t3)

t3[0][1]="Swapnil" #reasiigning a value inside a list which is present inside a tuple.
print(t3)

t4 = [(1,2,3,4),4,5,6,]#List can contain a tuple
print(t4)

#-------------------------------------------------------------------------------------------------------------------#
#SET
#Set is a collection which tries to hold unique elements

s1 ={1,3,5,6,4,2,5,7}
print(type(s1))
print(s1)#by default duplicates will be removed.

s2={} #dictionary (empty set)
print(type(s2))

# print(s1[0]) #set is not ordered collection

#but if we store it in list then we can
print(list(s1))

s1.add("Swap")
print(s1)

#Set will not allow list as list is mutable 
# s1.add([1,2,3]) # We cannot store list inside set coz it will not allow any element that is mutable 
print(s1)
s1.add((1,2,3,4))#it will allow tuple.
s1.add((1,2,3,4))
print(s1)
s3={1,2,3,5,5}
print(s3)
s3.remove(5)
print(s3)
s3.discard(2) #if the element is not contained , then it will execute but won't give any error.
print(s3)

#set is unordered collection so is not mutable since there are no indexes.
p={"swap","swap"}
print(p)

#==================================================================================================================
#DICTIONARY: We store in key-value pair.
d={4:"swap"}
print(d)

d1={"key1":5445,"key2":"SAM","key3":[1,2,34,4]}
print(d1)

print(d1["key1"])
print(d1["key3"][1])

d = {3:["asd","sws",2,3,45]}
print(d)#special character names of keys are not allowed
#key being ".4" will work .
d2={"key1":5445,"key2":"SAM","key3":[1,2,34,4],"key3":[1,2,34,4],"key3":[1,2,34,4]}
print(d2["key3"])#key will always be able to hold the recent value not the previous one .Key is suppose to be unique. It wont give error 
# #It will simply update values can be same for keys.
print(d2)

d2={'name':"Swapnil",'Mo_num':541351351,'mail':"asdfsa@sdf.com",'key1':[1,2,3,4],'key2':(1,2,34,4),'key3':{1,2,3,4,4,5,5,5}}
print(d2)
print(d2['key2'])

print(d2.keys())
print(d2.items())#will return a list of items

d={'key1':"swpan0",'key2':[1,2,3,4]}
d['key3']="Kumar" #adding a new key 
print(d)

d['key1'] = "skdjfns"
print(d)

del d['key2']
print(d)

# del d #deletes the whole dictionary

# d1 = {'key1':'sudh', 'key2': [1,2,3,4]}
# # d1[[1,2,3,4,5]] = "pikachu" #List cannot be used as a key 
# d1[(1,2,3,4,5)] = "pikachu" #whereas tuple can be used as a key.
# print(d1)

# print(d1.get("key")) #if the key is not there , then it will return none.

d1={'key1':"skjdhf","key2":"asdas"}
d2 = {'key3':12,"key4":[1,2,3,4,]}
d1.update(d2)#will combine d1 with d2.
print(d1)
# print(d1+d2)#incase of dictionary "+" won't work but it will work in case of List.