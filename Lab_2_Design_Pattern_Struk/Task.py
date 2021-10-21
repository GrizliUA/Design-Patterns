from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Task:
    id:int
    title:str
    deadline:datetime
    items:List[str]
    status:float
    related_project:str

    def implement_items(self, item_name: str) -> str:
        pass

    def add_comment(self, comment: str) -> str:
        self.comment = comment
        comment = print("Comment was added")
        return comment