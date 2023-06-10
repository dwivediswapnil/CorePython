# while True:
#     try:
#         age = int(input('What is your age ?'))
#         print(age)
#     except ValueError: 
#         print('please enter a number')
#     except ZeroDivisionError: 
#         print('please enter a number')    
#     else:
#         print("Everythong looks fine")   
#         break     
#################################################
# def sum(num1,num2):
#     try: 
#         return num1+num2
#     except TypeError as e:
#         print("Plz enter valid numbers" +e)
# print(sum('2',1))
##################################################
while True:
        try: 
            age = int(input('What is your age ?'))
            10/age
            raise ValueError("CIAO CIAO")
        except (TypeError,ValueError) as e:
            print("Plz enter valid numbers" +e)
        except ZeroDivisionError:
            print("Plz enter value more than 0" )  
            break
        else:
            print("Thank you to the end")      
            break
        finally:
            print("Thank you")  
            
        print("Can u hear me")      


