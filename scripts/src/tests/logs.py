import os
from app.installer.window_app import next_action, cancel_action


def test_next_action():
    next_action()

    assert os.path.exists("logs")

    with open("logs/logs.txt", "r") as arquivo:
        conteudo = arquivo.read()
        assert "Log do próximo passo" in conteudo


def test_cancel_action():
    cancel_action()

    assert os.path.exists("logs")

    with open("logs/logs.txt", "r") as arquivo:
        conteudo = arquivo.read()
        assert "Log do cancelamento" in conteudo
