from sqlalchemy.orm import Session
from database import crud
from database.database import get_db
import schemas
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect


class WSManager:
    def __init__(self):
        self.connections: list[WebSocket] = []
        self.online = 0

    async def connect(self, websocket: WebSocket):
        self.online += 1
        await websocket.accept()
        self.connections.append(websocket)
        await self.send_data()

    async def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)
        self.online -= 1
        await self.send_data()

    async def send_data(self):
        for connection in self.connections:
            await connection.send_json({"online": self.online})


router = APIRouter(
    prefix='/server',
    tags=['Server'],
    responses={404: {"description": "Not found"}}

)

manager = WSManager()


@router.websocket("/status")
async def status_info(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
    except WebSocketDisconnect:
        await manager.disconnect(websocket)


@router.get("/server_list", response_model=list[schemas.ServerInfo])
def get_all_servers(db: Session = Depends(get_db)):
    """Возвращает инфу о всех серверах"""
    return crud.get_servers_info(db)


