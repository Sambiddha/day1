# Tuple datatypes are similar to python list type but they are immutable
# Indexing and Slicing in tuple are same as that of list
# Empty tuple can be created using paranthesis () or tuple() built-in function

t = tuple() #an empty tuple
print(t)

t = (1, 2, 3) # an non-empty tuple
print(t)
t = tuple([1, 2, 3]) #tuple() function takes iterable as a parameter

# Creating a tuple with single elements
t = (1) # This seems like a tuple but, it is an integer type
print(type(a))  #int

t = (1, ) # We need to add a comma while creating tuple with single elemets
print(type(a)) #tuple

# Tuple Packing and Unpacking
t = 1, 2, "Hello World" # A tuple can be created without using paranthesis as given in this example. this type of tuple
# creating is tuple packing

# Assigning of the tuple elements to individual variables in the LHS is called tuple unpacking
a, b, c = 1, 2, "Hello World"
print(a) #result => 1
print(b)  #result => 2
print(c) # result => "Hello World"



# This is how we do swapping normally in other language. With the use of 3rd variable (c)

a = 1
b = 2

c = a
a = b
b = c

#Swapping can be implemented easily in python with tuple packing and unpacking
a =1
b = 2
a, b = b, a  #Swapping using tuple packing/unpacking
print(a)
print(b)



# Elements in LHS must be equal to RHS in tuple packing and unpacking else it raises an error
a, b = 1, 2, 3  #This raises an error
# a, b, c = 1, 2 #This also raises an error


# Indexing and Slicing in tuple is same as that of list

a = (1, 2, 3, 4, 5, 6, 7)
print(a[::2]) #this traverse from forward jumping one step
#Result => (1, 3, 5, 7)
print(a[-2:-6:-1]) #Providing negative step size traverse the sequence from backward. Result = (6, 5 , 4, 3)
print(a[::-1])  #This reverses the sequence. Result => (7, 6, 5, 4, 3, 2, 1)


del a #This delets the tuple a (del keyword deletes any object)


