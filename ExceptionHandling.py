# try:
#     a=5
#     b=int(input)
#     print(a/b) 
# except:
#     print("There was a mistake")   
# print("This is my code")    

#Try-catch won't handle syntactical mistakes
# try:
#     l=[1,2,3,4,4]
#     for i  range(len(l)):
#         print(l)
# except:
#     print("This is my code")    

# try:
#     l=[1,2,3,4,4]
#     for i in range(len(l)+1):
#         print(l[i])
# except Exception as e:#Exception is a class
#     print("Error: ",e)     

try:
    a=int(input())
    b=int(input())
except Exception as e :
    print(e)   