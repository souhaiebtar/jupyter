import ex26
from pprint import pprint

#pprint(ex26.__dict__)
print("height is", ex26.height)
print("height is also", ex26.__dict__['height'])

print(f"I am currently {ex26.height} inches tall.")

ex26.__dict__['height'] = 1000
print(f"I am now {ex26.height} inches tall.")

ex26.height = 12
print(f"Oops, now I'm {ex26.__dict__['height']} inches tall.")


help(print)
