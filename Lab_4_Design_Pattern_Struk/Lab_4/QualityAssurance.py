from dataclasses import dataclass
from Employee import Employee
from datetime import datetime
from PersonalInfo import PersonalInfo
from Task import Task
from collections import defaultdict

@dataclass
class QualityAssurance(Employee):
    def __init__(self,personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.tasks = defaultdict(list)

    def calculate_tax(self) -> float:
        return self.personal_info.salary*0.2

    def calculate_salary(self) -> float:
        return self.personal_info.salary-self.calculate_tax()

    def set_task(self,task: Task) -> None:
        self.tasks[datetime.now()].append(task)

    def add_ticket() -> None:
        pass