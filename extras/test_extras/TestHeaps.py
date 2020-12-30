import pytest

from ..heaps import MinHeap, MaxHeap

class TestHeaps:
    def test_insertmax(self):
        maxh = MaxHeap()

        maxh.insert(4)
        assert maxh.peek() == 4

        maxh.insert(5)
        assert maxh.peek() == 5

        maxh.insert(1)
        assert maxh.peek() == 5


    def test_insertmin(self):
        minh = MinHeap()

        minh.insert(4)
        assert minh.peek() == 4

        minh.insert(5)
        assert minh.peek() == 4

        minh.insert(1)
        assert minh.peek() == 1

    def test_extractmax(self):
        maxh = MaxHeap()

        maxh.insert(3)
        maxh.insert(5)
        maxh.insert(1)
        maxh.insert(8)
        maxh.insert(2)

        top = maxh.extract()
        assert top == 8
        assert maxh.peek() == 5

    def test_extractmin(self):
        minh = MinHeap()

        for num in [3,5,1,8,2]:
            minh.insert(num)
        
        top = minh.extract()
        assert top == 1
        assert minh.peek() == 2
