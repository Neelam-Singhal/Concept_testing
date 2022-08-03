# Decorator is a function that takes in another function as an argument,
# add some kind of functionality and
# then returns another function
# All of this is done without altering the source code of the original function that you passed in

# Why to use Decorator -> Add functionaly to existing function without changing the existing code
def decorator_function(original_function): # Passing in a function as an argument
    def wrapper_function(*args, **kwargs):
        print("This function is executed before {} function".format(original_function.__name__))
        return original_function(*args)  # Executing the original function. May add new functionality to it
    return wrapper_function  # Retuning a new function



# def display():
#     print( "Run Display function")

# decorator_variable = decorator_function(display)
# decorator_variable()    

# @decorator_function means --> display = decorator_function(display)
# Essentially, the output of display() has been updated without actually changing the code for display() function and instead using a decorator.

@decorator_function
def display():
    print( "Run Display function")
display()

@decorator_function
def creds(name, age):
    print("Name: {}, age: {}".format(name, age))

creds("Neelam",36)