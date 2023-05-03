# LIst are mutable datatypes in python

# Empty list can be created using built-in list() function
a = list() #This gives emptylist 'a'
b = [] # Empty list can also be created in this way

c = [1, 2, 3] #This is a non-empty list

#List are heterogenous datatypes. that means it can have the elements of  different data types

c = [1,"Hello",[5, 6, 7], (1, 2)]  #List with multiple datatypes
print(c)


# Accessing list elements
# List elements can be accessed with indexing and slicing.
# List indexing starts from 0 for forward indexing and -1 for backward indexing

a = [1, "Hello", "World",5.8, [4, 5, 6], 5]
print(a[0]) # This gives 1
print(a[-1]) # Negative index starts from -1. So it gives 5

print(a[4])  # it gives [4, 5, 6]
print(a[-5]) # it gives 'hello'

print(a[4][1])  # it gives 5 from nested list.
 #print(a[6]) #this gives list index out of range error
 #print(a[-8]) #same as above


# We can assign item in any particular index of a list
a[2] = 10 # This changes the value at 2nd index of the list to 10


# Slicing in List
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:])  #this gives exactly the same list
print(a[:6]) #this includes elements from 0 to 5. 6 is excluded. Result[ 0, 1, 2, 3, 4, 5]
print(a[0:6]) # this is same as above
print(a[5:]) # this includes elements from fifth index to the last. Result[5, 6, 7, 8, 9, 10]
print(a[1:8]) #this gives [1, 2, 3, 4, 5, 6, 7]
print(a[1:6:2]) # it jumps 1 step for elements from 1 to 7.


#Negative slicing
print(a[:-4]) # this gives elements from 0 index to -5th index
print(a[-5:]) #this gives from -5th index to the last element
print(a[-6:-2]) #this gives from -6th to -3rd index [5, 6, 7, 8]
print(a[-6:-8]) #this gives []

##list operations

#Concatination with + operator
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(a + b) #this concatenates two lists. Result [1, 2, 3, 4, 5, 6, 7, 8]

# Repetition with * operator (broadcast)
print(a*2) #It gives [1, 2, 3, 4, 1, 2, 3, 4]

# Membership Check
print(2 in a) # it gives True
print(5 not in b) #it gives false

# Methods are the function which are compulsarily called by an object

# Operation
# Methods
# Built-in functions

sum() # this id a function

# List Methods
a = [1, 2, 3]
a.append("hello")
print(a)  # this gives [1, 2, 3, "hello" )
result = a.append(4) # this statement appends value 4 to the list 'a' but it does not return anything ( i.e. None)
print(a) #[1, 2, 3, "Hello", 4]
print(result)  # this gives None

a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a) #result => [1, 2, 3, 4, 5, 6]
#extend() method also returns a None type

a.insert(1, "Hello world")
print(a) # result => [1, "Hello World", 2, 3]

a.remove(3) # this removes 3 from the list
print(a) #result => [1, "Hello World", 2]
# but if we pass the elements not present in the list to the remove method then it raises error.


















