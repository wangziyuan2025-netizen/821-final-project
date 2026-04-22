# 821 Final Project
Ziyuan Wang

## Overview

This project is a simple command-line todo application written in Python.
It allows users to manage tasks from the terminal, including adding, listing, completing, and deleting tasks. Tasks are stored locally in a JSON file.

The goal of this project is to practice building a small Python library with a clean structure and basic software engineering practices.

---

## Features

* Add new tasks
* List all tasks
* Mark tasks as completed
* Delete tasks
* Save and load tasks using a JSON file

---

## Project Structure

```text
src/todo/
    models.py    # defines the Task data structure
    service.py   # contains the core task management logic
    storage.py   # handles saving/loading tasks from JSON
    cli.py       # command-line interface

tests/
    test_models.py
    test_service.py
    test_storage.py

README

```

---

## How to Run

From the project root directory:

```bash
$env:PYTHONPATH="src"
python -m todo.cli add "Buy milk"
python -m todo.cli list
python -m todo.cli complete 1
python -m todo.cli delete 1
```

---

## Running Tests

```bash
pytest
```

All core functionality is covered by unit tests in the `tests/` folder.

---

## Notes

* The CLI is intentionally kept simple and focuses on demonstrating functionality.
* Business logic is separated from the CLI to keep the design clean.
* Tasks are stored in a local `tasks.json` file (ignored by git).

---

## AI Usage

ChatGPT was used during development for:

* debugging errors
* suggesting code structure
* helping write initial versions of some functions



