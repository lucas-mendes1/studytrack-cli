"""Regras de negócio e relatórios do StudyTrack."""

from collections import defaultdict

from studytrack.models import StudySession


def total_minutes(sessions: list[StudySession]) -> int:
    """Retorna a soma da duração de todas as sessões."""
    return sum(session.duration_minutes for session in sessions)


def minutes_by_subject(sessions: list[StudySession]) -> dict[str, int]:
    """Agrupa o tempo de estudo por disciplina."""
    totals: dict[str, int] = defaultdict(int)
    for session in sessions:
        totals[session.subject] += session.duration_minutes
    return dict(sorted(totals.items(), key=lambda item: item[0].casefold()))
