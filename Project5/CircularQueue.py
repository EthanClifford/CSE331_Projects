class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """
        Converts the queue into a string then prints it
        :return: None
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        j = 0
        i = 0
        while i < self.capacity:
            output.append(str(self.data[j]))
            j += 1
            if j >= len(self.data):
                j = 0
            i += 1
        return "{} Capacity: {}".format(output, str(self.capacity))

    def is_empty(self):
        """
        Checks if the queue is empty
        :return: Returns true if the list is empty, false otherwise
        """
        return self.size == 0

    def __len__(self):
        """
        Returns the amount of values in the queue
        :return: count of values in the queue
        """
        return self.size

    def first_value(self):
        """
        Returns the first value in the queue
        :return: The value at the head of the data
        """
        return self.data[self.head]

    def enqueue(self, val):
        """
        Adds val to the end of the queue.  If the queue with the new element
        exceeds the capacity, call grow()
        :param val: The value to be added
        :return: None
        """
        if self.size+1 >= self.capacity:
            self.grow()
        if self.tail >= len(self.data):
            self.tail = 0
        self.data[self.tail] = val
        self.tail += 1
        self.size += 1

    def dequeue(self):
        """
        Checks if the queue is empty.  If not, removes the first
        element in the queue and returns its value.  If the size of
        the queue is less than 1/4 of the capacity with the head removed, call shrink()
        :return: The value of the head of the queue
        """
        head = self.data[self.head]
        if self.is_empty():
            return None
        self.data[self.head] = None
        self.head += 1
        self.size -= 1
        if self.head >= len(self.data):
            self.head = 0
        if self.size <= self.capacity/4:
            self.shrink()
        return head

    def grow(self):
        """
        Creates a new queue with double the capacity, copy all
        values to the new queue, then assign all values from the new queue to self
        :return: None
        """
        q1 = CircularQueue(self.capacity*2)
        i = 0
        sz = self.size
        while i < sz:
            q1.enqueue(self.dequeue())
            i += 1
        self.data = q1.data
        self.tail = q1.tail
        self.head = 0
        self.capacity = q1.capacity
        self.size = q1.size

    def shrink(self):
        """
        Makes sure that the capacity/2 is greater than 4,
        and if so, it copies all values from self to a new
        queue with half the capacity then assigns all values
        from that new queue to self again.
        :return: None
        """
        if self.capacity/2 >= 4:
            q1 = CircularQueue(self.capacity // 2)
            i = self.head
            sz = self.size
            while i < self.head+sz:
                q1.enqueue(self.data[i])
                i += 1
            self.data = q1.data
            self.tail = q1.tail
            self.head = 0
            self.capacity = q1.capacity
            self.size = q1.size
