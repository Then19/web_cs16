import schemas
from fastapi import FastAPI, Depends, HTTPException
from database import crud
from database.database import get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="ServerInfoAPI",
    version='0.0.1'
)

origins = [
    "http://localhost:3000",
    "https://v-cs.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/server/server_list", response_model=list[schemas.ServerInfo], tags=['Server'])
def get_all_servers(db: Session = Depends(get_db)):
    """Возвращает инфу о всех серверах"""
    return crud.get_servers_info(db)


@app.get("/users/top", response_model=schemas.UserTop, tags=['Users'])
def get_all_users(limit: int = 25, skip: int = 0, db: Session = Depends(get_db)):
    """Возвращает инфу о пользователях"""
    if limit > 100: limit = 100
    return crud.get_users_stats(db, limit=limit, skip=skip)


@app.get("/users/top_info", response_model=schemas.UserTopInfo, tags=['Users'])
def get_all_users(db: Session = Depends(get_db)):
    """Возвращает инфу о пользователях (Топ 5 по киллам времени и тд)"""
    return crud.get_users_top_info(db)


@app.get("/users/user", response_model=schemas.UserStats, tags=['Users'])
def get_user(user_id: int = 0, steam_id: str = '', db: Session = Depends(get_db)):
    """Возврацает объект польователя, Принимает user_id либо steam_id

    Если были переданы оба аргумента то поиск будет проходить по user_id"""
    if not user_id and not steam_id:
        raise HTTPException(status_code=400,
                            detail='Должен быть передан хотя бы один из пареметров: (user_id or steam_id)')
    user = crud.get_user_by_id(db, user_id=user_id) if user_id else crud.get_user_by_steam_id(db, steam_id=steam_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user



