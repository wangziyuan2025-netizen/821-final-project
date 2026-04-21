from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    priority: str = "medium"
    due_date: str | None = None
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())