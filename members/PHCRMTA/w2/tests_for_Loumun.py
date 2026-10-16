# noqa: N999
from members.Loumun.w1.remove_dupp import remove_Dupp


def test_remove_Dupp_basic_numbers():
    assert remove_Dupp([1, 2, 2, 3, 4, 3, 1, 5]) == [1, 2, 3, 4, 5]


def test_remove_Dupp_strings():
    assert remove_Dupp(["apple", "banana", "apple", "orange"]) == [
        "apple",
        "banana",
        "orange",
    ]


def test_remove_Dupp_preserve_order():
    assert remove_Dupp([4, 5, 4, 1, 2, 5, 3]) == [4, 5, 1, 2, 3]


def test_remove_Dupp_empty_list():
    assert remove_Dupp([]) == []



def test_remove_Dupp_edge_case_unhashable_elements():
    input_vector = [[1, 2], [1, 2], [3, 4], [1, 2]]
    expected = [[1, 2], [3, 4]]

    assert remove_Dupp(input_vector) == expected