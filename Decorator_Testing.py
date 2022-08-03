# Decorator is a function that takes in another function as an argument,
# add some kind of functionality and
# then returns another function
# All of this is done without altering the source code of the original function that you passed in

def decorator_function(original_function): # Passing in a function as an argument
    def wrapper_function():
        return original_function()  # Executing the original function. May add new functionality to it
    return wrapper_function  # Retuning a new function


def display():
    print( "Display function")

decorator_variable = decorator_function(display)

decorator_variable()    