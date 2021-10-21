from Developer import Developer
from dataclasses import dataclass
from Employee import Employee
import random
from PersonalInfo import PersonalInfo

@dataclass
class ProjectManager(Employee):
    def __init__(self,personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)

    def calculate_tax(self) -> float:
        return self.personal_info.salary*0.15

    def calculate_salary(self) -> float:
        return self.personal_info.salary-self.calculate_tax()

    def discuss_progress(self,developer: Developer):
        progress_list = ['good job', 'bad work, fix this, or you will have a bad time.', 'this is awful, remake it all, or you will have a bad time.']
        print(f'Oh, {developer.personal_info.name},',random.choice(progress_list))
