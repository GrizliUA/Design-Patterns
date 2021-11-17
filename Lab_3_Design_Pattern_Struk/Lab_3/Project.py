from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List
from PersonalInfo import PersonalInfo
from Task import Task
from abc import ABCMeta

@dataclass
class Project_A(metaclass=ABCMeta):
    title:str
    start_date:datetime
    task_list: list[int] #task_id's
    developers: list[str]
    materials: dict

    @abstractmethod
    def add_task(self,task) -> None:
        pass

    @abstractmethod
    def remove_task(self,task) -> None:
        pass

    @abstractmethod
    def add_member(member: PersonalInfo) -> None:
        pass

    @abstractmethod
    def remove_member(member: PersonalInfo) -> None:
        pass

    @abstractmethod
    def send_suplementary_materials(task_id: int, material: str) -> None:
        pass


class Project(Project_A):
    def add_task(self,task) -> None:
        self.task_list.append(task)

    def remove_task(self,task) -> None:
        self.task_list.remove(task)

    def add_member(self,member: PersonalInfo) -> None:
        self.developers.append(member.name)

    def remove_member(self,member: PersonalInfo) -> None:
        self.developers.remove(member.name)

    def send_suplementary_materials(self,task_id: int, material: str) -> None:
        for i in self.task_list:
            if i == task_id: self.materials.update({task_id: material})