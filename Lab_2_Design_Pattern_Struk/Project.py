from abc import abstractmethod
from dataclasses import dataclass
from datetime import datetime
from typing import List
from Task import Task
from abc import ABCMeta

@dataclass
class Project(metaclass=ABCMeta):
    title:str
    start_date:datetime
    task_list: list[int] #task_id's
    developers: list[str]

    def add_developer(self, name) -> None:
        self.developers.append(name)

    def remove_developer(self, name) -> None:
        self.developers.remove(name)

    def add_task(self,task) -> None:
        self.task_list.append(task)

    def remove_task(self,task) -> int:
        self.task_list.remove(task)
