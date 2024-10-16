# What is decorator ? 

# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are typically applied to functions, and they play a crucial role in enhancing or modifying the behavior of functions.

# Assigning Functions to Variables:--------> 

def plus_one(number):
    return number +1

add_one = plus_one
print(add_one(5))

# Defining Functions inside other functions:-----> 

def add(number):
    def addFunc(number):
        return number + 2
    
    result = addFunc(number)
    return result

print(add(7))

# Passing Functions as Arguments to other functions:----> 

def subtractions(number):
    return number - 2

def func_call(s):
    number_to_sub = 6

    return s(number_to_sub)

a = func_call(subtractions)
print(a)

# Functions returning other functions:--------> 

def hello_func():
    def say_hi():
        return "Hi"
    
    return say_hi

hello = hello_func()
print(hello())

# Nested Functions have access to the Enclosing Function's Variable Scope

def print_message(message):
    "Enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)

    message_sender()

print_message("Some random message")

# Creating Decorators 

def uppercase_decorator(func):
    def wrapper():
        f = func()
        make_uppercase = f.upper()
        return make_uppercase
    
    return wrapper

def say_hi():
    return 'hello world!'
decorate = uppercase_decorator(say_hi)
print(decorate())

@uppercase_decorator
def say_hello():
    return 'hello world'

print(say_hello())

# Applying multiple decorators to a single function 

import functools

def split_string(func):
    @functools.wraps(func)
    def wrapper():
        f = func()
        splitted_string = f.split()
        return splitted_string
    return wrapper

@split_string
@uppercase_decorator
def say_hey():
    return 'hello! guys'

print(say_hey()) 

# Accepting arguments in decorator functions 

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_arguments

@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities are: {0},{1} ".format(city_one, city_two))   

print(cities("Delhi", "Mumbai"))     

# Defining general purpose decorators 

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
