def my_decorator(func):
    def wrap_func():
        print("****************")
        func()
        print("****************")
    return wrap_func

@my_decorator
def hello():
    print('hello')

@my_decorator
def bye():
    print("Byeeeee")    

hello()
bye()

# #########################################
# #DECORATOR PATTERN
# def my_decorator(func):
#     def wrap_func(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrap_func

# @my_decorator
# def hello1(greeting,emoji = ':('):
#     print(greeting,emoji) 

# hello1('hiiii')       
# ############################################
# from time import time
# def performance(fn):
#     def wrapper(*args,**kwargs):
#         t1 = time()
#         result = fn(*args,**kwargs)
#         t2 = time()
#         print(f'took {t2-t1} sec')
#         return result
#     return wrapper



# @performance
# def long_time():
#     for i in range(199):
#         i*4

# long_time()        
# #############################################
# # Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# def authenticated(fn):
#   def wrapper(user):
#     if user1['valid']== True:
#         return fn(user1)
#     return wrapper

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)