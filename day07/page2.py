# scope

# global scope
# - variable declared outside of any function/class
num = 10

# print(num)


# def print():
#     print()
#

def function1():
    # local scope
    # - variable declared within a function
    my_var = "myvar"
    print("inside function1")
    print("old my_var = ", my_var)
    my_var = "myvar changed"
    print("new my_var = ", my_var)

    # henceforth consider the num as global variable
    # used to update the global variable value
    global num
    print("old num = ", num)
    num = 500
    print("new num = ", num)


function1()

print("outside function1")
# print("my_var = ", my_var)
print("num = ", num)

