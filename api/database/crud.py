from sqlalchemy.orm import Session
from schemas import ServerInfo
from database.modeles import Server


def get_servers_info(session: Session) -> list[ServerInfo]:
    """Возвращает информацию о всех серверах из бд"""
    return session.query(Server).all()
