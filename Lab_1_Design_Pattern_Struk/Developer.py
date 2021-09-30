from Assignment import Assignment
from Project import Project
from datetime import datetime

class Developer:
    def __init__(self, id: int, first_name: str, last_name: str, address: str, phone_number: str, email: str, position: int, rank: str, salary: float) -> None:
        if isinstance (id,int) : self.id = id
        if isinstance (first_name,str) : self.first_name = first_name
        if isinstance (last_name,str) : self.last_name = last_name
        if isinstance (address,str) : self.address = address
        if isinstance (phone_number,str) : self.phone_number = phone_number
        if isinstance (email,str) : self.email = email
        if isinstance (position,int) : self.position = position
        if isinstance (rank,str) : self.rank = rank
        if isinstance (salary,float) : self.salary = salary
        self.assignments = []


    def assign_possibility(self,project:Project) -> bool:
        if len(project.developers) == 0:
            print('You can add developer, nobody working here')
            return True
        else:
            print(f'You can`t add developer, {project.developers[0]} already working there')
            return False


    def assigned_projects(self,developer)->list[Project]:
        print(f'Assigned project: {self.assignments[0]}')

    def assign(self, project: Project) -> None:
        project.developers.append(self.last_name)
        assignment = Assignment(received_task={datetime:project.title})
        self.assignments.append(assignment)
        print(f"Assignment for {self.last_name} {self.first_name} to Project '{project.title}' has been done.")

    def unassign(self, project: Project) -> None:
        project.developers.pop(-1)
        self.assignments.pop(-1)