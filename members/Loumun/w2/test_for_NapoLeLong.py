import pytest

from members.NapoLeLong.W1.count_frequency import count_frequency


@pytest.mark.parametrize(
    "input_vector, expected",
    [
        ([], {}),
        ([5], {5: 1}),
        ([1, 2, 3], {1: 1, 2: 1, 3: 1}),
        ([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3}),
        (
            ["a", "b", "a", "c", "b", "a"],
            {"a": 3, "b": 2, "c": 1},
        ),
        ([-1, 0, -1, 2.5, 2.5], {-1: 2, 0: 1, 2.5: 2}),
    ],
)
def test_count_frequency_basic(input_vector, expected):
    assert count_frequency(input_vector) == expected


def test_count_frequency_with_tuples():
    vector = [(1, 2), (1, 2), (3, 4)]
    expected = {(1, 2): 2, (3, 4): 1}
    assert count_frequency(vector) == expected


def test_count_frequency_different_iterables():
    assert count_frequency((1, 1, 2, 3, 3)) == {1: 2, 2: 1, 3: 2}


def test_count_frequency_unhashable_type():
    unhashable_vector = [[1, 2], [1, 2]]
    with pytest.raises(TypeError):
        count_frequency(unhashable_vector)
