########################################
# PROJECT: Binary Min Heap and Sort
# Author:
########################################


class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []

    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        string = ''
        i = 0
        if self.get_size() == 0:
            return ''
        string += str(self.table[i])
        i += 1
        while i < self.get_size():
            string += ',' + str(self.table[i])
            i += 1
        return string

    def get_size(self):
        """
        Returns the number of nodes currently in the Heap
        :return:  The number of nodes in the heap's table table
        """
        return len(self.table)

    def parent(self, position):
        """
        Finds the parent of the node at index position
        :param position:  The position to find the parent of
        :return:  Index of the parent node
        """
        parnt = (position-1)//2
        if parnt >= 0:
            return parnt
        return -1

    def left_child(self, position):
        """
        Finds the left child of the node at index position
        :param position:  The position to look for the left child from
        :return:  The index of the left child
        """
        if self.has_left(position):
            return 2*position+1
        return -1

    def right_child(self, position):
        """
        Finds the right child of the node at index position
        :param position:  The position to look for the right child from
        :return:  The index of the right child
        """
        if self.has_right(position):
            return 2*position+2
        return -1

    def has_left(self, position):
        """
        Returns True if the node at index position has a left child, False otherwise
        :param position:  The position to look for the left child from
        :return:  True if there is a left child, false otherwise
        """
        if 2*position+1 < self.get_size():
            return True
        return False

    def has_right(self, position):
        """
        Returns True if the node at index position has a right child, False otherwise
        :param position:  The position to look for the right child from
        :return:  True if there is a right child, false otherwise
        """
        if 2*position+2 < self.get_size():
            return True
        return False

    def find(self, value):
        """
        Returns the index of the node with value
        Returns None if the value is not found in the heap
        :param value:  The value to search for
        :return:  The index of the value if found, None otherwise
        """
        indx = 0
        while indx < self.get_size():
            if self.table[indx] == value:
                return indx
            indx += 1
        return None

    def heap_push(self, value):
        """
        Adds a node with the given value and adds it to the heap
        Duplicates are ignored
        :param value:  The value to be added to the heap
        :return:  None
        """
        indx = self.find(value)
        if indx is not None:
            return
        self.table.append(value)
        self.percolate_up(self.get_size()-1)

    def heap_pop(self, value):
        """
        Removes the node with the given value
        :param value:  The value of the node to be removed
        :return:  The value of the removed node, None othewise
        """
        indx = self.find(value)
        if indx is None:
            return None
        node = self.table[indx]
        self.swap(indx, self.get_size()-1)
        self.table.pop()
        self.percolate_down(indx)
        return node

    def pop_min(self):
        """
        Removes the min node in the heap
        Returns the value it removed, or None
        :return:  The value of the removed node, None othewise
        """
        if self.get_size() == 0:
            return None
        self.swap(0, self.get_size()-1)
        node = self.table.pop()
        self.percolate_down(0)
        return node

    def swap(self, p1, p2):
        """
        Swaps the elements at indices p1 and p2
        :param p1:  The index of the first value
        :param p2:  The index of the second value
        :return:  None
        """
        temp = self.table[p1]
        self.table[p1] = self.table[p2]
        self.table[p2] = temp

    def percolate_up(self, position):
        """
        Moves node at index position up the tree until it is in the proper place
        :param position:  The starting position for percolating up
        :return:  None
        """
        parent = self.parent(position)
        if self.parent(position) < 0:
            return
        if self.table[parent] > self.table[position]:
            self.swap(position, parent)
            self.percolate_up(parent)
        return

    def percolate_down(self, position):
        """
        Moves node at index position down the tree until it is in the proper place
        :param position:  The starting position for percolating down
        :return:  None
        """
        if not self.has_left(position) and not self.has_right(position):
            return
        left = self.left_child(position)
        right = self.right_child(position)
        if self.table[left] < self.table[position]:
            if self.table[left] < self.table[right]:
                self.swap(left, position)
                self.percolate_down(left)
        if self.table[right] < self.table[position]:
            if self.table[right] < self.table[left]:
                self.swap(right, position)
                self.percolate_down(right)


def max_heap(tab, sz):
    """
    Takes in a list to turn into a max_heap and an ending point, sz
    :param tab: The list to be turned into a max heap
    :param sz: The last element to be included in the max heap
    :return: a heap in the form of a max heap
    """
    i = sz // 2 - 1
    j = sz
    heap = BinaryMinHeap()
    heap.table = tab
    while j > 0:
        left = heap.left_child(i)
        right = heap.right_child(i)
        if heap.table[i] < heap.table[left] or heap.table[i] < heap.table[right]:
            if heap.table[left] > heap.table[right] or right < 0:
                heap.swap(i, 2 * i + 1)
            elif heap.table[right] > heap.table[left] or left < 0:
                heap.swap(i, 2 * i + 2)
        j -= 1
        if i == 0:
            i = sz // 2 - 1
        else:
            i -= 1
    return heap


def heap_sort(unsorted):
    """
    Given an unsorted list, performs Heap Sort
    Returns the sorted list
    :param unsorted:  The list to be sorted
    :return:  The sorted list
    """
    heap = max_heap(unsorted, len(unsorted))
    j = len(unsorted)-1
    while j > 0:
        if j == 1:
            if heap.table[0] < heap.table[j]:
                break
        heap.swap(0, j)
        heap = max_heap(heap.table, j-1)
        j -= 1
    return heap.table
