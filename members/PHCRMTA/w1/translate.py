def insertion_sort(arr: list[int]) -> list[int]:
    """Sorts a list of integers in place using insertion sort and returns it.

    Difference from C++:
    - C++ requires explicit parameter types like std::vector<int>& for pass-by-reference.
      Python automatically passes lists as mutable references, so modifications happen direcly in-place
      without special reference syntax (&).
    - In python, we can swap elements cleanly using tuple unpacking (arr[j], arr[j - 1] = arr[j - 1], arr[j])
      instead of using std::swap() or a temporary variable like in C++.
    """    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr


