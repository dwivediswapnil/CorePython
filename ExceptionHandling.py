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
# #     print("Error: ",e)     

# try:
#     a=int(input())
#     b=int(input())
# except Exception as e :
#     print(e)   

#else block will run only when the try block has executed
# try:
#     a=int(input())
#     b=int(input())
# except Exception as e :
#     print("This will handle error",e) 
# else:
#     print("this will execute once try executes")
# try:
#     a=int(input())
#     b=int(input())
# except Exception as e :
#     print("This will handle error",e) 
# else:
#     print("this will execute once try executes successfully, else block executes")
# finally:
#     print("I will execute no matter what")   

#WAP to get the warning untill the input is integer
# def askInput():
#   flag=True
#   while flag:
#     try:
#       a=int(input("Enter the integer"))
#       if type(a)==int:
#         return "yes, you have entered an integer"
#         flag=False
#     except Exception as e:
#       print("Please enter an integer",e)

# askInput()

#Raising an exception
# def test(a):
#   if a<0:
#     raise ZeroDivisionError("You have entered a negative value",a)
#   return a
# test(-5)

#Logging
import logging
logging.basicConfig(filename='test.log',level=logging.INFO,format = '%(asctime)s %(message)s')
logging.info("This is info log")
logging.warning("This is my warning log")
logging.error("This is an error log")
# except Exception as e:
# logging.exception("Exception occured"+str(e))



     




    