from datetime import date

import pytest

from shared.contract import Block, Task
from shared.study_planner.render import render


def make_task(title: str) -> Task:
    return Task(title, 4, 2.0, date(2026, 10, 30))

def test_render_empty_list():
    assert render([]) == "No tasks scheduled."

def test_render_one_block():
    block = Block(make_task("Assignment"), 1.5)
    assert render([block]) == "Tonight (1.5 h):\n1. Assignment: 1.5 h"

def test_render_multiple_blocks():
    blocks = [
        Block(make_task("Assignment"), 1.5),
        Block(make_task("DS exam"), 0.5),
    ]
    expected = "Tonight (2.0 h):\n1. Assignment: 1.5 h\n2. DS exam: 0.5 h"
    assert render(blocks) == expected

def test_render_keeps_input_order():
    blocks = [
        Block(make_task("Second task"), 2.0),
        Block(make_task("First task"), 1.0),
    ]
    result = render(blocks)
    assert result.index("Second task") < result.index("First task")

def test_render_rounds_hours_to_one_decimal():
    block = Block(make_task("Review"), 1.234)
    assert render([block]) == "Tonight (1.2 h):\n1. Review: 1.2 h"

def test_render_zero_hours():
    block = Block(make_task("Break"), 0.0)
    assert render([block]) == "Tonight (0.0 h):\n1. Break: 0.0 h"

def test_render_rejects_negative_hours():
    block = Block(make_task("Assignment"), -1.0)
    with pytest.raises(ValueError, match="non-negative"):
        render([block])
