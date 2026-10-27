"""Testes da persistência em JSON."""

from pathlib import Path

from studytrack.models import StudySession
from studytrack.storage import load_sessions, save_sessions


def test_missing_file_returns_empty_list(tmp_path: Path) -> None:
    assert load_sessions(tmp_path / "missing.json") == []


def test_save_and_load_sessions(tmp_path: Path) -> None:
    path = tmp_path / "data" / "sessions.json"
    original = [StudySession("Redes", "2026-10-26", 50, "Modelo OSI")]

    save_sessions(path, original)

    assert load_sessions(path) == original
