if 2 > 1:
    print("2 > 1")


for i in range(1,3):
    print(i)

indexWhileLoop = 10

while indexWhileLoop > 0:
    print("index is")
    indexWhileLoop = indexWhileLoop - 1

from math import sqrt as square_root

result = square_root(16)
print(result)

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"An error occured: {e}")


with open("test.txt", 'r') as text:
    content = text.read()
    print(content)

import numpy as np

array = np.array([1,2,3])
print(array)

def divide(a, b):
    assert b != 0, "The divisor must not be zero."
    return a / b

result = divide(10, 2)  # This will work
# result = divide(10, 0)  # This will raise an AssertionError with the message "The divisor must not be zero."