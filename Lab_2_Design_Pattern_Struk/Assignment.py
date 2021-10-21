from dataclasses import dataclass
from datetime import datetime
from Project import Project

@dataclass
class Assignment:
    def __init__(self,received_task: dict) -> None:
        self.received_tasks = received_task

    def get_tasks_by_date(self) -> None:
        sorted_values = sorted(self.received_tasks.values()) # Sort the values
        sorted_dict = {}    
        for i in sorted_values:
            for k in self.received_tasks.keys():
                if self.received_tasks[k] == i:
                    sorted_dict[k] = self.received_tasks[k]
                    break
        print(sorted_dict)