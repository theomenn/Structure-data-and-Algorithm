# Creating Decorators
def uppercase_decorator(function):
    def up():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return up

@uppercase_decorator
def say_hi():
    return 'hello there'

print(say_hi())



# Applying Multiple Decorators to a Single Function
import functools

def split_str(func):
    @functools.wraps(func)
    def wrapper():
        return func().split()
    return wrapper

@split_str
def say_hi():
    "This will say hi"
    return 'hello there'

print(say_hi())

# Accepting Arguments in Decorator Functions

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f'My arguments are: {arg1}, {arg2}')
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def intro(name, age):
    print(f'My name is {name} and I am {age} years old')

intro('Abdi', 18)


# Defining General Purpose Decorators
def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()

# contoh program
import time

# Decorator untuk mengukur waktu eksekusi fungsi
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = round(end_time - start_time)
        
        print(f"Waktu eksekusi untuk {func.__name__}: {execution_time} detik")
        return result
    return wrapper

# Menggunakan decorator dengan sintaksis @decorator
@timing_decorator
def example_function():
    print("Mengeksekusi fungsi...")
    time.sleep(2)

# Memanggil fungsi yang telah dihias
example_function()
