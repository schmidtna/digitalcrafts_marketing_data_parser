# decorators are functions that get called before other functions
# functools library has decorators we'll use in this ex
import functools


def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the deocrator!")
        func()
        print("After the decorator!")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")

#my_function()

    # my function is passed into my decorator as func
    # then my function is replaced by function that runs func

##

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator!")
            if number == 56:
                print("Not running the function")
            else:
                func(*args, **kwargs)
            print("After the decorator!")
        return function_that_runs_func
    return my_decorator



@decorator_with_arguments(90)
def my_function_too(x, y):
    print(x + y)

my_function_too(100, 200)

# useful for validation such as user/admin credentials or database entries
# should have args and kwargs in decorator so you can pass in parameters from passed in function