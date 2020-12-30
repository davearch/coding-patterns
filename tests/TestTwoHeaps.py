import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from two_heaps import MedianOfAStream

class TestTwoHeaps:

    def test_median_stream(self):
        stream = MedianOfAStream()

        stream.insert_num(3)
        stream.insert_num(1)
        assert stream.find_median() == 2.0

        stream.insert_num(5)
        assert stream.find_median() == 3.0
        stream.insert_num(4)
        assert stream.find_median() == 3.5