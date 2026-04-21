import json
from pathlib import Path
from typing import List

from todo.models import Task


class JSONStorage:
    def __init__(self, file_path: str = "tasks.json") -> None:
        self.file_path = Path(file_path)

    def save(self, tasks: List[Task]) -> None:
        data = [task.__dict__ for task in tasks]
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load(self) -> List[Task]:
        if not self.file_path.exists():
            return []

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return [Task(**item) for item in data]