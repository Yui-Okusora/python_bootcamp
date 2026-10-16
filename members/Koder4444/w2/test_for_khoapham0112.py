from khoapham0112.w1.translate import binary_search


def test_binary_search_normal_case() -> None:
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2


def test_binary_search_element_at_boundaries() -> None:
    arr = [10, 20, 30, 40]
    assert binary_search(arr, 10) == 0
    assert binary_search(arr, 40) == 3


def test_binary_search_missing_element() -> None:
    arr = [2, 4, 6, 8]
    assert binary_search(arr, 5) == -1


def test_binary_search_empty_list() -> None:
    arr = []
    assert binary_search(arr, 3) == -1


def test_binary_search_single_element() -> None:
    arr = [42]
    assert binary_search(arr, 42) == 0
    assert binary_search(arr, 99) == -1