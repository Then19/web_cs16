from pydantic import BaseModel, Field
from datetime import datetime


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


class UserStats(BaseModel):
    id: int
    steamid: str
    name: str
    skill: float
    kills: int
    deaths: int
    hs: int
    tks: int = Field(title="Team kills")
    shots: int
    hits: int
    dmg: int
    bombdef: int
    bombdefused: int
    bombplants: int
    bombexplosions: int
    h_0: int
    h_1: int
    h_2: int
    h_3: int
    h_4: int
    h_5: int
    h_6: int
    h_7: int
    connection_time: int
    connects: int
    roundt: int
    wint: int
    roundct: int
    winct: int
    assists: int
    first_join: datetime
    last_join: datetime

    class Config:
        orm_mode = True


class UserTop(BaseModel):
    count: int
    items: list[UserStats]
    top5_kills: list[UserStats]
    top5_damage: list[UserStats]
    top5_time: list[UserStats]
