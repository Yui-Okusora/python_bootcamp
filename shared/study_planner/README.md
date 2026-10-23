# Study Planner

A command-line tool that helps you optimally schedule study sessions from a task list. The program reads task data from a CSV file, prioritizes important assignments, allocates available time, and displays a detailed study plan.

## Pipeline Structure
The tool processes data through the following sequence:
`parse_csv` → `prioritise` → `allocate` → `render`

## Usage

Run the module via the command line using the following syntax:
```bash
python -m shared.study_planner <path_to_csv> --hours <number_of_hours>