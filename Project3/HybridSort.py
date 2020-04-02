def merge_sort(unsorted, threshold, reverse):
    """
    Takes an unsorted list, a threshold, below which
    insertion sort is used instead of merge sort,
    and a boolean reverse, which determines if the
    list is sorted in increasing or decreasing order.
    This part splits the list into progressively
    smaller parts then calls merge to put it all back together
    :param unsorted: The list to be sorted
    :param threshold: The threshold length of unsorted below which insertion sort should be used
    :param reverse: A boolean to determine if the list should be sorted in increasing (False)
                    or decreasing (True) order
    :return: The newly sorted list
    """
    length = len(unsorted)
    if length < 2:
        return unsorted
    elif length < threshold:
        return insertion_sort(unsorted, reverse)
    else:
        mid = length//2
        list1 = unsorted[0:mid]
        list2 = unsorted[mid:length]
        list1 = merge_sort(list1, threshold, reverse)
        list2 = merge_sort(list2, threshold, reverse)
        unsorted = merge(list1, list2, reverse)
        return unsorted


def merge(first, second, reverse):
    """
    Merges two lists, first and second, in either increasing or decreasing order,
    depending on reverse
    :param first: The first list to be merged
    :param second: The second list to be merged
    :param reverse: A boolean to determine if the list should be sorted in increasing (False)
                    or decreasing (True) order
    :return: A list made up of first and second in the desired order
    """
    final = [0]*(len(first)+len(second))
    i = 0
    j = 0
    if reverse:
        while i+j < len(final):
            if (j >= len(second)) or ((i < len(first)) and (first[i] > second[j])):
                final[i+j] = first[i]
                i += 1
            else:
                final[i+j] = second[j]
                j += 1
    else:
        while i+j < len(final):
            if (j >= len(second)) or ((i < len(first)) and (first[i] < second[j])):
                final[i+j] = first[i]
                i += 1
            else:
                final[i+j] = second[j]
                j += 1
    return final


def insertion_sort(unsorted, reverse):
    """
    Takes an unsorted list and sorts it using the insertion sort method
    in the order specified by the value of reverse
    :param unsorted: The list to be sorted
    :param reverse: A boolean to determine if the list should be sorted in increasing (False)
                    or decreasing (True) order
    :return: A sorted list
    """
    length = len(unsorted)
    if reverse:
        i = 0
        j = 0
        while i < length:
            j = i
            while j > 0 and unsorted[j] > unsorted[j-1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j-1]
                unsorted[j-1] = temp
                j -= 1
            i += 1
    else:
        i = 0
        j = 0
        while i < length:
            j = i
            while j > 0 and unsorted[j] < unsorted[j-1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j - 1]
                unsorted[j - 1] = temp
                j -= 1
            i += 1
    return unsorted
