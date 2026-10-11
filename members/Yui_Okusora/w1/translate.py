def transpose(matrix: list[list[int]]) -> list[list[int]]:
    """Transpose a 2D matrix (vector of vectors).

    Difference from C++:
    In C++, transposing requires pre-allocating output vector capacities and using
    explicit nested loops indexed by row and column indices. Python pre-allocates
    dynamically using list comprehension and updates values by index.
    """
    if not matrix or not matrix[0]:
        return []

    return [list(col) for col in zip(*matrix)]