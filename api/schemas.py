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
    shots: int = Field(title="Всего выстрелов")
    hits: int = Field(title="Попаданий")
    dmg: int
    bombdef: int
    bombdefused: int
    bombplants: int
    bombexplosions: int
    h_0: int
    h_1: int = Field(title="Выстрелов в голову")
    h_2: int = Field(title="Выстрелов в грудь")
    h_3: int = Field(title="Выстрелов в живот")
    h_4: int = Field(title="Выстрелов в левую руку")
    h_5: int = Field(title="Выстрелов в правую руку")
    h_6: int = Field(title="Выстрелов в левую ногу")
    h_7: int = Field(title="Выстрелов в правую ногу")
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
