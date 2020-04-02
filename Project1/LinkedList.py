########################################
# PROJECT 1 - Linked List
# Author:
# PID:
########################################


class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'next_node'

    def __init__(self, value, next_node=None):
        """
        DO NOT EDIT
        Initialize a node
        :param value: value of the node
        :param next_node: pointer to the next node, default is None
        """
        self.value = value  # element at the node
        self.next_node = next_node  # reference to next node

    def __eq__(self, other):
        """
        DO NOT EDIT
        Determine if two nodes are equal (same value)
        :param other: node to compare to
        :return: True if nodes are equal, False otherwise
        """
        if other is None:
            return False
        if self.value == other.value:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a node
        :return: string of value
        """
        return str(self.value)


class LinkedList:
    def __init__(self):
        """
        DO NOT EDIT
        Create/initialize an empty linked list
        """
        self.head = None   # Node
        self.tail = None   # Node
        self.size = 0      # Integer

    def __eq__(self, other):
        """
        DO NOT EDIT
        Defines "==" (equality) for two linked lists
        :param other: Linked list to compare to
        :return: True if equal, False otherwise
        """
        if self.size != other.size:
            return False
        if self.head != other.head or self.tail != other.tail:
            return False

        # Traverse through linked list and make sure all nodes are equal
        temp_self = self.head
        temp_other = other.head
        while temp_self is not None:
            if temp_self == temp_other:
                temp_self = temp_self.next_node
                temp_other = temp_other.next_node
            else:
                return False
        # Make sure other is not longer than self
        if temp_self is None and temp_other is None:
            return True
        return False

    def __repr__(self):
        """
        DO NOT EDIT
        String representation of a linked list
        :return: string of list of values
        """
        temp_node = self.head
        values = []
        if temp_node is None:
            return None
        while temp_node is not None:
            values.append(temp_node.value)
            temp_node = temp_node.next_node
        return str(values)

    ###### MODIFY THE BELOW FUNCTIONS #####

    # ------------------------Accessor Functions---------------------------

    def length(self):
        """
        Gets the number of nodes of the linked list
        :return: size of list
        """
        return self.size

    def is_empty(self):
        """
        Determines if the linked list is empty
        :return: True if list is empty and False if not empty
        """
        if self.size == 0:
            return True
        return False

    def front_value(self):
        """
        Gets the first value of the list
        :return: value of the list head
        """
        if self.size == 0:
            return None
        return self.head.value

    def back_value(self):
        """
        Gets the last value of the list
        :return: value of the list tail
        """
        if self.size == 0:
            return None
        return self.tail.value

    def count(self, val):
        """
        Counts the number of times a value 'val' occurs in the list
        :param val: value to find and count
        :return: number of time 'val' occurs
        """
        if self.size == 0:
            return 0
        if self.size == 1:
            if self.head.value == val:
                return 1
            return 0
        count = 0
        index = self.head
        while index is not None:
            if index.value == val:
                count = count+1
            index = index.next_node
        #if self.tail.value == val:
            #count = count+1
        return count

    def find(self, val):
        """
        Searches for and returns the first node with the value 'val'
        :param val: value to search for
        :return: True if value is in list, False if value is not found
        """
        if self.size == 0:
            return False
        if self.size == 1:
            if self.head.value == val:
                return True
            return False
        index = self.head
        while index is not None:
            if index.value == val:
                return True
            index = index.next_node
        return False

    # ------------------------Mutator Functions---------------------------

    def push_front(self, val):
        """
        Adds a node to the front of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        new_node = Node(val, self.head)
        self.head = new_node
        self.size = self.size+1
        if self.size == 1:
            self.tail = new_node

    def push_back(self, val):
        """
        Adds a node to the back of the list with value 'val'
        :param val: value to add to list
        :return: no return
        """
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif self.size == 1:
            self.head.next_node = new_node
            self.tail = new_node
        else:
            #node1 = Node(self.tail.value)
            #index = self.head
            self.tail.next_node=new_node
            self.tail = new_node
        """
            while index != self.tail:
                if index.next_node == self.tail:
                    index.next_node = node1
                    self.tail = new_node
                    node1.next_node = new_node
                    break
                index = index.next_node
                """
        self.size = self.size + 1

    def pop_front(self):
        """
        Removes a node from the front of the list
        :return: the value of the removed node
        """
        if self.size == 0:
            return None
        val = self.head.value
        self.head = self.head.next_node
        self.size = self.size - 1
        return val

    def pop_back(self):
        """
        Removes a node from the back of the list
        :return: the value of the removed node
        """
        if self.size == 0:
            return None
        val = self.tail.value
        index = self.head
        while index != self.tail:
            if index.next_node == self.tail:
                index.next_node = None
                self.tail = index
                break
            index = index.next_node
        self.size = self.size - 1
        return val

    def reverse_list(self):
        """
        Reverses the values of the given linked list
        :return: no return
        """

        linked = LinkedList()
        index = self.head
        while index is not None:
            linked.push_front(index.value)
            self.pop_front()
            index = index.next_node
        index = linked.head
        while index is not None:
            self.push_back(index.value)
            index = index.next_node




        """
        initial_node = self.head
        val_i = initial_node.value
        end_node = self.tail
        val_e = end_node.value
        index = self.head
        while index is not None:
            if index.next_node == end_node:
                initial_node.value = val_e
                end_node.value = val_i
                end_node = index
                initial_node = initial_node.next_node
                index = initial_node
                val_i = initial_node.value
                val_e = end_node.value
            index = index.next_node
        #if index.next_node == self.tail:
        """