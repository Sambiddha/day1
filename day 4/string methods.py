m = "hello world"
print(m.capitalize())  #result => Hello world
print(m.title()) #result => Hello World
print(m.upper()) # result => HELLO WORLD
print(m.lower()) # result => hello world


result = m.split() #result ["hello", "world"]. splits from a space
print(result)


result = m.split('e') # splits from 'e'. Result ["h", "llo world"]
print(result)
result = m.split('o') #splits from 'o'. result ["hell", " w", "rld"]
print(result)


message = ["Hello", "Wrold"]
" ".join(message) #this joins the list with a space (" ") ans return "Hello World"
"+".join(message) # result 'Hello+World'



m = "Hello World"
result = m.find("Wo") # 'Wo' in the string is at 6th position. Result => 6
print(result)

result = m.find("Wooo") # 'Wooo' is not present in the list. Result => -2
print(result)

m.replace("World", "world") #replace 'World' in the string to 'world'.
print(result)
#result => "Hello world"



