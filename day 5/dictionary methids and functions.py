student = {"name":"jon", "age":23}
print(all(student)) #Returns true if all the values in the iterable are Truthy. Here result => True

print(all([])) #this is an exception because it gives True . this is like 'and' operation


print(any(student)) #this gives True. any() returns True if any of the elements in an iterable is truthy.
#this is like 'or' operation
print(any([])) #False


result = sorted(student)  #It sorts the keys of the dictionary and returns a list
print(result)  #["age", "name"]



#Dictionary methods continue
student = {"name":"jon", "age":23}
print(student.item()) #It gives list like object [("name", "jon"), ("age", 23)

print(student.keys()) #it gives list like object of dictionary Keys. result => ["name", "age"]

print(student.values()) #it gives list like object of dictionary values. Result => ["jon", 23]

d = student.fromkeys([1, 2 , 3], "Hello")
print(d) #gives a new dictionary with keys of iterable with common value
#Result => {1: "Hello", 2: "Hello", 3:"Hello"}

d = student.fromkeys([1, 2 , 3]
print(d) #{1: None, 2: None, 3: None}


