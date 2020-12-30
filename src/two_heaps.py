"""Many problems require breaking down a solution into two parts:
one where we will need a smallest element, and another where we will
need a biggest element. For problems like these we can use two heaps:
a min-heap and a max-heap. Some problems also require two heaps of the
same kind.

In Python the heapq module comes in the standard library. From it the
most important methods are heappush and heappop.
"""
from heapq import heappush, heappop

# Example problem 1
#
# Design a class to calculate the median of a number stream that
# has two methods:
#   insertNum(int num): stores the number in the class
#   findMedian(): returns the median of all numbers inserted


class MedianOfAStream:
    def __init__(self):
        self.minh = []
        self.maxh = []

    def insert_num(self, num):
        # O(log(n)) runtime
        # insert into maxh first
        if not self.maxh or num <= -self.maxh[0]:
            heappush(self.maxh, -num)
        else:
            heappush(self.minh, num)

        # maintain balance in the lengths of the two heaps
        self.rebalance_heaps()

    def find_median(self):
        # O(1) runtime
        # if the heaps are equal in length we just return the median
        # value between the two 'tops'
        if len(self.maxh) == len(self.minh):
            return (-self.maxh[0] + self.minh[0]) / 2
        else:
            return -self.maxh[0] / 1.0

    def rebalance_heaps(self):
        # the max-heap should always be one more in length if the heaps
        # are not even.
        if len(self.maxh) < len(self.minh):
            heappush(self.maxh, -heappop(self.minh))
        elif len(self.maxh) > len(self.minh) + 1:
            heappush(self.minh, -heappop(self.maxh))


# Example problem 2
#
# Given an array of numbers and a number 'k', find the median of all the
# 'k' sized sub-arrays (or windows) of the array.

# input: nums [1,2,-1,3,5], k = 2
# output: [1.5, 0.5, 1.0, 4.0]
# window size is two, so we start from the beggining of the list and
# it's collect the median from each pair of indices
# [*1,*2,-1,3,5] -> 5
# [1,*2,*-1,3,5] -> 0.5
# [1,2,*-1,*3,5] -> 1.0
# [1,2,-1,*3,*5] -> 4.o

class SlidingWindowMedian:

    def find_sliding_window_median(self, nums, k):
        pass

