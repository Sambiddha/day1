# Dictionary type is the key-value pair data type

# Empty dictionary can be created using curly braces{} or dict() built-in function

student = dict() #this is an empty dictionary
print(student)
student = {}  #this is also an empty dictionary
print(student)

student = {"name": "jon", "age": 45, "department":"CS"}  #Non-empty dictionary
print(student)
student = dict(name="jon", age=45, department="CS")  #Non-empty dictionary
print(student)


student = dict([
    ("name", "jon"),
    ("age", 43),
    ("department", "CS"),

])
print(student)  #This is also a dictionary






#Accessing values in dictionary
student = {"name": "jon", "age": 45, "department":"CS"}
name = student['name']
print(name) #Result => jon
print(student['department'])  #Result => CS
print(student["roll number"])  #this raises keyError because 'roll-number is not a key of dictionary student

# We can also access the dictionary values using get() method
name = student.get('name')
print(name)

roll_number = student.get('roll_number')
print(roll_number)  #this gives none. if the key not present in the dictionary is provided to the get() method
# then it returns None

# We can also provide a default value to the get() method
roll = student.get("roll_number", 4)  #here 4 is a default value
print(roll)  #this gives 4


name = student.get("name", "jane")  #Here jane is a default value
print(name)  #Result => Jon


#Adding and operating dictionary
student = {"name": "jon", "age": 45, "department":"CS"}
student["roll"] = 4
print(student)  #Result => student = {"name": "jon", "age": 45, "department":"CS", "roll": 4}

# If the key is already present in the dictionary then it gets updated
student['name'] = "jane"
#Result => student = {"name": "jon", "age": 45, "department":"CS", "roll": 4}

#Updating dictionary using update method
student = {"name": "jon", "age": 45,}
student.update({"department":"CS", "roll": 4})
print(student)
#Result => {"name": "jon", "age": 45, "department":"CS", "roll": 4}

student.update(id=1, height=5.8)
print(student)
#Result => {"name": "jon", "age": 45, "department":"CS", "roll": 4, "id": 1, "height": 5.8}


#Deleting or removing dictionary key-values
student = {"name": "jon",
           "age": 45,
           "department":"CS",
           "roll": 4,
           "id": 1,
           "height": 5.8
           }
roll = student.pop("roll")
print(student) #roll key is removed from the dictionary
print(roll) #result => 4

# Rules for dictionary keys and values
# 1. Dictionary keys must be immutable
# 2. Dictionary values can be of any data-type
# 3. A tuple can also be a dictionary key because it is immutable type. but, if it contains mutable type, then
# it can't be used


#Membership operation in dictionary

student = {"name":"jon", "age":23}
print("age" in student) #True. Membership is checked in keys in a dictionary
print("department" in student) #false

