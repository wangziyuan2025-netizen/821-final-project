import argparse

from todo.service import TaskService
from todo.storage import JSONStorage


def main():
    parser = argparse.ArgumentParser(description="Todo CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument("--priority", default="medium")
    add_parser.add_argument("--due")

    # list
    subparsers.add_parser("list")

    # complete
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int)

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)

    args = parser.parse_args()

    storage = JSONStorage()
    service = TaskService()
    service.tasks = storage.load()

    if args.command == "add":
        task = service.add_task(
            args.title,
            priority=args.priority,
            due_date=args.due,
        )
        storage.save(service.tasks)
        print(f"Added task {task.id}: {task.title}")

    elif args.command == "list":
        tasks = service.list_tasks()
        for task in tasks:
            status = "✔" if task.completed else "✘"
            print(f"{task.id}. [{status}] {task.title}")

    elif args.command == "complete":
        task = service.complete_task(args.id)
        storage.save(service.tasks)
        print(f"Completed task {task.id}")

    elif args.command == "delete":
        service.delete_task(args.id)
        storage.save(service.tasks)
        print(f"Deleted task {args.id}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()