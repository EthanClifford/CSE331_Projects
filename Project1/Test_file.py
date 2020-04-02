from Project1.LinkedList import LinkedList


def main():
    # Initialize linked list
    linkl = LinkedList()

    # Add nodes
    linkl.push_back(47)
    linkl.push_back(47)
    linkl.push_front(39)
    linkl.push_front(39)
    linkl.push_back(39)
    linkl.push_back(21)
    linkl.push_front(58)
    linkl.push_back(32)
    linkl.push_front(94)
    linkl.push_back(16)
    linkl.push_front(77)
    linkl.push_back(56)
    linkl.push_front(21)
    linkl.push_back(4)
    linkl.push_back(4)
    linkl.push_front(79)
    print(linkl==linkl)


    # Print results
    print("OUTPUT")
    print("Linked List: ", linkl)
    print("Count of 21: ", linkl.count(21))
    print("Count of 94: ", linkl.count(94))
    print("Count of 4: ", linkl.count(4))
    print("Found 21: ", linkl.find(21))
    print("Found 43: ", linkl.find(43))
    linkl.reverse_list()
    print("Reverse: ", linkl)


main()