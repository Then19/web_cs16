from sqlalchemy.orm import Session
from database import crud
from database.database import get_db, get_session
import schemas
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
import asyncio


class WSManager:
    def __init__(self):
        self.connections: list[WebSocket] = []
        self.server_status = self.get_server_online()
        asyncio.create_task(self.update_servers_info())
        asyncio.create_task(self.send_data_loop())

    @staticmethod
    def get_server_online():
        with get_session() as db:
            return schemas.ServerList(data=crud.get_servers_info(db)).dict()

    async def update_servers_info(self):
        while True:
            await asyncio.sleep(10)
            try:
                self.server_status = self.get_server_online()
            except Exception as ex:
                print(ex)

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)
        await websocket.send_json({"online": len(self.connections), 'servers': self.server_status})

    async def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def send_data_loop(self):
        while True:
            await asyncio.sleep(10)
            for connection in self.connections:
                try:
                    await connection.send_json({"online": len(self.connections), 'servers': self.server_status})
                except WebSocketDisconnect:
                    await self.disconnect(connection)


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


