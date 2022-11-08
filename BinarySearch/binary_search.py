# -*- coding: utf-8 -*-

import time
import random


def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i # return the index
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0 # lowest possible
    if high is None:
        high = len(l) - 1

    if high < low: # target its not in the list
        return -1

    # example l = [1, 3, 5, 10, 12]  # should return 3 in our example because we choose the number 10
    midpoint = (low + high) // 2  # 2

    # we'll check if l[midpoint] == target, and if not, we can find out if
    # target will be to the left or right of midpoint
    # we know everything to the left of midpoint is smaller than the midpoint
    # and everything to the right is larger

    if l[midpoint] == target:
        return midpoint # our index
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

if __name__=='__main__':

    '''
    l = [1, 3, 5, 10, 12]
    target = 3
    print('Naive search: ', naive_search(l, target))
    print('Binary search: ', binary_search(l, target))

    '''
    # it shows the time for each search in order to compare both of the methots
    # so, given the results, binary search is fastest
    length = 10000
    # build a sorted list of length 10000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length)) # range -30000 to 30000
    sorted_list = sorted(list(sorted_list))

    #naive search time
    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('Naive search time: ', (end - start), 'seconds')

    #binary search time
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('Binary search time: ', (end - start), 'seconds')
  
