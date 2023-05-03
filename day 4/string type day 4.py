# strings in python are of immutable type
# we can create an empty string using str built-in function or using  empty single or double quotes

example =>  "" #Empty string using double quotes
print(example)
example = ''  # Empty  string using single quotes
example = str() #Empty string
print(example)


example = "Hello World"   # its a valid string
#example = 'Hello World' # invalid string
# example = "Hello World' #invalid string


##Escape sequences
# Escape Sequence / Characters are the strings in python which suppresses the usual meaning os a character and gives
# a new meaning


example = 'I\'m learning Python   # Here \' is an escape character
print(example)


example = "path to my folder is c:\\Project\\Broadway"
print(example)

example = "Hello\nworld" #here \n is a new line escape character
print(example)


example = "Hello\tWorld"  # here \t is a
print(example)


example = "Hello\bWorld"






## Triple quoted strings
example = '''
Example 1 
'''
print(example) #example with triple single quotes


example = """
Example2
"""
print(example) #example with triple double quotes
example = """
I'm learning python
"""

print(example) # we dont need to use escape characters for single/double quote in


"""
Function to calculate difference, WE csn treat this as a multiples comment
"""
def fxn(a, b ):
return a-b





# indexing and slicing in string
# string indexing and slicing is similar to l;ost slicing and indexing



message = "Hello World"
print(message[3]) #this gives 'l'
print(message[6])  #this gives 'w'. space is also considered as a character
print(message[-2]) #negative indexing is also possible. it gives 'l'


print(message[1: 7])  #result => 'ello W'
print(message[1: 7: 2])  #result => 'el'
print(message[1: -3]) #result => 'ello Wo'
print(message[-7: -3])  #result => 'o Wo'
print(message[-3: -7])  #result => ''




#string doesn't support item assignment because it is immutable
message = "hello"
 # message[1] = "E" #This is not possible






