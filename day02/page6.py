print("enter your name: ")

# get input from user and set it to name var
name = input()
print("hello ", name)
print("type of name: ", type(name))

print("enter your age: ")

# get string input and convert it to int
age = int(input())
print("age =", age)
print("type of age = ", type(age))
if age >= 18:
    print("yes.. person can vote")
else:
    print("no.. person can not vote")


