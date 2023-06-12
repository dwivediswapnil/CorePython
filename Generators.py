def generator_function():
    for i in range(100):
        #yield pauses the function
        yield i

for item in generator_function():
    print(item)
#######################################
def fib(number):
    a=0
    b=1 
    for i in range(number):
        yield a
        temp =a 
        a=b
        b=temp+b

for x in fib(10):
    print(x)
########################################