from sqlalchemy.orm import Session
from database import crud
from database.database import get_db
import schemas
from fastapi import APIRouter, Depends, HTTPException


router = APIRouter(
    prefix='/server',
    tags=['Server'],
    responses={404: {"description": "Not found"}}

)


@router.get("/server/server_list", response_model=list[schemas.ServerInfo])
def get_all_servers(db: Session = Depends(get_db)):
    """Возвращает инфу о всех серверах"""
    return crud.get_servers_info(db)
