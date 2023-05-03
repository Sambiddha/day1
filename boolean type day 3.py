# True and False are the keyboards for boolean type in python
# Logical operations, relational operations, identity and membership operations returns boolean result


a = 1
b = 2
c = 0

# Logical operations
print(bool(a) and bool(b)) #this gives true
print(bool(a) and bool(c)) #this gives false
print(bool(a) or bool(c)) # this gives true

# relational operations
print(a > b) #false
print(b > a) #true
print(a == b) #false
print(a != b) #true


#identity ooperations
a = 1
b = 1
c = 2
print(a is b) #true
print(a is c) #false


#Membership operation
print(2 in [ 1, 2, 3]) #true
print(3 not in [1, 2, 3]) #false
print("h" in "hello") #true

# boolean is a subclass of integer type in python.Thus, True represents integer 1 and False represents 0.
# Arithmetic operations is possible for the boolean type

print(True + 1) #result => 2 (1+1)
print(False + 5)  #result => 5 (0+5)
print(False * 70) #result => 0 (0*70)



#bool() built-in function
#bool() function can take any object as a parameter and returns True or False based on the truthy of falsy nature of the object.

# Any no-empty strings, tuple, dictionary, set are truthy in nature. ALso, all integers are truthy in nature
#except 0
print(bool("hello")) #true
print(bool([1, 2, 3])) #true
print(bool({"name" : "jon"})) #true
print(bool({1, 2, 3})) #true
print(bool(5)) #true
print(bool(-5)) #true

# All empty list, dictionary, set, string (or any empty object) are falsy in nature. 0 and none are also falsy
# in nature
print(bool(None)) #false
print(bool(0)) #false
print(bool("")) #false
print(bool([])) #false
print(bool({})) #false
print(bool(False)) #false


