from sqlalchemy import desc
from sqlalchemy.orm import Session
from schemas import ServerInfo, UserStats, UserTop
from database.modeles import Server, OrmUserStat


def get_servers_info(session: Session) -> list[ServerInfo]:
    """Возвращает информацию о всех серверах из бд"""
    return session.query(Server).all()


def get_users_stats(session: Session, limit=25, skip=0) -> UserTop:
    """Возвращает UserTop"""
    valid_users = session.query(OrmUserStat).filter(OrmUserStat.kills > 10)

    count: int = valid_users.count()

    top5_kills: list[UserStats] = valid_users.order_by(desc(OrmUserStat.kills)).limit(limit=5).all()
    top5_damage: list[UserStats] = valid_users.order_by(desc(OrmUserStat.dmg)).limit(limit=5).all()
    top5_time: list[UserStats] = valid_users.order_by(desc(OrmUserStat.connection_time)).limit(limit=5).all()

    users: list[UserStats] = valid_users.order_by(desc('skill')).offset(offset=skip).limit(limit=limit).all()

    return UserTop(count=count, items=users, top5_time=top5_time, top5_kills=top5_kills, top5_damage=top5_damage)
