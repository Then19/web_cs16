from modeles import Server
from database import get_session


def add_new_server(host: str, port: int):
    """Добавляет новый сервер в базу данных"""
    with get_session() as session:
        s = Server(host=host, port=port)
        session.add(s)
        session.commit()


def get_all_servers() -> list[Server]:
    """Возвращает список всех серверов из бд"""
    with get_session() as session:
        return session.query(Server).all()


def update_info_by_id(server_id: int, new: Server):
    """Обновляет информацию о сервере по id"""
    with get_session() as session:
        session.query(Server).filter_by(id=server_id).update(new.get_update_dict())
        session.commit()


if __name__ == "__main__":
    for i in range(27016, 27025):
        add_new_server('92.255.175.170', i)
