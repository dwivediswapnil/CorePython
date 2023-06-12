word ="Hello World"
print(word.find("l"))
print(word.index("l"))
print(word.count("l"))
print(word.count(" "))
print("***************")
print(word[0])
print(word[0:4])
print(word[:4])
print(word[0:-4])
print(word[-4:])
print(word[4:])
print("*****************")
print(word.split(" "))
#Check whether a string starts or end with a character in Python
print(word.startswith('H'))
print(word.endswith('d'))
#Repeat Strings Multiple Times in a String in Python
my_str="PFB OPb"
print(my_str*4)
print(my_str.replace('P','U'))
print(my_str.upper())
print(my_str.lower())
print(my_str.capitalize())
print(my_str.swapcase())
print("".join(reversed(my_str)))
print(my_str[::-1])

str1 = "*********Mario*********"
print(str1.strip("*"))
print(str1.lstrip("*"))
print(str1.rstrip("*"))
print(str1 + my_str)

test_list = ["", "Greece is heaven", "", "is", "best", ""]
while ("" in test_list):
    test_list.remove("")
print(test_list)    

########################################
import random
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10,2))
print(random.choice([1,2,4,2,1,1,34,99]))
print(random.choice("Computer"))
print(random.choice((22,3,113,11)))
numbers = [22,3,113,11]
random.shuffle(numbers)
print(numbers)

my_list = {1,2,3,4,5,6}
# print(my_list[0:5:3])

my_list2=range(1,5,3)
for i in my_list2:
    print(i)

n=[0,1,2,3,4,5]
print (n[1:3] ) 
n[1:3]=(77,)
print (n )   
# n[1:3]='5'
# print (n)

num=[0,1,2,3,4,5]
num1=slice(1,3)
print (num[num1])

num=[0,1,2,3,4,5]
print(num[0:5:2])

for i in range(0,5,2):
    print(i)
    