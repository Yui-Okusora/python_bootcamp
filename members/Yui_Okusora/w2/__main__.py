from pathlib import Path

from .io_utils import load_tasks


def main():
  csv_path = Path(__file__).parent / 'tasks.csv'

  if not csv_path.exists():
    csv_path.write_text(
        'title,importance,effort_h,deadline\n'
        'DS exam,5,6,2026-10-30\n'
        'Assignment,4,1.5,2026-10-27\n',
        encoding='utf-8',
    )

  tasks = load_tasks(csv_path)

  print('--- Loaded tasks ---')
  for task in tasks:
    print(
        f'- {task.title} (Importance: {task.importance}, Time:'
        f' {task.effort_h}h, Deadline: {task.deadline})'
    )


if __name__ == '__main__':
  main()