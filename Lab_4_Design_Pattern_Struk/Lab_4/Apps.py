from dataclasses import dataclass
from Project import Project
from abc import ABCMeta

@dataclass
class ProjectFlow(Project):
    progress = ''
    
    def set_progress(self,progress:str) -> str:
        self.progress = progress

@dataclass
class MobileApp(Project):
    os = ''

    def set_os(self,os:str) -> str:
        self.os = os
        
@dataclass
class WebApp(Project):
    ip = ''
    
    def set_ip(self,ip:str) -> str:
        self.ip = ip