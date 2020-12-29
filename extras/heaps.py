"""Heaps are for quick extraction of 'priority' items i.e., the biggest
element in a max-heap or the smallest element in a min-heap.

Heaps are complete binary trees, usually implemented internally as an
array. The insert and extract methods run in O(log(n)) time, with n
being the number of elements in the heap array. peek (non-removal) of a
priority item (max or min) is O(1). The O(log(n)) runtime of extraction
means that extracting n nodes would be the equivalent of a O(nlog(n))
sort of the array.

todo: more comments, more tests
"""

# david archuleta jr.

from abc import ABC, abstractclassmethod


class Heap(ABC):
    def __init__(self):
        self.arr = []

    def extract(self):
        # remove and return top element while maintaining heap invariant
        pass

    def insert(self, elem):
        # insert elem into the heap whil maintaining heap invariant
        pass

    def peek(self):
        return self.arr[0]

    def _parent(self, index):
        # how the actual heapq lib does it
        # basically the same thing as //ing by 2^1 i.e., (index -1) // 2
        p = (index - 1) >> 1
        return p if p > 0 else 0

    def _leftChild(self, index):
        return (index * 2) + 1

    def _rightChild(self, index):
        return (index * 2) + 2

    def _swap(self, pos1, pos2):
        self.arr[pos1], self.arr[pos2] = self.arr[pos2], self.arr[pos1]

    def print_heap(self):
        from collections import deque

        if len(self.arr) == 0:
            return []

        q = deque()
        q.append(0)
        levels = []
        while q:
            level = []
            for _ in range(len(q)):
                curr = q.popleft()
                level.append(self.arr[curr])
                left = self._leftChild(curr)
                right = self._rightChild(curr)
                if left and left < len(self.arr):
                    q.append(left)
                if right and right < len(self.arr):
                    q.append(right)
            levels.append(level)
        h = len(levels)
        for idx, level in enumerate(levels):
            print(f'{idx}{" " * (h *(h - idx))}{level}', end="\n")


class MinHeap(Heap):
    def extract(self):
        top = self.arr[0]
        self.arr[0] = self.arr.pop()
        self._minHeapifyDown(0)
        return top

    def insert(self, elem):
        self.arr.append(elem)
        self._minHeapifyUp(len(self.arr) - 1)
        return True

    # the element at index invalidates the heap invariant.
    # shift it upwards towards the root sifting down all other elements
    # that are bigger.
    def _minHeapifyUp(self, index):
        newitem = self.arr[index]
        root = 0  # for clarity

        while index > root:
            parentindex = self._parent(index)
            parent = self.arr[parentindex]
            if newitem < parent:
                self.arr[index] = parent
                index = parentindex
                continue
            break
        self.arr[index] = newitem

    def _minHeapifyDown(self, index):
        left = self._leftChild(index)
        right = self._rightChild(index)

        if self.arr[left] < self.arr[right]:
            smaller = left
        else:
            smaller = right

        if self.arr[smaller] < self.arr[index]:
            self._swap(smaller, index)
            self._minHeapifyDown(smaller)


class MaxHeap(Heap):
    def extract(self):
        top = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self._maxHeapifyDown(0)
        return top

    def insert(self, elem):
        self.arr.append(elem)
        self._maxHeapifyUp(len(self.arr) - 1)

    def _maxHeapifyDown(self, index):
        left = self._leftChild(index)
        right = self._rightChild(index)

        if left > right:
            childIndex = left
        else:
            childIndex = right

        if self.arr[childIndex] > self.arr[index]:
            self._swap(childIndex, index)
            self._maxHeapifyDown(childIndex)

    def _maxHeapifyUp(self, index):
        parent = self._parent(index)

        while self.arr[parent] < self.arr[index]:
            self._swap(parent, index)
            index = parent
            parent = self._parent(index)


if __name__ == "__main__":

    minh = MinHeap()

    for elem in [80, 90, 5, 70, 400, 24, 30, 20, 10]:
        minh.insert(elem)

    minh.print_heap()