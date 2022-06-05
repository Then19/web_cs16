from sqlalchemy import desc, asc
from sqlalchemy.orm import Session, Query
from schemas import ServerInfo, UserStats, UserTop, UserTopInfo, WeaponStats
from database.modeles import Server, OrmUserStat, OrmWeaponsStat


def get_servers_info(session: Session) -> list[ServerInfo]:
    """Возвращает информацию о всех серверах из бд"""
    return session.query(Server).filter(Server.map != None).all()


def get_users_stats(session: Session, limit=25, skip=0, sort='skill', reverse=True) -> UserTop:
    """Возвращает UserTop"""
    valid_users = session.query(OrmUserStat).filter(OrmUserStat.deaths > 10)
    count: int = valid_users.count()
    sort_as = desc if reverse else asc

    if sort == 'kd':
        sort_as = sort_as(OrmUserStat.kills / OrmUserStat.deaths)
    elif sort == 'acc':
        sort_as = sort_as(OrmUserStat.hits / OrmUserStat.shots)
    else:
        sort_as = sort_as(sort)

    users: list[UserStats] = valid_users.order_by(sort_as).offset(offset=skip).limit(limit=limit).all()
    return UserTop(count=count, items=users)


def get_users_top_info(session: Session) -> UserTopInfo:
    """Возвращает UserTopInfo (top 5)"""
    valid_users = session.query(OrmUserStat).filter(OrmUserStat.deaths > 25)
    top5_kills: list[UserStats] = valid_users.order_by(desc(OrmUserStat.kills)).limit(limit=5).all()
    top5_kd: list[UserStats] = valid_users.order_by(desc(OrmUserStat.kills / OrmUserStat.deaths)).limit(limit=5).all()
    top5_time: list[UserStats] = valid_users.order_by(desc(OrmUserStat.connection_time)).limit(limit=5).all()

    return UserTopInfo(top5_time=top5_time, top5_kills=top5_kills, top5_kd=top5_kd)


def get_user_by_id(session: Session, user_id: int) -> UserStats:
    """Возвращает объект пользователя по id"""
    return session.query(OrmUserStat).filter_by(id=user_id).first()


def get_user_by_steam_id(session: Session, steam_id: str) -> UserStats:
    """Возвращает объект пользователя по steam_id"""
    return session.query(OrmUserStat).filter_by(steamid=steam_id).first()


def get_weapons_stats(session: Session, user_id: int) -> list[WeaponStats]:
    """Возвращает список оружия со статистикой"""
    return session.query(OrmWeaponsStat).filter_by(player_id=user_id).all()
