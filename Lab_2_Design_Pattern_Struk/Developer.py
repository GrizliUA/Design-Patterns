
from PersonalInfo import PersonalInfo
from Employee import Employee
from datetime import datetime
from Task import Task
from collections import defaultdict

class Developer(Employee):
    def __init__(self,personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.tasks = defaultdict(list)
        self.salary = 0.0

    def calculate_tax(self) -> float:
        return self.personal_info.salary*0.18

    def calculate_salary(self) -> float:
        return self.personal_info.salary-self.calculate_tax()

    def set_task(self,task: Task) -> None:
        self.tasks[datetime.now()].append(task)


