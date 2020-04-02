"""
PROJECT 2 - Recursion
Name:
PID:
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """
    Takes a value and a Node and insert them into the list while keeping the nodes sorted in increasing order
    :param value: The value to be placed into the new node
    :param node: The first node of the list
    :return: The first node
    """
    if node is None:
        node1 = LinkedNode(value, None)
        return node1
    if node.value > value:
        node1 = LinkedNode(value, node)
        return node1
    if node.next_node is None:
        node1 = LinkedNode(value, None)
        node.next_node = node1
    elif node.next_node.value >= value:
        node1 = LinkedNode(value, node.next_node)
        node.next_node = node1
    else:
        insert(value, node.next_node)
    return node


def string(node):
    """
    Takes a starting node and returns the list as a string value
    :param node: The starting node in the list
    :return: A string form of the list
    """
    string_rep = ""
    if node is None:
        return string_rep
    else:
        if node.next_node is not None:
            string_rep = str(node.value) + ", " + string(node.next_node)
        else:
            string_rep = str(node.value)
        return string_rep


def reversed_string(node):
    """
    Takes a starting node and returns the list as a string in the reversed order from how it occurs in the list
    :param node: The starting node in the list
    :return: A string form of the list
    """
    string_rep = ""
    if node is None:
        return string_rep
    if node.next_node is None:
        string_rep = str(node.value)
    else:
        string_rep = reversed_string(node.next_node) + ", " + str(node.value)
    return string_rep


def remove(value, node):
    """
    Takes a starting node and the value to be removed and removes the first occurrence of the value in the list
    :param value: The value to be removed
    :param node: The starting node
    :return: The first node
    """
    counter = 0
    if node is None:
        return node
    else:
        if node.next_node is None:
            if node.value == value:
                node = node.next_node
                return None
            return node
        if node.value == value:
            node = node.next_node
            return node
        if node.next_node.value == value:
            node.next_node = node.next_node.next_node
            counter = counter+1
        if counter == 0:
            remove(value, node.next_node)
        return node


def remove_all(value, node):
    """
    Removes all instances of the value in the list starting with node
    :param value: The value to be removed
    :param node: The starting node
    :return: The first node
    """
    if node is None:
        return node
    else:
        if node.next_node is None:
            if node.value == value:
                node = node.next_node
                return None
            return node
        if node.value == value:
            node = node.next_node
            remove_all(value, node)
        if node.next_node.value == value:
            node.next_node = node.next_node.next_node
            remove_all(value, node)
        else:
            remove_all(value, node.next_node)
        return node


def search(value, node):
    """
    Searches the list starting at node for a node that has the value of value and returns true if it is found and false
    otherwise
    :param value: The value to be found
    :param node: The starting node
    :return: True if the value is found, False otherwise
    """
    if node is None:
        return False
    if node.value == value:
        return True
    elif node.next_node is None:
        return False
    else:
        return search(value, node.next_node)


def length(node):
    """
    Determines the number of nodes in the list starting at node
    :param node: The starting node
    :return: The length of the list
    """
    if node is None:
        return 0
    if node.next_node is None:
        return 1
    return 1 + length(node.next_node)


def sum_all(node):
    """
    Sums all of the values of the nodes in the list starting at node
    :param node: The starting node
    :return: The sum of all the values
    """
    if node is None:
        return 0
    if node.next_node is None:
        return node.value
    return node.value + sum_all(node.next_node)


def count(value, node):
    """
    Determines the number of times a value occurs in the list beginning with node
    :param value: The value to be found and counted
    :param node: The starting node
    :return: The total count of the number of times the value occurs
    """
    if node is None:
        return 0
    if node.next_node is None:
        if node.value == value:
            return 1
        else:
            return 0
    else:
        if node.value == value:
            return 1 + count(value, node.next_node)
        else:
            return count(value, node.next_node)
