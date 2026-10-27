from studytrack.cli import _register_session


def test_register_session_rejects_non_integer_duration(
    monkeypatch, tmp_path, capsys
):
    inputs = iter(
        ["Python", "2026-10-27", "clear", "Funções e listas"]
    )
    monkeypatch.setattr("builtins.input", lambda _prompt: next(inputs))

    data_file = tmp_path / "sessions.json"
    _register_session(data_file)

    output = capsys.readouterr().out

    assert "a duração deve ser um número inteiro de minutos" in output
    assert not data_file.exists()