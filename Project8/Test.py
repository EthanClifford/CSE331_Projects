from Project8.BinaryMinHeap import BinaryMinHeap as bh
from Project8.BinaryMinHeap import heap_sort as hs

heap = bh()

heap.heap_push(4)
heap.heap_push(3)
heap.heap_push(2)
heap.heap_push(7)
heap.heap_push(1)
heap.heap_push(5)
heap.heap_push(6)

print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)
print(heap.pop_min())
print(heap)

#print(heap.get_size()) #5
#print(heap.parent(4)) #1
#print(heap.left_child(0)) #1
#print(heap.right_child(0)) #2
#print(heap.has_left(2)) #False
#print(heap.has_right(0)) #True