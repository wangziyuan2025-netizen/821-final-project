from todo.models import Task


def test_create_task():
    task = Task(id=1, title="Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.completed is False
    assert task.priority == "medium"


def test_task_mark_completed():
    task = Task(id=1, title="Test task")
    task.completed = True

    assert task.completed is True