import valve.source.a2s as a2s
from modeles import Server
from crud import get_all_servers, update_info_by_id
from time import sleep


def get_server_info(host: str, port: int):
    srv = Server()
    srv.host = host
    srv.port = port

    try:
        with a2s.ServerQuerier((host, port), timeout=2) as serv:
            server_info = serv.info()
    except Exception as ex:
        print(ex)
        return srv

    srv.name = server_info.get('server_name', '')
    srv.map = server_info.get('map', '')
    srv.count_players = server_info.get('player_count', 0)
    srv.max_players = server_info.get('max_players', 0)
    return srv


while True:
    for server in get_all_servers():
        upd_server = get_server_info(server.host, server.port)
        if not upd_server.equal(server):
            update_info_by_id(server.id, upd_server)
        sleep(1.5)
