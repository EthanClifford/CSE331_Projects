import Project3.HybridSort as Hs
from random import shuffle

unsorted = [i for i in range(10)]
threshold = 5
reverse = False
shuffle(unsorted)
print("unsorted: ", unsorted)
unsorted = Hs.merge_sort(unsorted, threshold, reverse)
print("sorted: ", unsorted)
