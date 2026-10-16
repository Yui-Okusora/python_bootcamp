from datetime import date
from shared.contract import Block, Task
from shared.study_planner.allocate import allocate


def test_allocate_greedy():
  t1 = Task("DS Exam", 5, 4.0, date(2026, 10, 30))
  t2 = Task("Assignment", 4, 3.0, date(2026, 10, 27))

  # Allocating 5 available hours to tasks needing 4h and 3h
  blocks = allocate([t1, t2], hours=5.0)

  assert len(blocks) == 2
  assert blocks[0] == Block(task=t1, hours=4.0)
  assert blocks[1] == Block(task=t2, hours=1.0)