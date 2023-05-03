a = "Hello World"
print(len(a)) # Returns the length of a sequence / iterable

print(bool(a)) # here a is non-empty string which is truthy. so it gives true.

print(a[slice(1, 5)])  # slice() function can be used in the string slicing. First parameter is start and
# second is stop slice(start, stop, step) # step can also be provided as the third parameter

print(type(a)) #this returns type of the object inside the function
# here it is string