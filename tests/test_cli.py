import sys
from todo.cli import main


def test_cli_add(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["todo", "add", "Test task"])
    main()

    captured = capsys.readouterr()
    assert "Added task" in captured.out