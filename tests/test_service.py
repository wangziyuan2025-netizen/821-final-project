import pytest

from todo.service import TaskNotFoundError, TaskService


def test_add_task():
    service = TaskService()

    task = service.add_task("Finish project")

    assert task.id == 1
    assert task.title == "Finish project"
    assert task.completed is False
    assert len(service.tasks) == 1


def test_list_tasks():
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")

    tasks = service.list_tasks()

    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_complete_task():
    service = TaskService()
    service.add_task("Read book")

    task = service.complete_task(1)

    assert task.completed is True
    assert service.tasks[0].completed is True


def test_delete_task():
    service = TaskService()
    service.add_task("Task to delete")

    service.delete_task(1)

    assert len(service.tasks) == 0


def test_get_task_by_id():
    service = TaskService()
    service.add_task("Find me")

    task = service.get_task_by_id(1)

    assert task.title == "Find me"


def test_complete_task_invalid_id():
    service = TaskService()

    with pytest.raises(TaskNotFoundError):
        service.complete_task(999)


def test_delete_task_invalid_id():
    service = TaskService()

    with pytest.raises(TaskNotFoundError):
        service.delete_task(999)