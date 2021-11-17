from dataclasses import dataclass
from Apps import MobileApp, ProjectFlow, WebApp
from Employee import Employee
from Project import Project
from abc import ABCMeta
from PersonalInfo import PersonalInfo

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

@dataclass
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
        else: print('Input error')
        


    
