s1 = {1, 2, 3 , 4, 5}
s2 = {4, 5, 6, 7, 8}

s = s1.union(s2) #It guves union of two sets
print(s)
s = s1.intersection(s2) #it guves intersection of two sets
print(s)


s1.isdisjoint(s2) # s1 and s2 are not a disjoint set as they have common elements {4, 5}. so, it gives false

s1.symmetric_difference(s2)
print(s)
#this is a complement of s1 intersection s2
# Result {1, 2, 3, 6 , 7, 8}

s1.symmetric_difference_update(s2)
print(s1)
#This updates the symmetric difference of s1 and s2 to s1.

s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 4}
print(s2.issubset(s1)) #true
print(s1.issuperset(s2)) #true
print(s1.issuperset(s1)) #false


#Bitwise operators in set operations
s = s1 | s2 #Union => Same as s1.union(s2)
print(s)
s = s1 & s1 #Intersection => Same as s1.intersection(s2)
print(s)
s = s1 - s2  #Difference
print(s)
s = s1 ^ s2  #symmetric difference
print(s)

