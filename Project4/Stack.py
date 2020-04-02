"""
# Project 4
# Name:
# PID:
"""


class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """
        returns the stack size
        :return: size of stack
        """
        return self.size

    def is_empty(self):
        """
        returns true if the list is empty, false otherwise
        :return: true if the list is empty, false otherwise
        """
        if self.size == 0:
            return True
        return False

    def top(self):
        """
        returns the top value of the stack
        :return: top value of the stack
        """
        if self.is_empty():
            return self.data[0]
        return self.data[self.size-1]

    def push(self, val):
        """
        adds val to the top of the stack
        :param val: The value to be added to the stack
        :return: None
        """
        if self.is_empty():
            self.data[0] = val
        else:
            if self.size == self.capacity:
                self.grow()
            self.data[self.size] = val
        self.size += 1

    def pop(self):
        """
        removes and returns the value at the top of the stack
        :return: the value at the top of the stack
        """
        if self.is_empty():
            return None
        self.size -= 1
        temp = self.data[self.size]
        self.data[self.size] = None
        if self.size == self.capacity//2:
            self.shrink()
        return temp

    def grow(self):
        """
        doubles the size of the stack
        :return: None
        """
        stack1 = Stack(self.capacity*2)
        index = 0
        while index < self.size:
            stack1.push(self.data[index])
            index += 1
        self.data = stack1.data
        self.capacity = stack1.capacity

    def shrink(self):
        """
        Divides the size of the stack by 2
        :return: None
        """
        if (self.size <= self.capacity//2) and self.capacity//2 >= 2:
            stack1 = Stack(self.capacity//2)
            index = 0
            while index < self.size:
                stack1.push(self.data[index])
                index += 1
            self.data = stack1.data
            self.capacity = stack1.capacity


def reverse(stack):
    """
    reverses the order of the stack
    :param stack: the stack to be reversed
    :return: the reversed stack
    """
    if stack.is_empty() or stack.size == 1:
        return stack
    stack1 = Stack()
    i = 0
    size = stack.size
    while i < size:
        stack1.push(stack.pop())
        i += 1
    return stack1


def replace(stack, old, new):
    """
    searches through stack to find old, and if old is found, it is replaced by new
    :param stack: the stack to be looked through
    :param old: the value to be replaced by new
    :param new: the value to be placed into the list instead of old
    :return: the new stack
    """
    i = 0
    while i < stack.size:
        if stack.data[i] == old:
            stack.data[i] = new
        i += 1
    return stack
