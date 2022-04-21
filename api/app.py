import schemas
from fastapi import FastAPI, Depends
from database import crud
from database.database import get_db
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://api.v-cs.ru"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/server/server_list", response_model=list[schemas.ServerInfo])
def get_all_servers(db: Session = Depends(get_db)):
    """Возвращает инфу о всех серверах"""
    return crud.get_servers_info(db)


@app.get("/users/top", response_model=schemas.UserTop)
def get_all_users(limit: int = 25, skip: int = 0, db: Session = Depends(get_db)):
    """Возвращает инфу о пользователях"""
    return crud.get_users_stats(db, limit=limit, skip=skip)

