#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass

def greet(name):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1,num2):
    sum = int(num1) + int(num2)
    return(sum)
    pass

def halve(number):
    number = float(number / 2)
    return number
    pass
