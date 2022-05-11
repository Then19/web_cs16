from sqlalchemy.orm import Session
from database import crud
from database.database import get_db
import schemas
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix='/users',
    tags=['Users'],
    responses={404: {"description": "Not found"}}
)


@router.get("/top", response_model=schemas.UserTop)
def get_all_users(limit: int = 25, skip: int = 0, db: Session = Depends(get_db)):
    """Возвращает инфу о пользователях"""
    if limit > 100: limit = 100
    return crud.get_users_stats(db, limit=limit, skip=skip)


@router.get("/top_info", response_model=schemas.UserTopInfo)
def get_all_users(db: Session = Depends(get_db)):
    """Возвращает инфу о пользователях (Топ 5 по киллам времени и тд)"""
    return crud.get_users_top_info(db)


@router.get("/user", response_model=schemas.UserStats)
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


@router.get('/weapons', response_model=list[schemas.WeaponStats])
def get_users_weapon(user_id: int, db: Session = Depends(get_db)):
    """Возвращает список со статистикой оружия пользователя по user_id"""
    user = crud.get_weapons_stats(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user
