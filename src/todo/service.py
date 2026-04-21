from todo.models import Task


class TaskNotFoundError(Exception):
    pass


class TaskService:
    def __init__(self) -> None:
        self.tasks: list[Task] = []

    def add_task(
        self,
        title: str,
        priority: str = "medium",
        due_date: str | None = None,
    ) -> Task:
        task = Task(
            id=self._next_id(),
            title=title,
            priority=priority,
            due_date=due_date,
        )
        self.tasks.append(task)
        return task

    def list_tasks(self) -> list[Task]:
        return self.tasks

    def complete_task(self, task_id: int) -> Task:
        task = self.get_task_by_id(task_id)
        task.completed = True
        return task

    def delete_task(self, task_id: int) -> None:
        task = self.get_task_by_id(task_id)
        self.tasks.remove(task)

    def get_task_by_id(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(f"Task with id {task_id} not found")

    def _next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1