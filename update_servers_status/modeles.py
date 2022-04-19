from database import Base, engine
from sqlalchemy import Column, Integer, String


class Server(Base):
    __tablename__ = 'servers_info'

    id = Column(Integer, primary_key=True)
    host: str = Column(String(50))
    port: int = Column(Integer)
    name: str = Column(String(100), default="None")
    map: str = Column(String(50), default='None')
    count_players: int = Column(Integer, default=0)
    max_players: int = Column(Integer, default=0)

    def __repr__(self):
        return '<Server(ip: %s, port: %s, name: %s)>' % (self.host, self.port, self.name)

    def get_update_dict(self):
        return {'name': self.name, 'map': self.map,
                'count_players': self.count_players, 'max_players': self.max_players}

    def equal(self, value):
        """Принимает в себя такой же объект и сравнивает их"""
        return self.get_update_dict() == value.get_update_dict()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
