from datetime import datetime

class Project:
    def __init__(self, title: str, start_date: datetime) -> None:
        if isinstance (title, str) : self.title = title
        if isinstance (start_date, datetime) : self.start_date = start_date
        self.task_list = []
        self.developers = []

    def add_developer(self, last_name) -> None:
        self.developers.append(last_name)

    def remove_developer(self, last_name) -> None:
        self.developers.remove(last_name)