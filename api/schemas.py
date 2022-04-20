from pydantic import BaseModel


class ServerInfo(BaseModel):
    id: int
    host: str
    port: int
    name: str
    map: str
    count_players: int
    max_players: int

    class Config:
        orm_mode = True
