from dataclasses import dataclass
from Assignment import Assignment
from Project import Project
from datetime import datetime
from PersonalInfo import PersonalInfo
from abc import ABCMeta

@dataclass
class Employee(metaclass=ABCMeta):
    def __init__(self,personal_info: PersonalInfo) -> None:
        self.personal_info = personal_info
        self.assignments = []

    @property
    def personal_info(self) -> PersonalInfo:
        return self._personal_info

    @personal_info.setter
    def personal_info(self,personal_info: PersonalInfo) -> None:
        if isinstance(personal_info, PersonalInfo):
            self._personal_info = personal_info
        else:
            raise AttributeError('Can not set non PersonalInfo object')

    def calculate_tax(self) -> float:
        return self.personal_info.salary*0.12

    def calculate_salary(self) -> float:
        return self.personal_info.salary-Employee.calculate_tax(self)

    @staticmethod
    def assign_possibility(project: Project) -> bool:
        if len(project.developers) == 0:
            print('You can add developer, nobody working here')
            return True
        else:
            print(f'You can`t add developer, {project.developers[0]} already working there')
            return False

    def assigned_projects(self) -> list[Project]:
        if len(self.assignments) == 0:
            print('No assigned projects')
        else:
            print(f'Assigned project: {self.assignments}')

    

    def assign(self, project: Project) -> None:
        project.developers.append(self.personal_info.name)
        assignment = Assignment(received_task={project.start_date:project.title})
        self.assignments.append(assignment.received_tasks)
        print(f"Assignment for {self.personal_info.name} to Project '{project.title}' has been done.")

    def unassign(self, project: Project) -> None:
        project.developers.pop(-1)
        self.assignments.pop(-1)
