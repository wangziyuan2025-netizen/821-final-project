from todo.models import Task
from todo.storage import JSONStorage


def test_save_and_load_tasks(tmp_path):
    file_path = tmp_path / "tasks.json"
    storage = JSONStorage(str(file_path))

    tasks = [
        Task(id=1, title="Task 1", completed=False, priority="low"),
        Task(id=2, title="Task 2", completed=True, priority="high", due_date="2026-04-25"),
    ]

    storage.save(tasks)
    loaded_tasks = storage.load()

    assert len(loaded_tasks) == 2
    assert loaded_tasks[0].title == "Task 1"
    assert loaded_tasks[0].completed is False
    assert loaded_tasks[1].title == "Task 2"
    assert loaded_tasks[1].completed is True
    assert loaded_tasks[1].due_date == "2026-04-25"


def test_load_returns_empty_list_when_file_does_not_exist(tmp_path):
    file_path = tmp_path / "missing.json"
    storage = JSONStorage(str(file_path))

    loaded_tasks = storage.load()

    assert loaded_tasks == []