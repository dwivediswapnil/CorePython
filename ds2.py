# print("Enter the income")
# income = int(input())
# print(income)

# l=[1,2,3,4,5,6]
# for i in l:
#     print(i)

# l=(2,2,3,4,5,6)
# for i in l:
#     print(i)    

# l=[1,2,3.3,4+5j,"Swap"]
# for i in l:
#     print(type(i)) 

#append the digits 
# l=(2,2,3,4,5,6)
# l1=[]
# for i in l:
#     print(i+2) 
#     l1.append(i+2)
#     print(l1)

#filter out the integers
# l=[1,2,34,"Swe",3+2j,[12,3,43]]
# l2=[]
# for i in l:
#     if (type(i)==int):
#         l2.append(i)
#         print(l2)
#     elif type(i) == list:
#         for j in i:
#             if type(j) == int:
#                 print(j)    

l=[2,24,32,"Swap",3+4j,[21,23,43,"swal"]]
l2=[]
# for i in range(len(l)):
#     print("index",i,"for an element",l[i])

# for i in enumerate(l):
#     print(i)    

for i in l:
    if (type(i)==str):
        l2.append(i)
        print(l2)
    elif type(i) == list:
        for j in i:
            if type(j) == str:
                l2.append(j)
                print(l2)    

