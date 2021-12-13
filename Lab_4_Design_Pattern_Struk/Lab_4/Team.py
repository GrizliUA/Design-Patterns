from dataclasses import dataclass
from Apps import MobileApp, ProjectFlow, WebApp
from Employee import Employee
from Project import Project
from PersonalInfo import PersonalInfo
from abc import ABCMeta, abstractmethod
from datetime import datetime
import os

@dataclass
class Team:
    id: int
    name:str
    member_list: list[int]   #member id`s
    suplementary_materials:dict   #{'task_id':[link1,link2...]}
    project_id:int


@dataclass
class TeamLead(Employee):                 
    def __init__(self,personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.team = Team

@dataclass
class TopManagement(metaclass=ABCMeta):
    def __init__(self,personal_info: PersonalInfo) -> None:
        self.personal_info = personal_info
        self.projects = []


    def fill_project(self,team_lead:TeamLead,team:Team) -> None:
        team_lead.team = team

    def attach_project(self,*args) -> list[Project]:
        self.projects = args

@dataclass
class ChiefTechnicalOfficer(TopManagement):
    def __init__(self,personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.project = []

    def attach_project(self,*args) -> ProjectFlow:
        try:
            self.project = ProjectFlow(args[0],args[1],args[2],args[3],args[4])
        except: print('Input error')
        try: 
            self.project.set_progress(args[5])
        except: pass



'''@dataclass
class SolutionArchitect(TopManagement):
    def __init__(self,personal_info: PersonalInfo) -> None:
        super().__init__(personal_info)
        self.project = []

    def attach_project(self,*args) -> Project:
        if args[0] == 'mob':
            try:
                self.project = MobileApp(args[0],args[1],args[2],args[3],args[4])
            except: print('Input error')
            try: 
                self.project.set_os(args[5])
            except: pass
        elif args[0] == 'web':
            try:
                self.project = WebApp(args[0],args[1],args[2],args[3],args[4])
            except: print('Input error')
            try: 
                self.project.set_ip(args[5])
            except: pass
        else: print('Input error')'''
        


    
@dataclass
class ISolutionArchitect(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def set_title(self):
        pass

    @staticmethod
    @abstractmethod
    def set_start_date(self):
        pass

    @staticmethod
    @abstractmethod
    def create_deadlines(self):
        pass

    @staticmethod
    @abstractmethod
    def create_task(self):
        pass

    @staticmethod
    @abstractmethod
    def assign_developers(self):
        pass

    @staticmethod
    @abstractmethod
    def add_materials(self):
        pass

    @staticmethod
    @abstractmethod
    def get_result(self):
        pass

@dataclass
class SolutionArchitect(ISolutionArchitect):
    def __init__(self):
        self.project = Project()

    def set_title(self):
        os.system('CLS')
        title = input("Enter title\n")
        self.project.title = title
        return self

    def set_start_date(self):
        os.system('CLS')
        start_date = input("Enter start date\n")
        self.project.start_date = start_date
        return self

    def create_deadlines(self):
        os.system('CLS')
        deadline = input("Enter deadline\n")
        self.project.deadline = deadline
        return self

    def create_task(self):
        os.system('CLS')
        task = input("Enter task\n")
        self.project.task_list.append(task)
        return self

    def assign_developers(self):
        os.system('CLS')
        id = input("Enter developer's id to add him\n")
        self.project.developers.append(id)
        return self

    def add_materials(self):
        os.system('CLS')
        task_id = input("Enter task id\n")
        material = input("Enter materials\n")
        self.project.materials.update({task_id: material})
        return self

    def get_result(self):
        return self.project

@dataclass
class Project(metaclass=ABCMeta):
    def __init__(self):
        self.title = ''
        self.start_date:datetime = ''
        self.deadline:datetime = ''
        self.task_list: list[int] = []
        self.developers: list[str] = []
        self.materials: dict = {}

@dataclass
class SeniorSolutionArchitect():
    @staticmethod
    def create_project():
        "Constructs and returns the final product"
        return SolutionArchitect()\
            .set_title()\
            .set_start_date()\
            .create_deadlines()\
            .create_task()\
            .assign_developers()\
            .add_materials()\
            .get_result()