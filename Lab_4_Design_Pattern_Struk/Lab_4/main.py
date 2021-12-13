from Apps import MobileApp, ProjectFlow, WebApp
from Project import Project
from datetime import datetime
from ProjectManager import ProjectManager
from Employee import Employee
from Developer import Developer
from PersonalInfo import PersonalInfo
from QualityAssurance import QualityAssurance
from Task import Task
from Assignment import Assignment
from Team import *

if __name__ == '__main__':
    
    employee = Employee(PersonalInfo(
                                        id=1, 
                                        name='Test', 
                                        address='test', 
                                        phone_number='test', 
                                        email='test', 
                                        position=1, 
                                        rank='test', 
                                        salary=750))

    #print(f'{employee._personal_info.name} taxes = {employee.calculate_tax()}\nTotal salary = {employee.calculate_salary()}')

    dev = Developer(PersonalInfo(
                                        id=2, 
                                        name='Morgan', 
                                        address='Ternopil', 
                                        phone_number='8800', 
                                        email='test@test.com', 
                                        position=2, 
                                        rank='Junior', 
                                        salary=550))
    #print(f'{dev._personal_info.name} taxes = {dev.calculate_tax()}\nTotal salary = {dev.calculate_salary()}')

    manager = ProjectManager(PersonalInfo(
                                        id=3, 
                                        name='Garfild', 
                                        address='London', 
                                        phone_number='+500', 
                                        email='test@uk.en', 
                                        position=3, 
                                        rank='Recruit', 
                                        salary=50))
    #print(f'{manager._personal_info.name} taxes = {manager.calculate_tax()}\nTotal salary = {manager.calculate_salary()}')


    qual_assure = QualityAssurance(PersonalInfo(
                                        id=4, 
                                        name='Itachi', 
                                        address='Japan', 
                                        phone_number='099', 
                                        email='japan@test.jp', 
                                        position=1, 
                                        rank='Senior', 
                                        salary=1200))
    #print(f'{qual_assure._personal_info.name} taxes = {qual_assure.calculate_tax()}\nTotal salary = {qual_assure.calculate_salary()}')

    '''project1 = WebApp('Data Science',
                        datetime(2021,12,31),
                        [],
                        [],
                        {})'''
    '''project1 = MobileApp(Project(
                        title ='Data Science',
                        start_date = datetime(2021,11,17),
                        task_list = [],
                        developers = [],
                        materials = {}),
                        os = '192')'''

    '''project1 = MobileApp(Project(
                        title ='Data Science',
                        start_date = datetime(2025,12,25,12,25,25),
                        task_list = [],
                        developers = [],
                        materials = {}))'''
    '''project1 = MobileApp(title ='Data Science',
                        start_date = datetime(2025,12,25,12,25,25),
                        task_list = [],
                        developers = [],
                        materials = {})'''

    #print(project1.os)
    #project1.set_os('192')
    #print(project1.os)
    #print(project1.materials)
    #project1.add_task(1)
    #print(project1.task_list)
    #project1.send_suplementary_materials(1,'Make a coffee')
    #print(project1.materials)

    '''task1 = Task(1,'Make Coffee',(2021,10,25),[],0.0,'wake,up')
        task1.add_comment('Waked up')
    print(task1.comment)

    print(task1)
    project1.add_task(task1.id)
    print(project1.task_list)
    project1.add_developer(dev.personal_info.name)   
    print(project1.developers)
    project1.remove_developer(dev.personal_info.name)
    print('\n\n-----')
    print(project1.developers)
    project1.remove_task(1)
    print(project1.task_list)
    

    dev.set_task(task1)
    print(dev.tasks)
    manager.discuss_progress(dev)'''

    '''print(employee.assign_possibility(project1))
    project1.add_developer(dev.personal_info.name)
    print(employee.assign_possibility(project1))
    project1.remove_developer(dev.personal_info.name)
    print(employee.assign_possibility(project1))'''

    '''assigment = Assignment({'Wake up':(2021,10,31),'Make tea':(2021,11,15),'Drink tea':(2021,12,25),'Wash cup':(2021,12,31)})
    print(assigment.received_tasks)
    print(assigment.received_tasks.get('Wake up'))

    assigment.get_tasks_by_date()
    print('\n\n\n\n')
    assigment1 = Assignment({'Make tea':(2021,11,15),'Wake up':(2021,10,31),'Wash cup':(2021,12,31),'Drink tea':(2021,12,25)})
    assigment1.get_tasks_by_date()'''

    '''employee.assign_possibility(project1)
    employee.assigned_projects()

    qual_assure.set_task(task1)
    print(qual_assure.tasks)'''




'''    project = Project(title='Making a cup of Tea', start_date=(2021,10,31),task_list=[],developers=[])
    employee.assign(project)
    employee.assigned_projects()'''

'''    print(project.developers)
    employee.unassign(project)
    employee.assigned_projects()
    print(project.developers)
    employee.assign_possibility(project)'''

lead = TeamLead(PersonalInfo(
                                        id=2, 
                                        name='Morgan', 
                                        address='Ternopil', 
                                        phone_number='8800', 
                                        email='test@test.com', 
                                        position=2, 
                                        rank='Junior', 
                                        salary=550))

team_1 = Team(id=1,
                name='NAVI',
                member_list=[employee,dev,manager,qual_assure],
                suplementary_materials={},
                project_id=1)
#print(team_1)


top_manager = TopManagement(PersonalInfo(
                                        id=2, 
                                        name='Morgan', 
                                        address='Ternopil', 
                                        phone_number='8800', 
                                        email='test@test.com', 
                                        position=2, 
                                        rank='Junior', 
                                        salary=550))

#print(lead.team)

#top_manager.fill_project(lead,team_1.id)
#print('--------')
#print(team_1)
#top_manager.fill_project(lead,team_1)
#print(lead.team)
#top_manager.attach_project(project1)


chieftain = ChiefTechnicalOfficer(PersonalInfo(
                                        id=2, 
                                        name='Morgan', 
                                        address='Ternopil', 
                                        phone_number='8800', 
                                        email='test@test.com', 
                                        position=2, 
                                        rank='Junior', 
                                        salary=550))

#print(chieftain)
#chieftain.attach_project('Data Science',(2025,12,25),[],[],{},15)
#print(chieftain.project)
#print(chieftain.project.progress)

'''archi = SolutionArchitect(PersonalInfo(
                                        id=2, 
                                        name='Morgan', 
                                        address='Ternopil', 
                                        phone_number='8800', 
                                        email='test@test.com', 
                                        position=2, 
                                        rank='Junior', 
                                        salary=550))'''

#print(archi)
#print(archi.project)
#archi.attach_project('mob','Data Science',(2025,12,25),[],[],{},15)
#print(archi.project)


#project = SeniorSolutionArchitect.create_project()