"""Interface de linha de comando do StudyTrack."""

import os
from datetime import date
from pathlib import Path

from studytrack.models import StudySession
from studytrack.service import minutes_by_subject, total_minutes
from studytrack.storage import load_sessions, save_sessions

DEFAULT_DATA_FILE = Path.home() / ".studytrack" / "sessions.json"


def _data_file() -> Path:
    """Permite definir outro arquivo de dados pela variável STUDYTRACK_DATA."""
    configured_path = os.getenv("STUDYTRACK_DATA")
    return Path(configured_path).expanduser() if configured_path else DEFAULT_DATA_FILE


def _register_session(path: Path) -> None:
    subject = input("Disciplina: ").strip()
    raw_date = input(f"Data (AAAA-MM-DD) [hoje: {date.today().isoformat()}]: ").strip()
    session_date = raw_date or date.today().isoformat()
    raw_duration = input("Duração em minutos: ").strip()
    notes = input("Conteúdo estudado (opcional): ").strip()

    try:
        duration = int(raw_duration)
    except ValueError:
        print(
            "Não foi possível registrar a sessão: "
            "a duração deve ser um número inteiro de minutos."
        )
        return

    try:
        session = StudySession(subject, session_date, duration, notes)
        sessions = load_sessions(path)
        sessions.append(session)
        save_sessions(path, sessions)
    except (ValueError, OSError) as exc:
        print(f"Não foi possível registrar a sessão: {exc}")
        return
    print("Sessão registrada com sucesso!")


def _list_sessions(path: Path) -> None:
    try:
        sessions = load_sessions(path)
    except (ValueError, OSError) as exc:
        print(f"Não foi possível carregar as sessões: {exc}")
        return

    if not sessions:
        print("Nenhuma sessão cadastrada ainda.")
        return

    print("\n=== Sessões registradas ===")
    for index, session in enumerate(sessions, start=1):
        print(
            f"{index}. {session.date} | {session.subject} | "
            f"{session.duration_minutes} min"
        )
        if session.notes:
            print(f"   Conteúdo: {session.notes}")


def _show_report(path: Path) -> None:
    try:
        sessions = load_sessions(path)
    except (ValueError, OSError) as exc:
        print(f"Não foi possível gerar o relatório: {exc}")
        return

    if not sessions:
        print("Registre uma sessão para visualizar o relatório.")
        return

    minutes = total_minutes(sessions)
    hours, remainder = divmod(minutes, 60)
    print(f"\nTempo total estudado: {hours} h e {remainder} min")
    print("Tempo por disciplina:")
    for subject, subject_minutes in minutes_by_subject(sessions).items():
        print(f"- {subject}: {subject_minutes} min")


def main() -> None:
    """Executa o menu principal."""
    path = _data_file()
    while True:
        print("\n=== StudyTrack ===")
        print("1. Registrar sessão de estudo")
        print("2. Listar sessões")
        print("3. Ver relatório")
        print("0. Sair")
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            _register_session(path)
        elif option == "2":
            _list_sessions(path)
        elif option == "3":
            _show_report(path)
        elif option == "0":
            print("Até a próxima sessão de estudos!")
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 0.")
