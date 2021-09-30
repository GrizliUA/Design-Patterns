from datetime import datetime

class Assignment:
    def __init__(self,received_task: dict) -> None:
        self.received_tasks = {}

    def get_tasks_by_date(self, date_by: datetime) -> str:
        task_by_date = []
        for date, tasks in self.received_tasks.items():
            if date <= date_by:
                task_by_date.append(tasks)
        return task_by_date