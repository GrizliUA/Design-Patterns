from Developer import Developer
from Project import Project
import random

class ProjectManager:
    def __init__(self, id: int, first_name: str, last_name: str, address: str, phone_number: str, email: str, salary: float, project: Project):
        if isinstance (id,int) : self.id = id
        if isinstance (first_name,str) : self.first_name = first_name
        if isinstance (last_name,str) : self.last_name = last_name
        if isinstance (address,str) : self.address = address
        if isinstance (phone_number,str) : self.phone_number = phone_number
        if isinstance (email,str) : self.email = email
        if isinstance (salary,float) : self.salary = salary
        self.project = project


    def discuss_progress(developer: Developer):
        progress_list = ['good job', 'bad work, fix this', 'this is awful, remake it all']
        print(f'Oh, {developer.last_name},',random.choice(progress_list)) 