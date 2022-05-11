#202103103510506
#Kushagra Peter
#B.tech CSE

'''
Write a python program to demonstrate the use of arbitrary arguments.
'''


def greet(*names):
    """This function greets all
    the person in the names tuple."""

    for name in names:
        print("Hello", name)


greet("Kush", "Milan", "Dhwani", "Aisha")