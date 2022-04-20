import schemas
from fastapi import FastAPI, Depends
from database import crud
from database.database import get_db
from sqlalchemy.orm import Session


app = FastAPI()


@app.get("/server/server_list/", response_model=list[schemas.ServerInfo])
def get_all_servers(db: Session = Depends(get_db)):
    return crud.get_servers_info(db)

