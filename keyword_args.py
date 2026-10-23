'''
In Python, keyword arguments are arguments that are preceded by an identifier (the parameter’s name) when you call a function.
They make your code easier to read and allow you to change the order of arguments when calling a function.
'''
def hello(gretting,title,first,last):
    print(gretting,title,first,last)

#call the function with poitional arguments - this means the order matters:
hello("Hello", "Mr.", "Evan", "Burlingame")
#what happens when we change the order
hello("Evan", "Hello", "Nurlingame", "Mr.")
# try again with keyword arguments

hello(first="Evan", gretting="Hello", last = "Burlingame", title="Mr.")

#Note: You can mix, but positional args must be first
hello("Hello," "Mr.", last="Burlingame", first="Evan")