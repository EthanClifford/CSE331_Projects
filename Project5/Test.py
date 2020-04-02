from Project5.CircularQueue import CircularQueue as cq

queue = cq(8)

for i in range(7):
    queue.enqueue(i)

for i in range(3):
    queue.dequeue()
for i in range(3):
    queue.enqueue(i)
for i in range(3):
    queue.dequeue()
for i in range(3):
    queue.dequeue()

print(str(queue))
print(queue.first_value())
print(queue.capacity)