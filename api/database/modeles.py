from database.database import Base
from sqlalchemy import Column, Integer, String


class Server(Base):
    __tablename__ = 'servers_info'

    id = Column(Integer, primary_key=True)
    host: str = Column(String)
    port: int = Column(Integer)
    name: str = Column(String)
    map: str = Column(String)
    count_players: int = Column(Integer)
    max_players: int = Column(Integer)

