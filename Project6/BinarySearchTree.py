class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Takes in a value to be added to the tree as a node
        Adds the node to the tree
        Do nothing if the value is already in the tree
        :param value: The value to be added
        :return: No value is returned
        """
        if self.size == 0:
            self.root = Node(value)
            self.size += 1
        else:
            prnt = self.search(value, self.root)
            if prnt.value == value:
                return
            nd = Node(value, prnt)
            self.size += 1
            if value <= prnt.value:
                prnt.left = nd
            else:
                prnt.right = nd

    def remove(self, value):
        """
        Takes in a key to remove from the tree
        Do nothing if the key is not found
        When removing a node with two children, replace with the minimum of the right subtree
        :param value:  The value of the node to be removed
        :return:  No value is returned
        """
        removed_one = False
        if self.size == 1:
            if self.root.value == value:
                self.root = None
                removed_one = True
        elif self.size == 0:
            return
        else:
            removed_one = True
            nd = self.search(value, self.root)
            if nd.value != value:
                return
            if nd == self.root:
                if nd.left is not None and nd.right is None:
                    self.root = nd.left
                    self.root.parent = None
                elif nd.right is not None and nd.left is None:
                    self.root = nd.right
                    self.root.parent = None
                else:
                    newnd = self.min(nd.right)
                    val = newnd.value
                    self.remove(newnd.value)
                    removed_one = False
                    self.root.value = val
                    self.root.parent = None
            else:
                ndprnt = nd.parent
                leftnd = ndprnt.left
                rightnd = ndprnt.right
                left = False
                right = False
                if leftnd == nd:
                    left = True
                if rightnd == nd:
                    right = True
                if nd.left is None and nd.right is None:
                    if left is True:
                        ndprnt.left = None
                    if right is True:
                        ndprnt.right = None
                elif nd.left is not None and nd.right is None:
                    if left is True:
                        ndprnt.left = nd.left
                        nd.left.parent = ndprnt
                    if right is True:
                        ndprnt.right = nd.left
                        nd.left.parent = ndprnt
                elif nd.left is None and nd.right is not None:
                    if left is True:
                        ndprnt.left = nd.right
                        nd.right.parent = ndprnt
                    if right is True:
                        ndprnt.right = nd.right
                        nd.right.parent = ndprnt
                else:
                    newnd = self.min(nd.right)
                    val = newnd.value
                    self.remove(newnd.value)
                    removed_one = False
                    if left is True:
                        ndprnt.left.value = val
                    if right is True:
                        ndprnt.right.value = val
        if removed_one is True:
            self.size -= 1

    def search(self, value, node):
        """
        Takes in a value to search for and a node which is the root of a given tree or subtree
        Returns the node with the given key if found, else returns the potential parent node
        :param value:  The value of the node to be found
        :param node:  The starting node
        :return:  The node that has the given value, or the potential parent of that node
        """
        if node is None:
            return node
        if self.size == 1:
            return self.root
        nd = node
        if value < node.value:
            if node.left is not None:
                nd = self.search(value, node.left)
        elif value > node.value:
            if node.right is not None:
                nd = self.search(value, node.right)
        return nd

    def inorder(self, node):
        """
        Returns a generator object of the tree traversed using the
        inorder method of traversal starting at the given node
        :param node:  The node to start the traversal at
        :return: yields the node being visited
        """
        if self.size == 0:
            yield None
        else:
            if node.left is not None:
                for other in self.inorder(node.left):
                    yield other
            yield node.value
            if node.right is not None:
                for other in self.inorder(node.right):
                    yield other

    def preorder(self, node):
        """
        Returns a generator object of the tree traversed using the
        preorder method of traversal starting at the given node
        :param node:  The node to start the traversal at
        :return: yields the node being visited
        """
        if self.size == 0:
            yield None
        else:
            yield node.value
            if node.left is not None:
                for other in self.preorder(node.left):
                    yield other
            if node.right is not None:
                for other in self.preorder(node.right):
                    yield other

    def postorder(self, node):
        """
        Returns a generator object of the tree traversed using the
        postorder method of traversal starting at the given node
        :param node:  The node to start the traversal at
        :return: yields the node being visited
        """
        if self.size == 0:
            yield None
        else:
            if node.left is not None:
                for other in self.postorder(node.left):
                    yield other
            if node.right is not None:
                for other in self.postorder(node.right):
                    yield other
            yield node.value

    def depth(self, value):
        """
        Returns the depth of the node with the given value
        :param value:  The value of the node whose depth is being calculated
        :return:  The depth as an int
        """
        nd = self.root
        if nd is None:
            return -1
        if self.size == 1:
            return 0
        dpth = 0
        while nd.value != value:
            if nd.value > value:
                dpth += 1
                nd = nd.left
            elif nd.value < value:
                dpth += 1
                nd = nd.right
            if nd is None:
                return -1
        return dpth

    def height(self, node):
        """
        Returns the height of the tree rooted at the given node
        :param node:  The node to start calculating the height from
        :return:  The height as an int
        """
        heightl = 0
        heightr = 0
        if node is None:
            return -1
        if (node.left is None) and (node.right is None):
            return 0
        elif node.right is None:
            heightl = self.height(node.left)+1
        elif node.left is None:
            heightr = self.height(node.right) + 1
        else:
            heightl = self.height(node.left)+1
            heightr = self.height(node.right)+1
        if heightl >= heightr:
            return heightl
        else:
            return heightr

    def min(self, node):
        """
        Returns the node with the minimum of the tree rooted at the given node
        :param node:  The node to start the search for the minimum value node from
        :return: The node with the smallest value
        """
        if node is None:
            return node
        if node.left is None:
            return node
        min = self.min(node.left)
        return min

    def max(self, node):
        """
        Returns the node with the maximum of the tree rooted at the given node
        :param node:  The node to start the search for the maximum value node from
        :return: The node with the largest value
        """
        if node is None:
            return node
        if node.right is None:
            return node
        max = self.max(node.right)
        return max

    def get_size(self):
        """
        Returns the size of the tree
        :return: The number of nodes in the tree
        """
        return self.size

    def is_perfect(self, node):
        """
        Returns a Boolean of whether or not the BST rooted at the given node is perfect
        :param node: The root node of the tree in question
        :return: True if the tree is perfect, false otherwise
        """
        if self.size <= 1:
            return True
        perfect_sz = (2**(self.height(node)+1))-1
        if perfect_sz == self.size:
            return True
        return False

    def is_degenerate(self):
        """
        Returns a Boolean of whether or not the BST is degenerate
        :return: True if the tree is degenerate, false otherwise
        """
        if self.size > 1:
            if self.root.left is None or self.root.right is None:
                return True
        return False
