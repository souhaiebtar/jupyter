# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")
    

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

def testArgs(*args):
    param1, param2, param3 = args
    print(f"""
    param1 is {param1}
    param2 is {param2}
    param3 is {param3}
    """)

testArgs("p1", "p2", "p3")

def print_one_again(arg1):
    print(f"arg1: {arg1}")

y = "First!!!!!"
print_one(y)
