"""Testes de validação do modelo de sessão."""

import pytest

from studytrack.models import StudySession


def test_create_valid_session() -> None:
    session = StudySession("Python", "2026-10-26", 45, "Laços de repetição")
    assert session.subject == "Python"
    assert session.duration_minutes == 45


@pytest.mark.parametrize(
    ("subject", "session_date", "duration", "message"),
    [
        ("   ", "2026-10-26", 30, "disciplina"),
        ("Python", "26/10/2026", 30, "AAAA-MM-DD"),
        ("Python", "2026-10-26", 0, "maior que zero"),
        ("Python", "2026-10-26", -5, "maior que zero"),
    ],
)
def test_reject_invalid_session(
    subject: str, session_date: str, duration: int, message: str
) -> None:
    with pytest.raises(ValueError, match=message):
        StudySession(subject, session_date, duration)
