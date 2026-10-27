"""Testes dos cálculos e relatórios."""

from studytrack.models import StudySession
from studytrack.service import minutes_by_subject, total_minutes


def test_total_minutes() -> None:
    sessions = [
        StudySession("Python", "2026-10-25", 30),
        StudySession("Redes", "2026-10-26", 45),
        StudySession("Python", "2026-10-26", 15),
    ]
    assert total_minutes(sessions) == 90


def test_minutes_by_subject_groups_and_sorts() -> None:
    sessions = [
        StudySession("Python", "2026-10-25", 30),
        StudySession("Redes", "2026-10-26", 45),
        StudySession("Python", "2026-10-26", 15),
    ]
    assert minutes_by_subject(sessions) == {"Python": 45, "Redes": 45}
