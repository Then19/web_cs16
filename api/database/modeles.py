from database.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime


class Server(Base):
    __tablename__ = 'servers_info'

    id = Column(Integer, primary_key=True)
    host: str = Column(String)
    port: int = Column(Integer)
    name: str = Column(String)
    map: str = Column(String)
    count_players: int = Column(Integer)
    max_players: int = Column(Integer)


class OrmUserStat(Base):
    __tablename__ = 'csstats'

    id = Column(Integer, primary_key=True)
    steamid = Column(String)
    name = Column(String)
    skill = Column(Float)
    kills = Column(Integer)
    deaths = Column(Integer)
    hs = Column(Integer)
    tks = Column(Integer)
    shots = Column(Integer)
    hits = Column(Integer)
    dmg = Column(Integer)
    bombdef = Column(Integer)
    bombdefused = Column(Integer)
    bombplants = Column(Integer)
    bombexplosions = Column(Integer)
    h_0 = Column(Integer)
    h_1 = Column(Integer)
    h_2 = Column(Integer)
    h_3 = Column(Integer)
    h_4 = Column(Integer)
    h_5 = Column(Integer)
    h_6 = Column(Integer)
    h_7 = Column(Integer)
    connection_time = Column(Integer)
    connects = Column(Integer)
    roundt = Column(Integer)
    wint = Column(Integer)
    roundct = Column(Integer)
    winct = Column(Integer)
    assists = Column(Integer)
    first_join = Column(DateTime)
    last_join = Column(DateTime)


class OrmWeaponsStat(Base):
    __tablename__ = 'csstats_weapons'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer)
    weapon = Column(String)
    kills = Column(Integer)
    deaths = Column(Integer)
    hs = Column(Integer)
    tks = Column(Integer)
    shots = Column(Integer)
    hits = Column(Integer)
    dmg = Column(Integer)
    h_0 = Column(Integer)
    h_1 = Column(Integer)
    h_2 = Column(Integer)
    h_3 = Column(Integer)
    h_4 = Column(Integer)
    h_5 = Column(Integer)
    h_6 = Column(Integer)
    h_7 = Column(Integer)
