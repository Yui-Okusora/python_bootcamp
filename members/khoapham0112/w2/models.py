import datetime
from dataclasses import dataclass


@dataclass
class Task:
   title: str
   importance: int
   effort_h: float
   deadline: datetime.date
   
   def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
   def days_left(self, today: datetime.date):
       diff = self.deadline - today
       if(diff.days < 0):
           return 0
       return diff.days