# parameterless function
def function1():
    print("inside function1")


# function1()

# parameterized function
def function2(param1):
    print("inside function2")
    print("param1 = ", param1)
    print("type of param1 = ", type(param1))



# function2(10) #int
# function2(4.5) #float
# function2("steve") #string



def function3(param1, param2):
    addition = param1 + param2
    print("addition = ", addition)


function3(10, 30)
function3("test1", "test2")
function3('40', '50')