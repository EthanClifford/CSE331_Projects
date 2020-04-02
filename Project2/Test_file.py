import Project2.Recursion as r
from Project2.LinkedNode import LinkedNode

linked_node = LinkedNode(None, None)
#str = r.string(linked_node)
#print("String:", str)
#linked_node = r.remove_all(4, linked_node)
#print("REMOVE ALL 4:", r.string(linked_node))
#print("SEARCH 5:", r.search(5, linked_node))
#print("LENGTH INIT:", r.length(None))
#print("SUM:", r.sum_all(None))
#print("COUNT 5:", r.count(5, None))
rev_str = r.reversed_string(None)
print(rev_str)

linked_node = r.insert(2)

#print("COUNT 2:", r.count(2, linked_node))
#print("SUM:", r.sum_all(linked_node))
#print("LENGTH 1:", r.length(linked_node))
#print("SEARCH 2:", r.search(2, linked_node))
#linked_node = r.remove_all(2, linked_node)
#print("REMOVE ALL 2:", r.string(linked_node))
#str = r.string(linked_node)
#print("String:", str)
rev_str = r.reversed_string(linked_node)
print(rev_str)

linked_node = r.insert(1, linked_node)
linked_node = r.insert(4, linked_node)
linked_node = r.insert(4, linked_node)
linked_node = r.insert(3, linked_node)
linked_node = r.insert(3, linked_node)
str = r.string(linked_node)
print("String:", str)
rev_str = r.reversed_string(linked_node)
print("Reversed String:", rev_str)

#linked_node = r.remove(4, linked_node)
#print("REMOVE 4:", r.string(linked_node))
#linked_node = r.remove(3, linked_node)
#print("REMOVE 3:", r.string(linked_node))

#linked_node = r.remove_all(3, linked_node)
#print("REMOVE ALL 3:", r.string(linked_node))

#print("SEARCH 4:", r.search(4, linked_node))
#print("SEARCH 5:", r.search(5, linked_node))

#print("LENGTH END:", r.length(linked_node))

#print("SUM:", r.sum_all(linked_node))

#print("COUNT 4:", r.count(4, linked_node))


#node = linked_node
#while node is not None:
    #print(node.value)
    #node = node.next_node