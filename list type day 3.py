# List Method continue

# pop() method takes index as a parameter and removes the elements at the provided index
a = ["Hello", "from", "broadway", "i'm", "learning", "python"]
value = a.pop(2) # this pops the elements at 2nd index from the list and returns the variables
print(a)
print(value)
print(a.clear())
print(a.index(1))

a.clear()


a = [1, 2, 3, 4 , 1, 5, 3, 2]
a.index(2) # this gives the index of value 2 in the given list. in this case the index of 2 (at first occurance) is 1.

print(a.index(3, 3, 7)) #This 3gives 6 as 3 is searcheed in range 3rd to 6th position

 print(a.count(3))  # this gives 2 because 3 is repeated two times in the list

 a = ["hello", "from", "broadway"]
 a.reverse()
 print(a)




