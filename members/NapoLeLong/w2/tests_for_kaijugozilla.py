import pytest
from kaijugozilla.W1.translate import merge_sorted_lists

def test_merge_standard():
    assert merge_sorted_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
def test_merge_different_lengths():
    assert merge_sorted_lists([1, 4], [2, 3, 5, 6]) == [1, 2, 3, 4, 5, 6]
def test_merge_with_empty_lists():
    assert merge_sorted_lists([], [1, 2, 3]) == [1, 2, 3]
    assert merge_sorted_lists([4, 5, 6], []) == [4, 5, 6]
    assert merge_sorted_lists([], []) == []
def test_merge_with_duplicates():
    assert merge_sorted_lists([1, 2, 2], [2, 3, 4]) == [1, 2, 2, 2, 3, 4]
def test_merge_negative_numbers():
    assert merge_sorted_lists([-5, -1, 3], [-3, 0, 4]) == [-5, -3, -1, 0, 3, 4]