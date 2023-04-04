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

# l=[2,24,32,"Swap",3+4j,[21,23,43,"swal"]]
# l2=[]
# for i in range(len(l)):
#     print("index",i,"for an element",l[i])

# for i in enumerate(l):
#     print(i)    

# for i in l:
#     if (type(i)==str):
#         l2.append(i)
#         print(l2)
#     elif type(i) == list:
#         for j in i:
#             if type(j) == str:
#                 l2.append(j)
#                 print(l2)    


# print(list(range(3,10)))

# s=" This is Swapnil"
# count =0
# for i in s:
#     count=count+1 #or count+=1
# print (count)    

# print(s[::-1])
# #same pg without slicing 
# for i in range(len(s)-1,-1,-1):
#     print(s[i])

# #to find out vowel
# s="iSwapnil"
# v="AaEeIiOoUu"
# for i in s:
#     if i in v:
#         print("vowel",i)
#     else:
#         print("not vowel",i)    

# #palindrome
# s="tnnt"
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")     
# #or
# s1=""
# for i in s:
#         s1=i+s1
# if s==s1:
#      print("Yes, palindrome")
# else:
#      print("Not plindrome")             

# d={"A":"01","B":"02","C":"03"}
# print("A" in d.items()) #will only search in keys
# #=========================================================
# t_1={"Iapple":{
#      "a":12,
#      "b":10,
#      "c":3
#     },
#     "course":{"d":23,
#           "e":22,
#           "f":1}
# }      
# lst=[]
# for i in t_1.values():
#      for j in i.values():
#           lst.append(j)
#      print(lst)  
#      print(max(lst))        


