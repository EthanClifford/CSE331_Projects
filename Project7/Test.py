from Project7.HashTable import HashTable
from Project7.HashTable import string_difference

ht = HashTable()

ht.insert("abc", 1)
ht.insert("acb", 2)
ht.insert("bac", 3)

#print(ht.size)  #3
#print(ht.capacity)  #4

for i in range(ht.capacity):
    print(ht.table[i])

print(ht.quadratic_probe("abc"))  #6
print(ht.quadratic_probe("4"))  #4
print(ht.quadratic_probe(""))  #2
print(ht.quadratic_probe("c"))  #3
print(ht.quadratic_probe("acb"))  #2



s2 = "red"
s1 = "blue"

result = string_difference(s1, s2)
#expected = set(['r','d','b','l','u'])

print(result)

s2 = "green"
s1 = "white"

result = string_difference(s1, s2)
#expected = set(['g','r','e','n','h','i','w','t'])

print(result)

s2 = "blue"
s1 = "blue"

result = string_difference(s1, s2)
#expected = set()

print(result)

s2 = "aabbcc"
s1 = "ab"

result = string_difference(s1, s2)
#expected = set()

print(result)

s2 = " "
s1 = ""

result = string_difference(s1, s2)
#expected = set(['r','d','b','l','u'])

print(result)

string = " "
print(len(string))