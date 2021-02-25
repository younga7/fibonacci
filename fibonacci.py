# CS362 In class activity
# Alex Young
# 2/25/2021
# Run this file using python3 HW4.py
# This program returns a value in the fibonacci sequenec

def series(x):
    try:
        if (x < 0):
            return("Negative Input")
    except TypeError:
        return("Type Error")
    return fibo(x)

def fibo(x):
    if (x <= 1):
        return x
    return fibo(x - 1) + fibo(x - 2)


def factorial(x):
    try:
        if (x < 0):
            return("Negative Input")
    except TypeError:
        return("Type Error")
    return r_factorial(x)

def r_factorial(x):
    if (x == 0):
        return 1
    return x * factorial(x - 1)

