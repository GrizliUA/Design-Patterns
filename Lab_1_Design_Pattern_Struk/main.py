from ProjectManager import ProjectManager
from Developer import Developer
from Project import Project
from datetime import datetime

if __name__ == '__main__':
    developer = Developer(
        id=1,
        first_name='Freeman',
        last_name='Morgan',
        address='half@life.com',
        phone_number='88005553535',
        email='wikipedia@wiki.com',
        position='junior',
        rank=2,
        salary=500)

    project = Project(title='Miner 3000',start_date=datetime.now())
    developer.assign(project)
    #developer.assigned_projects(developer)
    #developer.assign_possibility(project)
    #developer.unassign(project)
    #developer.assign_possibility(project)


    #ProjectManager.discuss_progress(developer)
    


    #developer.unassign(project)
    #developer.assign_possibility(project)
    
    #project.add_developer('Morgan')
    #for x in project.developers: print(x)
    #project.remove_developer('Morgan')
    #for x in project.developers: print(x)